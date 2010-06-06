#!/usr/bin/python

import fontforge
import os

family = "xits"
styles = ("math", "regular", "bold", "italic", "bolditalic")
flags  = ("opentype",)
source = "sources"

for style in styles:
    print "Generating %s..." % style
    font = fontforge.open(os.path.join(source, family+"-"+style+".sfd"))
    font . mergeFeature  (os.path.join(source, family+".fea"))
    font . generate(family+"-"+style+".otf", flags=flags)
    font . close()
