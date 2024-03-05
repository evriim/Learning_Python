amountDue = 50

#Will return until all money is paid
while True:
    if amountDue == 0:
        print("Change Owed: 0")
        break
    
#Loop to check coin thrown
    print(f"Amount Due: {amountDue} " )
    coin = int(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5: 
        amountDue = amountDue - coin
    else:
        coin = int(input("Insert Coin: "))
    
