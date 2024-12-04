'''
1 = STONE
-1 = PAPER
0 = SCISSORS
'''
import random



computer = random.choice([0, 1, -1])
print("WECOME TP STONE PAPER AND SCISSORS GAME !!!!! \n FOR STONE ---> ST \n FOR PAPER ---> P \n FOR SCISSORS ---> S  ")
userstat = input("YOUR TURN : ")
yourdict = {"ST" : 1 , "P" : -1 , "S" : 0 }
revdict = {1:"ST", -1:"P" , 0 : "S"}

you = yourdict[userstat]
print(f" computer said {revdict[computer]} \n You said {revdict[you]}")

if(computer == you):
    print("ohh its a draw")
else:
    if(computer == 1 and you == -1):
        print("YOU WIN!!! 🏆")
    elif(computer == 1 and you == 0):
        print("YOU LOST  😢")

    elif(computer == -1 and you == 1):
        print("YOU LOST  😢")
    elif(computer == -1 and you == 0):
        print("YOU WIN!!! 🏆")

    elif(computer == 0 and you == 1):
        print("YOU WIN!!! 🏆")
    elif(computer == 0 and you == -1):
        print("YOU LOST  😢")
    else:
        print("WRONG INPUT")



