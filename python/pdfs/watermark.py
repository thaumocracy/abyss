import PyPDF2
import sys

input = sys.argv[1]


def wm(item):
    with open(f'{item}', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        with open('wtr.pdf', 'rb') as wtr:
            water = PyPDF2.PdfFileReader(wtr)
            waterPage = water.getPage(0)
            page.mergePage(waterPage)
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(page)
            with open('output.pdf', 'wb') as marked_output:
                writer.write(marked_output)


wm(input)
