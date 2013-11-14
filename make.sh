#!/bin/bash

latex -src -interaction=nonstopmode main.tex
bibtex main.aux
latex -src -interaction=nonstopmode main.tex
dvips -o main.ps main.dvi
ps2pdf main.ps
rm -r *.log
rm -r *.aux
rm -r *.blg
open main.pdf
