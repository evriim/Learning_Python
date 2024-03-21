"""Writing sentences following comma rules with Inflect"""
import inflect
p = inflect.engine()
name = []
try:
    while True:
        new_name = input("Name: ")
        name.append(new_name)
except EOFError:
    pass

output = p.join(name)
print("Adieu, adieu, to " + output)
