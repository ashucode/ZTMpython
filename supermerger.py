import PyPDF2, sys,os

path=' '.join(sys.argv[1:])

def pdf_merger(pdf_list):
	merger=PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		a=path+pdf
		merger.append(a)
	merger.write(path+'supermerge.pdf')

a=(os.listdir(path))
b=[]
for i in a:
	if i.lower().endswith('pdf'):
		b.append(i)
pdf_merger(b)