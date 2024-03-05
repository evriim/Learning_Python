#Retrieving data from the user and send it into the convert function
def main():
    time = input("What time is it? ")
    convert(time)

#Function that shows which meal time it is according to the clock
def convert(time):
    hours,minutes = time.split(":")
    hours = int(hours)
    if hours >=7 and hours<8:
        print("breakfast time")
    elif hours >=12 and hours<13:
        print("lunch time")
    elif hours >=18 and hours<19:
        print("dinner time")
            

#Call main
if __name__ == "__main__":
    main()