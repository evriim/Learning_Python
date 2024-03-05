#Retrieving data from the user
text = input("Input: ")
vowels = {"A","a","E","e","I","i","O","o","U","u"}

#Checking the individual indexes of the data for vowels.
#Remove vowels and create new data
for _ in text:
    for i in vowels:
        if _ == i :
            text= text.replace(_,"")
        else:
            continue

print(text)