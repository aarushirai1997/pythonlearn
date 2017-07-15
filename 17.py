a=str(input())
c=len(a)
a=int(a)
d=a
sum=0
for i in range(c):
	b=a%10
	
	sum=sum+(b**c)
	
	a//=10

if(sum==d):
	print("Armstrong")
	