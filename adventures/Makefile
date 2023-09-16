.PHONY: texdirs 
texdirs := $(wildcard */main.tex)

.PHONY: adventures
adventures: $(patsubst %/main.tex,%.pdf,$(texdirs))

%.pdf: %/main.pdf
	cp $< $@

%/main.pdf: %/main.tex
	latexmk -pdf -cd $<
	latexmk -c -cd $<

clean: $(texdirs)
	$(RM) *.pdf
