# Problem-3: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder

# brother1 = float(input("Enter brother one age : "))
# brother2 = float(input("Enter brother two age : "))

# def ageChecking():

#     if brother1 > brother2:
#         print("Brother 1 is elder and age is : ", brother1)
#     elif brother1 < brother2:
#         print("Brother 2 is elder and age is : ", brother2)
#     else:
#         print(("Brother 2 is elder and age is : ", brother2))


# ageChecking()


def ageChecking(brother1_age, brother2_age):
    if brother1_age > brother2_age:
        print("Brother 1 is elder and age is:", brother1_age)
    elif brother1_age < brother2_age:
        print("Brother 2 is elder and age is:", brother2_age)
    else:
        print("Both brothers are of the same age:", brother1_age)


ageChecking(86, 86)
