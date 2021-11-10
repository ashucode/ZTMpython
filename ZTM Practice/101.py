def func(a):
	dicta={}
	a=a.replace(" ","")
	for i in a:
		if i not in dicta:
			dicta[i]=1
		else:
			dicta[i]+=1
	l=[]

	for i in dicta:
		l.append(dicta[i])
	l=list(set(l))
	l.sort(reverse=True)
	for i in l:
		for j in dicta:
			if dicta[j]==i:
				print(j,dicta[j])

func('ashutosh roy')
