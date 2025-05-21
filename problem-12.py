# Problem-12: Find the common items between the lists and make SUM of the new
# list items which are common between the lists.


list1 = [3, 5, 7, 4, 8, 8]

# list1 = [3, 5, 7, 4, 8, 8, 7, 4, 3, 2, 7, 8, 9, 0, 7]

list2 = [4, 9, 8, 7, 1, 1, 13]

common_items = set(list1) & set(list2)
sum_Of_Common_list = sum(common_items)
print("Common items between the lists : ", common_items)
print("Sum of the common items between the lists : ", sum_Of_Common_list)
 