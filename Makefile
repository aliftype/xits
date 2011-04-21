NAME=xits
VERSION=1.009

SRC=sources
DIST=$(NAME)-$(VERSION)

FF=fontforge -lang=ff
FFLAGES=0x200000
SCRIPT='Open($$1); MergeFeature("$(SRC)/$(FEA)"); Generate($$2, "", $(FFLAGES))'

FONTS=math regular bold italic bolditalic
SFD=$(FONTS:%=$(SRC)/$(NAME)-%.sfd)
OTF=$(FONTS:%=$(NAME)-%.otf)
FEA=xits.fea

all: otf

otf: $(OTF)

%.otf : $(SRC)/%.sfd
	@echo "Generating $@"
	@$(FF) -c $(SCRIPT) $< $@ 2>/dev/stdout 1>/dev/stderr | tail -n +4

dist: $(OTF)
	@echo "Making dist tarball"
	@mkdir -p $(DIST)/$(SRC)
	@mkdir -p $(DIST)/documentation
	@mkdir -p $(DIST)/documentation/documentation-sources
	@cp $(SFD) $(DIST)/$(SRC)
	@cp $(SRC)/$(FEA) $(DIST)/$(SRC)
	@cp $(OTF) $(DIST)
	@cp -r documentation/*.pdf $(DIST)/documentation
	@cp -r documentation/documentation-sources/*.tex $(DIST)/documentation/documentation-sources
	@cp README.md $(DIST)/README.txt
	@cp Makefile OFL-FAQ.txt OFL.txt FONTLOG.txt $(DIST)
	@zip -r $(DIST).zip $(DIST)

clean:
	@rm -rf $(OTF) $(DIST) $(DIST).zip
