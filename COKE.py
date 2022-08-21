amount=50

while(amount>0):
    print("Amount due:",amount)
    coin=int(input("Insert Coin:"))
    if coin in [25,10,5]:
        amount=amount-coin

print("Change owed:", -1*(amount))
