def func(s,n):
	p=[]
	i=0
	while(i<len(s)):
		p.append(s[i:i+n])
		i=i+n
	for i in p:
		print(i)
func('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4)
