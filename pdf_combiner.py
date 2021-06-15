import PyPDF2, sys

pdfs=sys.argv[1:]
print(pdfs)

def pdf_combiner(pdf_list):
	combined=PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		a='./sample pdf/'+pdf
		combined.append(a)
	combined.write('combined.pdf')




pdf_combiner(pdfs)
