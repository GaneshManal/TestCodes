import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pyPdf import PdfFileReader, PdfFileWriter
from matplotlib.backends.backend_pdf import PdfPages

# Read a PDF  Document
pdfOne = PdfFileReader(file( os.getcwd() + os.path.sep + 'pdfOne.pdf', "rb"))

# Read the pdf and write to output.pdf
output = PdfFileWriter()
for page_pdf1 in xrange(pdfOne.getNumPages()):
    page_content =  pdfOne.getPage(page_pdf1)

    print type(page_content), dir(page_content)
    print '-' * 100
    # print 'Text :', page_content.getContents()
    output.addPage(pdfOne.getPage(page_pdf1))

outputStream = file(os.getcwd() + os.path.sep + "output.pdf", "wb")
output.write(outputStream)
outputStream.close()
