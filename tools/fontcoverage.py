#!/usr/bin/env python
from __future__ import division
import sys
import fontforge
import unicodedata

"""
Unicode blocks list generated from:
    http://www.unicode.org/Public/5.2.0/ucd/Blocks.txt

With the follwing code snippet:

    file = open("Blocks.txt", "r")
    blocks = [ ]
    for line in file.readlines():
        if not (line.startswith("#") or line == "\n"):
            start, end   = line.split("; ")[0].split("..")
            name         = line.split("; ")[1].strip()
            blocks.append((name, (start, end)))
"""
blocks = [
 ('Basic Latin', ('0000', '007F')),
 ('Latin-1 Supplement', ('0080', '00FF')),
 ('Latin Extended-A', ('0100', '017F')),
 ('Latin Extended-B', ('0180', '024F')),
 ('IPA Extensions', ('0250', '02AF')),
 ('Spacing Modifier Letters', ('02B0', '02FF')),
 ('Combining Diacritical Marks', ('0300', '036F')),
 ('Greek and Coptic', ('0370', '03FF')),
 ('Cyrillic', ('0400', '04FF')),
 ('Cyrillic Supplement', ('0500', '052F')),
 ('Armenian', ('0530', '058F')),
 ('Hebrew', ('0590', '05FF')),
 ('Arabic', ('0600', '06FF')),
 ('Syriac', ('0700', '074F')),
 ('Arabic Supplement', ('0750', '077F')),
 ('Thaana', ('0780', '07BF')),
 ('NKo', ('07C0', '07FF')),
 ('Samaritan', ('0800', '083F')),
 ('Devanagari', ('0900', '097F')),
 ('Bengali', ('0980', '09FF')),
 ('Gurmukhi', ('0A00', '0A7F')),
 ('Gujarati', ('0A80', '0AFF')),
 ('Oriya', ('0B00', '0B7F')),
 ('Tamil', ('0B80', '0BFF')),
 ('Telugu', ('0C00', '0C7F')),
 ('Kannada', ('0C80', '0CFF')),
 ('Malayalam', ('0D00', '0D7F')),
 ('Sinhala', ('0D80', '0DFF')),
 ('Thai', ('0E00', '0E7F')),
 ('Lao', ('0E80', '0EFF')),
 ('Tibetan', ('0F00', '0FFF')),
 ('Myanmar', ('1000', '109F')),
 ('Georgian', ('10A0', '10FF')),
 ('Hangul Jamo', ('1100', '11FF')),
 ('Ethiopic', ('1200', '137F')),
 ('Ethiopic Supplement', ('1380', '139F')),
 ('Cherokee', ('13A0', '13FF')),
 ('Unified Canadian Aboriginal Syllabics', ('1400', '167F')),
 ('Ogham', ('1680', '169F')),
 ('Runic', ('16A0', '16FF')),
 ('Tagalog', ('1700', '171F')),
 ('Hanunoo', ('1720', '173F')),
 ('Buhid', ('1740', '175F')),
 ('Tagbanwa', ('1760', '177F')),
 ('Khmer', ('1780', '17FF')),
 ('Mongolian', ('1800', '18AF')),
 ('Unified Canadian Aboriginal Syllabics Extended', ('18B0', '18FF')),
 ('Limbu', ('1900', '194F')),
 ('Tai Le', ('1950', '197F')),
 ('New Tai Lue', ('1980', '19DF')),
 ('Khmer Symbols', ('19E0', '19FF')),
 ('Buginese', ('1A00', '1A1F')),
 ('Tai Tham', ('1A20', '1AAF')),
 ('Balinese', ('1B00', '1B7F')),
 ('Sundanese', ('1B80', '1BBF')),
 ('Lepcha', ('1C00', '1C4F')),
 ('Ol Chiki', ('1C50', '1C7F')),
 ('Vedic Extensions', ('1CD0', '1CFF')),
 ('Phonetic Extensions', ('1D00', '1D7F')),
 ('Phonetic Extensions Supplement', ('1D80', '1DBF')),
 ('Combining Diacritical Marks Supplement', ('1DC0', '1DFF')),
 ('Latin Extended Additional', ('1E00', '1EFF')),
 ('Greek Extended', ('1F00', '1FFF')),
 ('General Punctuation', ('2000', '206F')),
 ('Superscripts and Subscripts', ('2070', '209F')),
 ('Currency Symbols', ('20A0', '20CF')),
 ('Combining Diacritical Marks for Symbols', ('20D0', '20FF')),
 ('Letterlike Symbols', ('2100', '214F')),
 ('Number Forms', ('2150', '218F')),
 ('Arrows', ('2190', '21FF')),
 ('Mathematical Operators', ('2200', '22FF')),
 ('Miscellaneous Technical', ('2300', '23FF')),
 ('Control Pictures', ('2400', '243F')),
 ('Optical Character Recognition', ('2440', '245F')),
 ('Enclosed Alphanumerics', ('2460', '24FF')),
 ('Box Drawing', ('2500', '257F')),
 ('Block Elements', ('2580', '259F')),
 ('Geometric Shapes', ('25A0', '25FF')),
 ('Miscellaneous Symbols', ('2600', '26FF')),
 ('Dingbats', ('2700', '27BF')),
 ('Miscellaneous Mathematical Symbols-A', ('27C0', '27EF')),
 ('Supplemental Arrows-A', ('27F0', '27FF')),
 ('Braille Patterns', ('2800', '28FF')),
 ('Supplemental Arrows-B', ('2900', '297F')),
 ('Miscellaneous Mathematical Symbols-B', ('2980', '29FF')),
 ('Supplemental Mathematical Operators', ('2A00', '2AFF')),
 ('Miscellaneous Symbols and Arrows', ('2B00', '2BFF')),
 ('Glagolitic', ('2C00', '2C5F')),
 ('Latin Extended-C', ('2C60', '2C7F')),
 ('Coptic', ('2C80', '2CFF')),
 ('Georgian Supplement', ('2D00', '2D2F')),
 ('Tifinagh', ('2D30', '2D7F')),
 ('Ethiopic Extended', ('2D80', '2DDF')),
 ('Cyrillic Extended-A', ('2DE0', '2DFF')),
 ('Supplemental Punctuation', ('2E00', '2E7F')),
 ('CJK Radicals Supplement', ('2E80', '2EFF')),
 ('Kangxi Radicals', ('2F00', '2FDF')),
 ('Ideographic Description Characters', ('2FF0', '2FFF')),
 ('CJK Symbols and Punctuation', ('3000', '303F')),
 ('Hiragana', ('3040', '309F')),
 ('Katakana', ('30A0', '30FF')),
 ('Bopomofo', ('3100', '312F')),
 ('Hangul Compatibility Jamo', ('3130', '318F')),
 ('Kanbun', ('3190', '319F')),
 ('Bopomofo Extended', ('31A0', '31BF')),
 ('CJK Strokes', ('31C0', '31EF')),
 ('Katakana Phonetic Extensions', ('31F0', '31FF')),
 ('Enclosed CJK Letters and Months', ('3200', '32FF')),
 ('CJK Compatibility', ('3300', '33FF')),
 ('CJK Unified Ideographs Extension A', ('3400', '4DBF')),
 ('Yijing Hexagram Symbols', ('4DC0', '4DFF')),
 ('CJK Unified Ideographs', ('4E00', '9FFF')),
 ('Yi Syllables', ('A000', 'A48F')),
 ('Yi Radicals', ('A490', 'A4CF')),
 ('Lisu', ('A4D0', 'A4FF')),
 ('Vai', ('A500', 'A63F')),
 ('Cyrillic Extended-B', ('A640', 'A69F')),
 ('Bamum', ('A6A0', 'A6FF')),
 ('Modifier Tone Letters', ('A700', 'A71F')),
 ('Latin Extended-D', ('A720', 'A7FF')),
 ('Syloti Nagri', ('A800', 'A82F')),
 ('Common Indic Number Forms', ('A830', 'A83F')),
 ('Phags-pa', ('A840', 'A87F')),
 ('Saurashtra', ('A880', 'A8DF')),
 ('Devanagari Extended', ('A8E0', 'A8FF')),
 ('Kayah Li', ('A900', 'A92F')),
 ('Rejang', ('A930', 'A95F')),
 ('Hangul Jamo Extended-A', ('A960', 'A97F')),
 ('Javanese', ('A980', 'A9DF')),
 ('Cham', ('AA00', 'AA5F')),
 ('Myanmar Extended-A', ('AA60', 'AA7F')),
 ('Tai Viet', ('AA80', 'AADF')),
 ('Meetei Mayek', ('ABC0', 'ABFF')),
 ('Hangul Syllables', ('AC00', 'D7AF')),
 ('Hangul Jamo Extended-B', ('D7B0', 'D7FF')),
 ('High Surrogates', ('D800', 'DB7F')),
 ('High Private Use Surrogates', ('DB80', 'DBFF')),
 ('Low Surrogates', ('DC00', 'DFFF')),
 ('Private Use Area', ('E000', 'F8FF')),
 ('CJK Compatibility Ideographs', ('F900', 'FAFF')),
 ('Alphabetic Presentation Forms', ('FB00', 'FB4F')),
 ('Arabic Presentation Forms-A', ('FB50', 'FDFF')),
 ('Variation Selectors', ('FE00', 'FE0F')),
 ('Vertical Forms', ('FE10', 'FE1F')),
 ('Combining Half Marks', ('FE20', 'FE2F')),
 ('CJK Compatibility Forms', ('FE30', 'FE4F')),
 ('Small Form Variants', ('FE50', 'FE6F')),
 ('Arabic Presentation Forms-B', ('FE70', 'FEFF')),
 ('Halfwidth and Fullwidth Forms', ('FF00', 'FFEF')),
 ('Specials', ('FFF0', 'FFFF')),
 ('Linear B Syllabary', ('10000', '1007F')),
 ('Linear B Ideograms', ('10080', '100FF')),
 ('Aegean Numbers', ('10100', '1013F')),
 ('Ancient Greek Numbers', ('10140', '1018F')),
 ('Ancient Symbols', ('10190', '101CF')),
 ('Phaistos Disc', ('101D0', '101FF')),
 ('Lycian', ('10280', '1029F')),
 ('Carian', ('102A0', '102DF')),
 ('Old Italic', ('10300', '1032F')),
 ('Gothic', ('10330', '1034F')),
 ('Ugaritic', ('10380', '1039F')),
 ('Old Persian', ('103A0', '103DF')),
 ('Deseret', ('10400', '1044F')),
 ('Shavian', ('10450', '1047F')),
 ('Osmanya', ('10480', '104AF')),
 ('Cypriot Syllabary', ('10800', '1083F')),
 ('Imperial Aramaic', ('10840', '1085F')),
 ('Phoenician', ('10900', '1091F')),
 ('Lydian', ('10920', '1093F')),
 ('Kharoshthi', ('10A00', '10A5F')),
 ('Old South Arabian', ('10A60', '10A7F')),
 ('Avestan', ('10B00', '10B3F')),
 ('Inscriptional Parthian', ('10B40', '10B5F')),
 ('Inscriptional Pahlavi', ('10B60', '10B7F')),
 ('Old Turkic', ('10C00', '10C4F')),
 ('Rumi Numeral Symbols', ('10E60', '10E7F')),
 ('Kaithi', ('11080', '110CF')),
 ('Cuneiform', ('12000', '123FF')),
 ('Cuneiform Numbers and Punctuation', ('12400', '1247F')),
 ('Egyptian Hieroglyphs', ('13000', '1342F')),
 ('Byzantine Musical Symbols', ('1D000', '1D0FF')),
 ('Musical Symbols', ('1D100', '1D1FF')),
 ('Ancient Greek Musical Notation', ('1D200', '1D24F')),
 ('Tai Xuan Jing Symbols', ('1D300', '1D35F')),
 ('Counting Rod Numerals', ('1D360', '1D37F')),
 ('Mathematical Alphanumeric Symbols', ('1D400', '1D7FF')),
 ('Mahjong Tiles', ('1F000', '1F02F')),
 ('Domino Tiles', ('1F030', '1F09F')),
 ('Enclosed Alphanumeric Supplement', ('1F100', '1F1FF')),
 ('Enclosed Ideographic Supplement', ('1F200', '1F2FF')),
 ('CJK Unified Ideographs Extension B', ('20000', '2A6DF')),
 ('CJK Unified Ideographs Extension C', ('2A700', '2B73F')),
 ('CJK Compatibility Ideographs Supplement', ('2F800', '2FA1F')),
 ('Tags', ('E0000', 'E007F')),
 ('Variation Selectors Supplement', ('E0100', 'E01EF')),
 ('Supplementary Private Use Area-A', ('F0000', 'FFFFF')),
 ('Supplementary Private Use Area-B', ('100000', '10FFFF'))
]

font = fontforge.open(sys.argv[1])
font.encoding = "UnicodeFull"
found = [ ]

for block in blocks:
    t = f = 0
    name = block[0]
    start, end = int(block[1][0], 16), int(block[1][1], 16)
    i = start
    while (i <= end):
        category = unicodedata.category(unichr(i))
        if category != "Cc" and category!= "Cn":
            try:
                glyph = font[i]
                f += 1
            except TypeError:
                pass
            t += 1
        i += 1
    if f:
        found.append((name, (t,f)))


coverage  = ""
coverage += "* %s:\n" %font.fullname
for f in found:
    for b in blocks:
        if b[0] == f[0]:
            name = f[0]
            start, end = b[1]
            total, present = f[1]
            percent = present/total*100
            coverage += "  %s (U+%s-%s): %s/%s (%.2f%%)\n" %(name, start, end, present, total, percent)

print coverage
