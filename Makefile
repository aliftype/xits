NAME=xits
VERSION=1.010

SRC=sources
DOC=documentation
DOCSRC=$(DOC)/$(DOC)-$(SRC)
DIST=$(NAME)-$(VERSION)

FF=fontforge -lang=ff
FFLAGES=0x200000
SCRIPT='Open($$1); MergeFeature("$(SRC)/$(FEA)"); Generate($$2, "", $(FFLAGES))'

FONTS=math regular bold italic bolditalic
DOCS=user-guide xits-specimen
FEA=xits.fea

SFD=$(FONTS:%=$(SRC)/$(NAME)-%.sfd)
OTF=$(FONTS:%=$(NAME)-%.otf)
TEX=$(DOCS:%=$(DOCSRC)/%.tex)
PDF=$(DOCS:%=$(DOC)/%.pdf)

all: otf

otf: $(OTF)

%.otf: $(SRC)/%.sfd
	@echo "Generating $@"
	@$(FF) -c $(SCRIPT) $< $@ 2>/dev/stdout 1>/dev/stderr | tail -n +4

doc: $(PDF)

$(DOC)/%.pdf: $(DOCSRC)/%.tex
	@echo "Building $@"
	@context --nonstopmode --result=$@ $< 1>/dev/null

dist: $(OTF) $(PDF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/$(DOC)
	@mkdir -p $(DIST)/$(DOCSRC)
	@cp $(SFD) $(DIST)/$(SRC)
	@cp $(SRC)/$(FEA) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)
	@cp -r $(PDF) $(DIST)/$(DOC)
	@cp -r $(TEX) $(DIST)/$(DOCSRC)
	@cp README.md $(DIST)/README.txt
	@cp Makefile OFL-FAQ.txt OFL.txt FONTLOG.txt $(DIST)
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(DIST) $(DIST).zip
