# Problem-9: Find if 6 is available in the list

# my_list = [4, 8, 7, 4,3,6,2,1,9]


def findNumberinList():
    my_list = [4, 8, 7, 4, 3, 6, 2, 1, 9]
    checkNumber = int(input("Enter a number to check in the list : "))
    print("List's numbers are : ",my_list)
    if checkNumber in my_list:
        print(checkNumber, "is in the list")
    else:
        print(checkNumber, "not in the list")


findNumberinList()
