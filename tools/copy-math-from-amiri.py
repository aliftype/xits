import sys
from sortsmill import ffcompat as fontforge


amiri = fontforge.open(sys.argv[1])
xits = fontforge.open(sys.argv[2])

amiri.em = 1000
amiri.layers[1].is_quadratic = 0
amiri.selection.all()
amiri.unlinkReferences()

names = []
alts = []
for aglyph in amiri.glyphs():
    u = aglyph.unicode
    if 0x1EEFF >= u >= 0x1EE00:
        names.append(aglyph.name)

for aglyph in amiri.glyphs():
    for name in names:
        if aglyph.name != name and aglyph.name.startswith(name):
            alts.append(aglyph.name)

for name in names + alts:
    aglyph = amiri[name]
    if aglyph.name not in xits:
        xits.createChar(aglyph.unicode, aglyph.name)
    xglyph = xits[aglyph.name]
    aglyph.draw(xglyph.glyphPen())
    xglyph.width = aglyph.width
    xglyph.round()
    xglyph.autoHint()

for name in alts:
    base, ext = name.split(".")
    if ext.startswith("alt"):
        xits[base].addPosSub("'cv00' Alternate Arabic Math symbols-1", name)
    elif ext.startswith("display"):
        xits[base].verticalVariants = (xits[base], xits[name])
    else:
        print "Unknown alternate glyph:", name

xits.save()
