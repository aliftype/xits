NAME=xits
VERSION=1.108

SRC=sources
WEB=webfonts
DOC=documentation
TOOLS=tools
DOCSRC=$(DOC)/$(DOC)-$(SRC)
DIST=$(NAME)-$(VERSION)

PY=python
MAKEFNT=$(TOOLS)/makefnt.py
MAKEWEB=$(TOOLS)/makeweb.py
COVERAGE=$(TOOLS)/fontcoverage.py

FONTS=math mathbold regular bold italic bolditalic
DOCS=user-guide xits-specimen

SFD=$(FONTS:%=$(SRC)/$(NAME)-%.sfd)
OTF=$(FONTS:%=$(NAME)-%.otf)
WOF=$(FONTS:%=$(WEB)/$(NAME)-%.woff)
EOT=$(FONTS:%=$(WEB)/$(NAME)-%.eot)
TEX=$(DOCS:%=$(DOCSRC)/%.tex)
PDF=$(DOCS:%=$(DOC)/%.pdf)

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

doc: $(PDF)

$(DOC)/%.pdf: $(DOCSRC)/%.tex
	@echo "Building $@"
	@context --nonstopmode --result=$@ $< 1>/dev/null

FONTLOG.txt: FONTLOG.txt.in $(COVERAGE) $(OTF)
	@echo "Generating $@"
	@$(PY) $(COVERAGE) tools/Blocks.txt $< $(OTF) $@

dist: $(OTF) $(WOF) $(PDF) FONTLOG.txt
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(DOC)
	@mkdir -p $(DIST)/$(DOCSRC)
	@mkdir -p $(DIST)/$(TOOLS)
	@cp $(SFD) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)
	@cp $(MAKEFNT) $(COVERAGE) $(DIST)/$(TOOLS)
	@cp -r $(PDF) $(DIST)/$(DOC)
	@cp -r $(TEX) $(DIST)/$(DOCSRC)
	@cp -r Makefile OFL-FAQ.txt OFL.txt FONTLOG.txt tex $(DIST)
	@cp README.md $(DIST)/README.txt
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(DIST) $(DIST).zip
