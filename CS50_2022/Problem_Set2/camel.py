camelCase = input("camelCase: ").strip
for i in camelCase:
    if i == i.upper():
        camelCase=camelCase.replace(i,"_"+i)
    else:
        continue
print("Snake form: " + camelCase)