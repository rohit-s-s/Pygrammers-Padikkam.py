import random
print("Welcome to the simple dice roller program.\n")

while True:
    n=int(input("Enter 1 to start rolling the dice or 0 to end: "))
    if(n==1):
        number=random.randint(1,6)
        print("The dice landed on: ",number)
        print("---------------")
    elif(n==0):
        print("Thanks for playing!")
        break
    else:
        print("Enter valid number")
