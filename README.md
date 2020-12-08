# Poor Men's Zoom

## Introdcution
 
This little tool helps to read scientific PDF papers on the remarkable epaper tablet by
splitting portrait oriented pages into two landscape pages (a top and a bottom one).

Unfortunaltely the remarkable doesn't support zooming to a document by rotating it from
portait to landscape. So this a poor men's zoom.

## Installation

You need a Python3-Intretator and the pyPDF2 library (python3-pypdf2 on Debian/Ubuntu).

## Usage

Just run the scrip in the command line, e.g.

 ./poor-mens-zoom.py my_paper.pdf

This will create a file call my_paper_zoomed.pdf which you can upload to your remarkable.

## Shortcommings

There is currently no way to merge the splitted pages again after reading/note taking.
Links, bookmarks, annotations get lost during splitting.
