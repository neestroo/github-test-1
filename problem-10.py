# Problem-10: The list below is the collection of the ages of people from a village.
# Clean up the data and store only numbers in another list.
# data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
# data_list = [13, 24, "Karim", {"name": "guru"}, 45, 17, 25, 24, 36, 85, 85, 23.36]
# cleanList=[]

# for data in data_list:
#     if type(data) == int:
#         cleanList.append(data)
#     else:
#         None


# print(cleanList)


def clean_List_Data():
    # data_list = [13, 24, "Karim", {"name": "guru"}, 45, 17, 25, 23.36]
    refined_list = []
    for data in data_list:
        if type(data) == int:
            refined_list.append(data)
            
        # elif type(data)== float:
        #     refined_list.append(data)
            # print(refined_list)
        else:
            None
    print(refined_list)


clean_List_Data()
# print(clean_List_Data())


# data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

# # Solution: Filter out only numeric values
# cleaned_list = [x for x in data_list if isinstance(x, (int, float))]

# print("Original list:", data_list)
# print("Cleaned list (only numbers):", cleaned_list)
