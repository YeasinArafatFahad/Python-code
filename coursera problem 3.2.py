hours = input("Enter Hours:")
h = float(hours)
Rate = input("Enter the Rate:")
x = float(Rate)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
