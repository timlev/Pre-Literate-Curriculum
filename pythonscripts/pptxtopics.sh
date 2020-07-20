#!/bin/bash
for file in "ls ./*.pptx"
do
	libreoffice --headless --convert-to pdf ${file}
done

for f in *.pdf
do
	convert -density 400 "${f}" "${f%.*}%d.png"
done
