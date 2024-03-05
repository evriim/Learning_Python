amountDue = 50

while True:
    if amountDue == 0:
        print("Change Owed: 0")
        break
    
    print(f"Amount Due: {amountDue} " )
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5: 
        amountDue = amountDue - coin
    else:
        coin = int(input("Insert Coin: "))
    
