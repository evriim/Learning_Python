#Retrieving data from the user.
greeting = input("Greeting: ").lower().strip()


#Determine the situations how much it will take based on the answer
if "hello" in greeting:
    print("$0")
elif "h" == greeting[0]:
    print("$20")
else:
    print("$100")
    
