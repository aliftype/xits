#!/usr/bin/python

import fontforge
import tempfile
import os
import sys


family = "xits"
styles = ("math", "regular", "bold", "italic", "bolditalic")
flags  = ("opentype",)
source = "sources"
args   = [ ]

def doPUA(font):
    print "Assigning unencoded glyphs to PUA..."
    pua = 0x100000
    for glyph in font.glyphs():
        if glyph.unicode == -1 and glyph.glyphname != ".notdef":
            glyph.unicode = pua
            pua += 1

if len(sys.argv) > 1:
    args = list(sys.argv[1:])

for arg in args:
    if arg == "all":
        args = styles
    elif not arg in styles:
        print "Unknown style requested: %s" %arg
        args.remove(arg)

if len(args) == 0:
    args = styles

for style in args:
    print "Generating %s..." % style
    xits = fontforge.open(os.path.join(source, family+"-"+style+".sfd"))
    if style == "math":
        doPUA(xits)
        # XXX: if we don't save the font and reload it, the generated font
        # contian invalid code points (outside Unicode) instead of PUA
        tmpfont = tempfile.mkstemp()[1]
        xits.save(tmpfont)
        xits.close()
        xits = fontforge.open(tmpfont)
    xits.mergeFeature  (os.path.join(source, family+".fea"))
    xits.generate(family+"-"+style+".otf", flags=flags)
    xits.close()
