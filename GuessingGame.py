import random
number=random.randint(0,9)
chances=1

print(number)

while chances < 5:
    source=input("Guess")
    
    if guess == number:
        print("Congratulation YOU WON")

    if not chances <5:
        print("You Lose!!! The number is", number)
