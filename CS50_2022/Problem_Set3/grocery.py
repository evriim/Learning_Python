grocery = {}

while True:
#If there is more than one piece of data, it adds it to the count.
    try:
        item =input().lower()
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item]=1

#When Control - D is pressed, it organizes all data and outputs        
    except EOFError:
        for i in sorted(grocery.keys()):
            print(grocery[i], i.upper())
        break