import random
playerIn = True
dealerIn = True
print("\nHello and welcome to matzz's casino!!\n")
depozit = input("How much money do you want to turn into chips?\n")

print(depozit + "$ Were transfered to your account.Thank you.\n")
tavolina = input("\nPress 1 if you want to play blackjack!!\n")
if tavolina == "1":
    bet = input("How much do you want to bet?\n")
    
    print("\nThe game is starting your bet is:" + bet + "$")
else:
    print("Goodbye hope to see you again.")
    exit()
    
win = int(bet) + int(depozit)
loose = int(depozit) - int(bet)


#Letrat,Lojtari dhe Dealer
letrat = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
"J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", ]
doralojtarit = []
doradealerit = []

#mi qkep letrat
def dealCard(turn):
    card = random.choice(letrat)
    turn.append(card)
    letrat.remove(card)

#kalkulim i kartave

def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10 
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total 

#me gjet fitusin

def revealDealerHand():
    if len(doradealerit) == 2:
        return doradealerit[0]
    elif len(doradealerit) > 2:
        return doradealerit[0], doradealerit[1]

#loop per loj  

for _ in range(2):
    dealCard(doradealerit)
    dealCard(doralojtarit)
while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and ??")
    print(f"You have {doralojtarit} wich is {total(doralojtarit)}")
    if playerIn:
        stayORhit = input("1: Stay\n2: Hit\n")
    if total(doradealerit) > 16:
        dealerIn = False
    else:
        dealCard(doradealerit)
    if stayORhit == "1" or stayORhit == "stay" or stayORhit == "Stay":
        playerIn = False
    else:
        dealCard(doralojtarit)
    if total(doralojtarit) >= 21:
        break
    elif total(doradealerit) >=21:
        break

if total(doralojtarit) == 21:
    print(f"\nYou have {doralojtarit} for a total of 21 and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("Blackjack!!You win!!")
    print(f"You have : {win}$ in your account")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")
    
elif total(doradealerit) == 21:
    print(f"\nYou have {doralojtarit} for a total of {total(doralojtarit)} and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("Blackjack!!Dealer wins!!")
    print(f"You have: {loose}$ in your account")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")
    
    

elif total(doralojtarit) > 21:
    print(f"\nYou have {doralojtarit} for a total of {total(doralojtarit)} and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("You loose!!Dealer wins!!")
    print(f"You have: {loose}$ in your account")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")
    

elif total(doradealerit) > 21:
    print(f"\nYou have {doralojtarit} for a total of {total(doralojtarit)} and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("You won!!Dealer lost!!")
    print(f"You have: {win}$ in your account")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")
    
elif 21 - total(doradealerit) < 21 - total(doralojtarit):
    print(f"\nYou have {doralojtarit} for a total of {total(doralojtarit)} and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("Dealer wins!!")
    print(f"You have: {loose}$ in your account")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")

elif 21 - total(doradealerit) > 21 - total(doralojtarit):
    print(f"\nYou have {doralojtarit} for a total of {total(doralojtarit)} and the dealer has {doradealerit} for a total of {total(doradealerit)}")
    print("You won!!")
    input(f"Llogaria jote eshte: {win}")
    vazhdo = input("Press 1 to play again\nPress 2 to stop\n")