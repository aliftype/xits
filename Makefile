NAME=xits
VERSION=1.106

SRC=sources
DOC=documentation
DOCSRC=$(DOC)/$(DOC)-$(SRC)
DIST=$(NAME)-$(VERSION)

FF=fontforge -lang=ff
POSTPROCESS=./postprocess.py
FFLAGES=0x200000
SCRIPT='Open($$1);\
       if ($$argc>3)\
         MergeFeature($$2);\
       endif;\
       SetFontNames("","","","","","$(VERSION)");\
       Generate($$argv[$$argc-1], "", $(FFLAGES))'

FONTS=math mathbold regular bold italic bolditalic
DOCS=user-guide xits-specimen
FEA=xits.fea

SFD=$(FONTS:%=$(SRC)/$(NAME)-%.sfd)
OTF=$(FONTS:%=$(NAME)-%.otf)
TEX=$(DOCS:%=$(DOCSRC)/%.tex)
PDF=$(DOCS:%=$(DOC)/%.pdf)

all: otf

otf: $(OTF)

xits-math.otf: $(SRC)/xits-math.sfd Makefile $(POSTPROCESS)
	@echo "Building $@"
	@$(FF) -c $(SCRIPT) $< $@ 2>/dev/stdout 1>/dev/stderr | tail -n +4
	@$(POSTPROCESS) $@
	@mv $@.post $@

xits-mathbold.otf: $(SRC)/xits-mathbold.sfd Makefile $(POSTPROCESS)
	@echo "Building $@"
	@$(FF) -c $(SCRIPT) $< $@ 2>/dev/stdout 1>/dev/stderr | tail -n +4
	@$(POSTPROCESS) $@
	@mv $@.post $@

%.otf: $(SRC)/%.sfd Makefile $(POSTPROCESS)
	@echo "Building $@"
	@$(FF) -c $(SCRIPT) $< $(SRC)/$(FEA) $@ 2>/dev/stdout 1>/dev/stderr | tail -n +4
	@$(POSTPROCESS) $@
	@mv $@.post $@

doc: $(PDF)

$(DOC)/%.pdf: $(DOCSRC)/%.tex
	@echo "Building $@"
	@context --nonstopmode --result=$@ $< 1>/dev/null

FONTLOG.txt: FONTLOG.txt.in
	@echo "Generating $@"
	@./tools/fontcoverage.py tools/Blocks.txt $< $(SFD) > $@

dist: $(OTF) $(PDF) FONTLOG.txt
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(DOC)
	@mkdir -p $(DIST)/$(DOCSRC)
	@cp $(SFD) $(DIST)/$(SRC)
	@cp $(SRC)/$(FEA) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)
	@cp -r $(PDF) $(DIST)/$(DOC)
	@cp -r $(TEX) $(DIST)/$(DOCSRC)
	@cp -r $(POSTPROCESS) Makefile OFL-FAQ.txt OFL.txt FONTLOG.txt tex $(DIST)
	@cp README.md $(DIST)/README.txt
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(DIST) $(DIST).zip
