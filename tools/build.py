import os
import sys

import fontforge
from fontTools.ttLib import TTFont

infile, outfile, version = sys.argv[1:4]

mods = [os.stat(infile).st_mtime]

font = fontforge.open(infile)

for glyph in font.glyphs():
    glyph.unlinkRmOvrlpSave = True

if len(sys.argv) > 4:
  mods += [os.stat(sys.argv[4]).st_mtime]
  font.mergeFeature(sys.argv[4])

os.environ["SOURCE_DATE_EPOCH"] = "%d" % max(mods)

font.appendSFNTName("English (US)", "UniqueID", "%s;%s;%s" % (version,
    font.os2_vendor, font.fontname))

font.version = version
font.generate(outfile, flags=("round", "opentype"))

ttfont = TTFont(outfile)

# Drop useless table with timestamp
if "FFTM" in ttfont:
    del ttfont["FFTM"]

ttfont.save(outfile)
