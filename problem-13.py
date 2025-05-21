# Problem-13: Compare the two dictionaries and find the common items based on KEYs of the dictionaries


dict1 = {"age": 13, "id": 12, "address": "Banani", "course": "Python"}

dict2 = {"address": "Rupnagar", "id": 25, "course": "MERN"}

common_Dictionaries_keys = set(dict1.keys()) & set(dict2.keys())


print("Common key between two  dictionaries : ", common_Dictionaries_keys)









# common_Dictionary_Items = {}

# for key in common_Dictionaries_keys:
#     if dict1[key] == dict2[key]:
#         common_Dictionary_Items[key] = dict1[key]
#     print(common_Dictionary_Items)

# print("Common key-value pair (same in both dictionaris) : ", common_Dictionary_Items)


# common_Dictionary_Items = {}

# for key in common_Dictionaries_keys:
#     common_Dictionary_Items[key] = (dict1[key], dict2[key])


# print("Common keys:", common_Dictionaries_keys)
# print("\nCommon items with their values from both dictionaries:")

# for key, (value1, value2) in common_Dictionary_Items.items():
#     print(f"{key}: {value1} (dict1) and {value2} (dict2)")











# Given dictionaries
# dict1 = {"age": 13, "id": 12, "address": "Banani", "course": "Python"}
# dict2 = {"address": "Rupnagar", "id": 25, "course": "MERN"}

# # Step 1: Find common keys
# common_keys = set(dict1.keys()) & set(dict2.keys())

# # Step 2: Compare values for the common keys
# common_key_values = {}

# for key in common_keys:
#     if dict1[key] == dict2[key]:
#         common_key_values[key] = dict1[key]

# # Output results
# print("Common keys:", list(common_keys))
# print("Common key-value pairs (same in both dicts):", common_key_values)

