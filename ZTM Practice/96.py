def func(s):
	l=[]
	for i in range(97,97+s):
		l.append(chr(i))
		"""if i!=96+s:
			l.append('-')"""
	res=[]
	#print(l)

	i=0
	for i in range(1,s+1):
		a=""
		for j in range(0,i):
			a=a+l[j]
			if j!=i-1:
				a+="-"
		if len(a)<s*2-1:
			a+=((s*2-1)-len(a))*"-"
		res.append(a) 
	res2=[]

	for i in range(0,len(res)):
		sample=res[i]
		sample=sample[::-1]
		if i!=len(res)-1:
			res2.append(sample[:-1]+res[i])
		print(sample[:-1]+res[i])
	for i in range(len(res2)-1,-1,-1):
		print(res2[i])


func(4)