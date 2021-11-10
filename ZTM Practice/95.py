def func(a,b):
	res=""
	c=0
	for i in a:
		res+=i
		c+=1
		if c==b:
			c=0
			res+=" "

	if res[-1]==" ":
		res=res[:-1]
	return res

a=input()
b=int(input())
print(func(a,b))


