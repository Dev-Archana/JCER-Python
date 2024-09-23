#Swapping of two number without using 3rd variable 
a=int(input("Enter A Number\n"))
b=int(input("Enter A Number\n"))
print("Before swapping")
print("Value of A:",a)
print("Value of B:",b)
a=a+b
b=a-b
a=a-b
print("After swapping")
print("Value of A:",a)
print("Value of B:",b)
