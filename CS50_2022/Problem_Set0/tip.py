#Remove the $ sign in the data and convert it to float data type
def dollars_to_float(d):
    d= d.replace("$","")
    return float(d)

#Remove the % sign in the data and calculate percentage.
#Converting the found data to float data type.
def percent_to_float(p):
    p = float(p.replace("%",""))
    p=p/100
    return float(p)

#Retrieving data from the user. Calculating tip value.
def main():
    dollars= dollars_to_float(input("How much was the meal? ").format())
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()