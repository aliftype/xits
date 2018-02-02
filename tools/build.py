import argparse
import os

import fontforge
from fontTools.ttLib import TTFont


def postProcess(args):
    font = TTFont(args.output)

    # Drop useless table with timestamp
    if "FFTM" in font:
        del font["FFTM"]

    font.save(args.output)


def makeFont(args):
    mods = [os.stat(args.input).st_mtime]

    font = fontforge.open(args.input)

    for glyph in font.glyphs():
        glyph.unlinkRmOvrlpSave = True

    if args.features:
        mods += [os.stat(args.features).st_mtime]
        font.mergeFeature(args.features)

    os.environ["SOURCE_DATE_EPOCH"] = "%d" % max(mods)

    font.appendSFNTName("English (US)", "UniqueID", "%s;%s;%s" % (args.version,
        font.os2_vendor, font.fontname))

    font.version = args.version
    font.generate(args.output, flags=("round", "opentype"))

    postProcess(args)


def main():
    parser = argparse.ArgumentParser(description="Create web fonts.")
    parser.add_argument("input", help="input font file name")
    parser.add_argument("output", help="output font file name")
    parser.add_argument("--version", help="font version", required=True)
    parser.add_argument("--features", help="font features file name")

    args = parser.parse_args()

    makeFont(args)

if __name__ == "__main__":
    main()
