def armstrong(a):
	a=str(a)
	c=len(a)
	a=int(a)
	d=a
	sum=0
	for i in range(c):
		b=a%10
	
		sum=sum+(b**c)
	
		a//=10

	if(sum==d):
		print(d,"\n")
	
no1=int(input())
no2=int(input())
if (no1<no2):
	for i in range(no1,no2):
		armstrong(i)
elif(no1>no2):
	for i in range(no2,no1):
		armstrong(i)
