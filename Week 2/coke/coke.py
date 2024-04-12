def main():

    print("Amount Due: 50")
    valid_coins = [5, 10, 25]
    balance = 0
    while True:
        addition = int(input("Insert Coin: "))
        if addition in valid_coins:
            balance += addition
        if balance < 50:
            print("Amount Due:", 50 - balance)
        else:
            print("Change Owed:", balance - 50)
            break

main()
