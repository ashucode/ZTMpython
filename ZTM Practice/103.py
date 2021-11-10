def func(n):
	if n==0:
		return n 
	else:
		return (func(n-1))+n

print(func(5))

