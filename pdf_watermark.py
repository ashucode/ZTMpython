import PyPDF2,sys


def apply_watermark(target,watermark):
	output=PyPDF2.PdfFileWriter()
	tar=PyPDF2.PdfFileReader(target)
	water=PyPDF2.PdfFileReader('./sample pdf/'+watermark)
	for i in range(0,tar.getNumPages()):
		sheet=tar.getPage(i)
		sheet.mergePage(water.getPage(0))
		output.addPage(sheet)
	with open('comwater.pdf','wb') as final:
		output.write(final)

apply_watermark(sys.argv[1],sys.argv[2])
