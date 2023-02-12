import random
print("Dice Rolling\n")
print("Enter 1 to start and 0 to end the game")
while True:
    n=int(input("Enter : "))
    if(n==1):
        number=random.randint(1,6)
        print("Die landed is ",number)
        print("---------------")
    elif(n==0):
        print("Game ended")
        break
    else:
        print("Enter valid number")
