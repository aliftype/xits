import argparse
import os

from fontTools.ttLib import TTFont

def makeWeb(args):
    """If we are building a web version then try to minimise file size"""

    font = TTFont(args.file)

    base, ext = os.path.splitext(args.file)
    for flavor in ("woff", "woff2"):
        font.flavor = flavor
        font.save(args.dir + "/" + base + "." + flavor)
    font.close()


def main():
    parser = argparse.ArgumentParser(description="Create web fonts.")
    parser.add_argument("file", help="input font to process")
    parser.add_argument("dir", help="output directory to write fonts to")

    args = parser.parse_args()

    makeWeb(args)

if __name__ == "__main__":
    main()
