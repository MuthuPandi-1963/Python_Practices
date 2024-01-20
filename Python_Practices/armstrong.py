number = int(input("enter a number :")) #user input
armstrong=sum(int(digit)**3 # armstrong calculation
for digit in str(number))

if number == armstrong:
   print(number,"is armstrong")
else:
   print( number,"is not armstrong")