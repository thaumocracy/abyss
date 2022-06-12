import PyPDF2

with open('dummy.pdf', 'rb') as file:

    page.rotateClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
