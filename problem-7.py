# Problem-7: Write a function that takes 1 number as argument. The function should
# return “Fizz” if the number is divisible by 3, the function should return “Buzz”
# if the number is divisible by 5, the function should return “FizzBuzz” if the number is divisible by both 5 and 3,
# otherwise return “Not a Fizz-buzz number”

# theCheckingNumber = int(input("Enter a number to check 'Fizz / Buzz or Fizz-buzz': "))


def FizzBuzzChecking(theCheckNumber):
    if theCheckNumber % 3 == 0 and theCheckNumber % 5 == 0:
        return "FizzBuzz"
    elif theCheckNumber % 5 == 0:
        return "Buzz"
    elif theCheckNumber % 3 == 0:
        return "Fizz"
    else:
        return "Not a Fizz-buzz number"


print(FizzBuzzChecking(15))


# def fizzBuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "FizzBuzz"
#     elif number % 3 == 0:
#         return "Fizz"
#     elif number % 5 == 0:
#         return "Buzz"
#     else:
#         return "Not a Fizz-buzz number"

# # Test the function
# number = int(input("Enter a number: "))
# result = fizzBuzz(number)
# print(result)
