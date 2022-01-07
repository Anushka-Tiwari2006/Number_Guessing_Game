import random

number = random.randint(0,9)
chances = 0
print("🔢🧠 NUMBER GUESSING GAME ⁉🧩🧩")
print("There are some rules you have to follow :-")
print("🧩🧩 1- You have only 5 chances to guess the number🧩🧩")
print("🧩🧩 2- You have to guess number according to the given instructions🧩🧩")
name = input("Enter your name: ")
print("Guess a number between 1 to 9" ,name,"😎")

while chances < 5:
    guess = int(input( "Enter your guess : " ))
    
    if guess == number:
        print("Congratulations!! You Won", name,"😎")
        break

    elif guess < number:
        print("Your guess is too low, Guess a number greater than",guess , name,"😎")

    else:
        print("Your guess is too high, Guess a number lesser than",guess , name,"😎")

    chances = chances + 1

    if not chances < 5:
        print("You lose, the number is ",number , name,"😎" , "but it's OK, try again 🤗🤗")   
                