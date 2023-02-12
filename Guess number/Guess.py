import random 

print("Number guessing game")

while True:

    n=int(input("Enter a number between 1 to 10 : "))

    number=random.randint(1,10)

    print("Entered number : ",n)

    print("Random number : ",number)

    if(n>10):

        print("please enter between range limit ")

        print("--------------")

    elif(n!=number) :

        print("Guessed number is incorrect")

        print("-----------")

    elif(n==number):

            print("Guessed number is correct")
