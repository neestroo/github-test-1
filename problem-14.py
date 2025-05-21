# Problem-14: Sort the list in DESCENDING order and find the subtraction of maximum and minimum numbers.

list_1 = [4, 9, 8, 7, 5, 2, 13]
# print(list_1)
# sortListAccending=sorted(list_1)
# print(sortListAccending)
print("List before sorting : ", list_1)
sortListDecending = sorted(list_1, reverse=True)
print("List after sorting in descending order : ", sortListDecending)

maxNumber = max(list_1)
minNumber = min(list_1)

print("Maximum number in the list : ", maxNumber)
print("Minimum number in the list : ", minNumber)

subtract = maxNumber - minNumber
print("Subtraction of maximum and minimum numbers : ", subtract)
