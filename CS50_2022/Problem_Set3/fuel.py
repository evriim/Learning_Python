def main():
    i=fuel()
    percent = i*100
    percent = round(percent)
    if percent == 100:
        print("Fuel: F")
    elif percent == 0:
        print("Fuel: E")
    else:
        print(f"Fuel: %{percent}")

#Retrieving fuel data from the user. Keeping data as two different integers.
def fuel():
    while True:
        try:
            fraction= input("Fraction: ")
            x,y= fraction.split("/")
            x = int (x)
            y = int (y)
            fuel_box = x/y
            if fuel_box <= 1:
                return fuel_box  
            
#Repeat in case of division by 0 and incorrect data entry
        except (ValueError,ZeroDivisionError):
            pass



main()