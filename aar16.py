def prime(a):
	for i in range(2,a):
		if(a%i==0):
			
			break
	else: print(a)
	
a=int(input())
b=int(input())
if(a<b):
	for j in range(a,b):
		prime(j)
elif (a>b):
	for j in range(b,a):
		prime(j)
