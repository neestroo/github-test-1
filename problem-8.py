# Problem-8: Guessing game
# Write a function that takes a number 1 to 9 from the user input (use input function inside a function).
# Store a number in a variable (let’s assume 6). If the input value is less than the variable,
# print (your guess is almost there), if the input value is greater than the variable,
# print - your guess is higher, if the input value and variable are equals, print - Your Guess Is Correct!


def guessingGame():
    storeNumber = 5
    guessingNumber = int(input("Guess the number between 1 to 9 : "))
    if guessingNumber in range(1, 10):
        if guessingNumber == storeNumber:
            print("Your Guess Is Correct!")

        elif guessingNumber > storeNumber:
            print("your guess is higher")
        else:
            print("your guess is almost there")

    else:
        print("Wrong input number")


guessingGame()
