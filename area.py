w=str(input())
if (w=="rectangle"):
	l=int(input())
	b=int(input())
	area=l*b
elif (w=="square"):
	a=int(input())
	area=a**2
elif (w=="triangle"):
	b=int(input())
	h=int(input())
	area=0.5*b*h
else:
	print("Invalid input")
	exit()
	
print("The area of the {} is {}".format(w,area))