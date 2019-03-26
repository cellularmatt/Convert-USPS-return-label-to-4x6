from PyPDF2 import PdfFileWriter, PdfFileReader

# Reads the SSS buyorder customer return labels
# and crops the USPS generated postage label to fit inside
# a 4x6" label for printing.
#
# Scripted by  Mathew Mendoza
# Last edited 06/08/2018

with open("combinednow.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()

    for i in range(numPages):
        page = input1.getPage(i)
        page.cropBox.upperLeft = (0 , 552)
        page.cropBox.upperRight = (500 , 553)
        page.cropBox.lowerLeft = (0 , 0)
        page.cropBox.lowerRight = (432 , 893)
        output.addPage(page)

    with open("buy-order-return-labels.pdf", "wb") as out_f:
        output.write(out_f)
