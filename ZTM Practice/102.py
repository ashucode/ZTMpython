def func(a):
	digit=0
	alpha=0
	for i in a:
		if i.isdigit():
			digit+=1
		else:
			alpha+=1
	print('digit:',digit,"\n","alphabet:",alpha)

func('Hello321Bye360')