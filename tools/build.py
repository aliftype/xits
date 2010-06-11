#!/usr/bin/python

import fontforge
import os
import sys


family = "xits"
styles = ("math", "regular", "bold", "italic", "bolditalic")
flags  = ("opentype",)
source = "sources"
args   = [ ]

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
    font . mergeFeature  (os.path.join(source, family+".fea"))
    font . generate(family+"-"+style+".otf", flags=flags)
    font . close()
