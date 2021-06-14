import sys , os
from PIL import Image, ImageFilter

target='F:/images with py/'+sys.argv[1]
path='F:/images with py/'+sys.argv[2]
if not os.path.isdir(path):
	os.mkdir(path)
for name in os.listdir(target):
	temp=target+name
	img=Image.open(temp)
	if (img.format=='JPEG') or (img.format=='PNG'):
		temp=path+name.split('.')[0]+'.png'
		img.save(temp,'png')