"""
ISO 8601, an international standard that prescribes that dates 
should be formatted in year-month-day (YYYY-MM-DD) order.
"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#Infinite loop
while True:
    date = input("Date: ")
    try:
        #For the date written in "/" format
        month, day, year = date.split("/")
        if int(day) >= 1 and int(day)<=31 and int(month) >=1 and int(month)<=12:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
    except:
        try:
            #Situations where the month is written in script
            month, day, year, = date.split(" ")
            day=day.replace(",","")
            for i in range(len(months)):
                if month == months[i]:
                    month = i+1
            if int(day) >= 1 and int(day)<=31 and int(month) >=1 and int(month)<=12:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
        except:
            pass
