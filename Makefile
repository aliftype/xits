NAME=XITS
VERSION=1.200

SRC=sources
WEB=webfonts
TOOLS=tools
DIST=$(NAME)-$(VERSION)

PY=python
MAKEFNT=$(TOOLS)/makefnt.py
MAKEWEB=$(TOOLS)/makeweb.py
COVERAGE=$(TOOLS)/fontcoverage.py

FONTS=$(NAME)Math-Regular $(NAME)Math-Bold \
      $(NAME)-Regular $(NAME)-Bold $(NAME)-Italic $(NAME)-BoldItalic

SFD=$(FONTS:%=$(SRC)/%.sfd)
OTF=$(FONTS:%=%.otf)
WOF=$(FONTS:%=$(WEB)/%.woff)

all: otf

otf: $(OTF)
web: $(WOF)

%.otf: $(SRC)/%.sfd $(SRC)/%.fea
	@echo "Building $@"
	@$(PY) $(MAKEFNT) $< $@ --version=$(VERSION) --features=$(word 2,$+)

$(WEB)/%.woff: %.otf
	@echo "Building $@"
	@mkdir -p $(WEB)
	@$(PY) $(MAKEWEB) $< $(WEB)

FONTLOG.txt: FONTLOG.txt.in $(COVERAGE) $(OTF)
	@echo "Generating $@"
	@$(PY) $(COVERAGE) tools/Blocks.txt $< $(OTF) $@

dist: $(OTF) $(WOF) FONTLOG.txt
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(WEB)
	@cp $(OTF) $(DIST)
	@cp $(WOF) $(DIST)/$(WEB)
	@cp -r OFL-FAQ.txt OFL.txt FONTLOG.txt $(DIST)
	@cp README.md $(DIST)/README.txt
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(DIST) $(DIST).zip
