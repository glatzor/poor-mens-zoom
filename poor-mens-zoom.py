#!/usr/bin/env python3
"""
# Copyright (C) 2020 Sebastian Heinlein <devel@glatzor.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

__author__ = "Sebastian Heinlein <devel@glatzor.de>"

import math
import os.path
from optparse import OptionParser
from PyPDF2 import PdfFileWriter, PdfFileReader

def _poor_mens_zoom(src, options):
    if not options.dest:
        dst = "%s_zoomed%s" % (os.path.splitext(src))
    else:
        dst = options.dest
    print("Converting %s to %s" % (src, dst))

    input = PdfFileReader(src)
    output = PdfFileWriter()

    progress = 0
    total = input.getNumPages()

    for page in input.pages:
        progress += 1
        print("Splitting page %s of %s" % (progress, total))
        height = math.floor(page.mediaBox.getHeight())
        width = math.floor(page.mediaBox.getWidth())

        ratio = height / width * (1 - 0.01 * options.overlap)
        offset = (height * ratio - width) * -1

        page_top = output.addBlankPage(height, width)
        page_top.mergeScaledTranslatedPage(page, ratio, 0, offset)

        page_bottom = output.addBlankPage(height, width)
        page_bottom.mergeScaledTranslatedPage(page, ratio, 0, 0)

    with open(dst, 'w+b') as file:
        output.write(file)
    print("Done.")

if __name__ == "__main__":
    usage = "usage: %prog [options] PDF_FILE"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--destination", default=None,
            action="store", dest="dest", type="string",
            help="Specify an output file name")
    parser.add_option("-o", "--overlap", default=0,
            action="store", dest="overlap", type="int",
            help="Minimum overlap of the splitted pages in percent. Defaults to 0")
    options, args = parser.parse_args()
    if len(args) != 1:
        parser.error("You have to specify a PDF file to convert")
    _poor_mens_zoom(args[0], options)
