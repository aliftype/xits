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
    font = fontforge.open(os.path.join(source, family+"-"+style+".sfd"))
    if style == "math":
        doPUA(font)
        tmpfont = tempfile.mkstemp()[1]
        font.save(tmpfont)
        font.close()
        font = fontforge.open(tmpfont)
    font . mergeFeature  (os.path.join(source, family+".fea"))
    font . generate(family+"-"+style+".otf", flags=flags)
    font . close()
