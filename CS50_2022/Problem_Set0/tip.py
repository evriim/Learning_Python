#Remove the $ and convert it to a float
def dollars_to_float(d):
    d= d.replace("$","")
    return float(d)

#Remove the %, calculating percent and convert it to a float
def percent_to_float(p):
    p = float(p.replace("%",""))
    p=p/100
    return float(p)

#Take input / Calculating tip / Output
def main():
    dollars= dollars_to_float(input("How much was the meal? ").format())
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()