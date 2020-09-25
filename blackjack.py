from random import randint
def startgame():
    while True:
        print("Do you want to play blackjack? Enter Yes or No: ")
        start = input()
        if start.lower().startswith("y"):
            print("Let the game begin")
            return True
        elif start.lower().startswith("n"):
            print("Goodbye")
            return False
        else:
            print("Looks like you did not enter a valid answer!")
def rollagain():
    while True:
        print("Do you want to roll again?")
        start = input()
        if start.lower().startswith("y"):
            print("Best of luck!")
            return True
        elif start.lower().startswith("n"):
            print("Alright, the dealer will roll.")
            return False
        else:
            print("Looks like you did not enter a valid answer!")

while True:
    track=[]
    if not startgame():
        break
    else:
        while sum(track) < 16:
            a = randint(1,6)
            track.append(a)
        print("We automatically rolled untill 16, your rolls where:")
        x=1
        for i in range(len(track)):
            print("Dice "+ str(i+1) + ": " + str(track[i]), end=" ")
        while True:
            if sum(track) == 21:
                print("CONGRATULATIONS YOU ROLLED 21!!!!!")
                break
            elif sum(track) < 21:
                print("for a total sum of " + str(sum(track)) + ".")
                if not rollagain():
                    dealer=[]
                    while sum(dealer) < 16:
                        a = randint(1,6)
                        dealer.append(a)
                    for i in range(len(dealer)):
                        print("Dice " + str(i+1) + ": " + str(dealer[i]), end=" ")
                    print("")
                    if sum(dealer) > sum(track):
                        print("Sorry dealers sum of " + str(sum(dealer)) +
                        " is greater than your sum of " + str(sum(track)))
                        break
                    elif sum(dealer) == sum(track):
                        print("Sorry dealers sum of " + str(sum(dealer)) +
                        " is equal to your sum of " + str(sum(track)) +
                        " the house wins." )
                        break
                    else:
                        while sum(dealer) < sum(track) and sum(dealer) < 22:
                            print("Dealers sum of " + str(sum(dealer)) +
                            " is lower than your sum of " + str(sum(track)) +
                            ", dealer will roll again.")
                            a = randint(1,6)
                            dealer.append(a)
                            print("Dealer rolled " + str(a) + ".")
                            if sum(dealer) > 21:
                                print("CONGRAULATIONS!!!! Dealer busted, you win!!!!")
                                break
                                continue
                            elif sum(dealer) > sum(track):
                                print("Dealer wins with a sum of " + str(sum(dealer)) +
                                " against your sum of " + str(sum(track)))
                                break
                else:
                    a = randint(1,6)
                    track.append(a)
                    print("You rolled " + str(a) + ". Your new sum is " +
                    str(sum(track)))
            else:
                print("Sorry you rolled above 21 and lost the game.")
                break
        break
