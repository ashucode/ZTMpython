def func(marks):
	marks=list(set(marks))
	marks.remove(max(marks))
	return(max(marks))

print(func([5,2,3,6,6,5]))