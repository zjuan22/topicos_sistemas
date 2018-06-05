pdflatex principal.tex
bibtex principal
# makeindex principal.idx
# makeindex principal.nlo -s nomencl.ist -o principal.nls
pdflatex principal.tex
pdflatex principal.tex
