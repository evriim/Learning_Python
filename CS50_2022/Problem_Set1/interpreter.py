#Retrieving data from the user.
x,y,z= (input("Expressions: ")).split(" ")

#Converting str format to int
x = int(x)
z = int(z)


#Figuring out what action to take
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    print(x/z)
else:
    print("Unknown format.")
