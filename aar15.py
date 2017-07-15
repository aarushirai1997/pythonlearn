a=int(input("enter the no\n"))
b=int(input("enter second no.\n"))
if (a<b):
	for i in range(a,b):
		if(i%2==0):
			print(i," ")
elif(b<a):
	for i in range(b,a):
		if(i%2==0):
			print(i," ")
