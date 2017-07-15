a=int(input("enter the no\n"))
for i in range(2,a):
	if(a%i==0):
		print("composite")
		exit()
print("Prime")