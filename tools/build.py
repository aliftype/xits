import sys

import fontforge

infile, outfile, version = sys.argv[1:4]

font = fontforge.open(infile)

for glyph in font.glyphs():
    glyph.unlinkRmOvrlpSave = True

if len(sys.argv) > 4:
  font.mergeFeature(sys.argv[4])

font.version = version
font.generate(outfile, flags=("round", "opentype"))
