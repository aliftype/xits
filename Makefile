NAME=xits
VERSION=1.108

SRC=sources
DOC=documentation
DOCSRC=$(DOC)/$(DOC)-$(SRC)
DIST=$(NAME)-$(VERSION)

PY=python
POSTPROCESS=./postprocess.py

define $(NAME)SCRIPT
import fontforge, sys
f = fontforge.open(sys.argv[1])
if len(sys.argv) > 3:
  f.mergeFeature(sys.argv[3])
f.version = "$(VERSION)"
f.generate(sys.argv[2], flags=("round", "opentype"))
endef

export $(NAME)SCRIPT

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
	@$(PY) -c "$$$(NAME)SCRIPT" $< $@
	@$(POSTPROCESS) $@
	@mv $@.post $@

xits-mathbold.otf: $(SRC)/xits-mathbold.sfd Makefile $(POSTPROCESS)
	@echo "Building $@"
	@$(PY) -c "$$$(NAME)SCRIPT" $< $@
	@$(POSTPROCESS) $@
	@mv $@.post $@

%.otf: $(SRC)/%.sfd Makefile $(SRC)/$(FEA) $(POSTPROCESS)
	@echo "Building $@"
	@$(PY) -c "$$$(NAME)SCRIPT" $< $@ $(SRC)/$(FEA)
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
