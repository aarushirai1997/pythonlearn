w=int(input())
sum=0
for i in range(w):
	if ((i%2) != 0):
		sum+=i
print ("The sum of odd numbers in {} numbers is {}".format(w,sum))

