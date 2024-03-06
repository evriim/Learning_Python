#Price dict
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

bill=0
while True:
    #Making the data received from the user similar to the data in the dictionary
    try:
        i=input("Item: ").title()
        if i in menu:
            bill+=menu[i]
            
        print(f"Total: ${bill}")

#When Control - D is pressed outputs.
    except EOFError:
        break
