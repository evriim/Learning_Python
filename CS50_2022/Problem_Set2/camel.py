#Retrieving data from the user.
camelCase = input("camelCase: ").strip

#Returning data from camelCase to snake form
for i in camelCase:
    if i == i.upper():
        camelCase=camelCase.replace(i,"_"+i)
    else:
        continue
print("Snake form: " + camelCase)
