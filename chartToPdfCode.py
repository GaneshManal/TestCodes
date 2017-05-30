import os
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pyPdf import PdfFileReader, PdfFileWriter
from matplotlib.backends.backend_pdf import PdfPages

# Target pdf
output = PdfFileWriter()

# Existing PDF
pdfOne = PdfFileReader(file( os.getcwd() + os.path.sep + 'pdfOne.pdf', "rb"))

x1 = np.arange(100)
y1 = x1**2
# print 'X1 :', x1
# print 'Y1 :', y1

pp = PdfPages('temp.pdf')


def function_plot(x,y):
    ######### Wave graph ##########
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    t = np.arange(0.01, 10.0, 0.01)
    s1 = np.exp(t)
    ax1.plot(t, s1, 'b-')
    ax1.set_xlabel('time (s)')
    # Make the y-axis label and tick labels match the line color.
    ax1.set_ylabel('exp', color='b')
    for tl in ax1.get_yticklabels():
        tl.set_color('b')

    ax2 = ax1.twinx()
    s2 = np.sin(2 * np.pi * t)
    ax2.plot(t, s2, 'r.')
    ax2.set_ylabel('sin', color='r')
    for tl in ax2.get_yticklabels():
        tl.set_color('r')
    pp.savefig()

    ######### Comparison chart #########
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    menStd = (2, 3, 4, 1, 2)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig = plt.figure()
    ax = fig.add_subplot(111)
    rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)

    womenMeans = (25, 32, 34, 20, 25)
    womenStd = (3, 5, 2, 3, 3)
    rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

    # add some
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    pp.savefig()

    ######### Line Chart #########
    plt.figure()
    plt.clf()
    plt.plot(x,y)
    plt.title('A Sample Chart')
    plt.xlabel('x axis', fontsize = 13)
    plt.ylabel('y axis', fontsize = 13)
    pp.savefig()

    ######### Bar Chart #########
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    l = plt.plot(bins, y, 'r--', linewidth=1)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    pp.savefig()

function_plot(x1,y1)
pp.close()


pdfTwo = PdfFileReader(file(os.getcwd() + os.path.sep + 'temp.pdf', "rb"))

# Read both the pdf and write to output.pdf
page_pdf2 = 0
for page_pdf1 in xrange(pdfOne.getNumPages()):
    output.addPage(pdfOne.getPage(page_pdf1))

    if (page_pdf1 + 1)%4 == 0:
        output.addPage(pdfTwo.getPage(page_pdf2))
        page_pdf2 += 1

outputStream = file(os.getcwd() + os.path.sep + "output.pdf", "wb")
output.write(outputStream)
outputStream.close()
