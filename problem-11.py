# Problem-11: Find the most frequent character in the paragraph
# rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
# for charecterOfStr in rhyme:

# rhyme = "Twinkle, twinkle, little star. How I wonder what you are!"

# # Step 1: Convert to lowercase to count characters fairly
# rhyme = rhyme.lower()

# # Step 2: Create a dictionary to count characters
# char_count = {}

# for char in rhyme:
#     if char.isalpha():  # Count only letters (ignore spaces, punctuation)
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1

# # Step 3: Find the most frequent character
# most_frequent = max(char_count, key=char_count.get)
# frequency = char_count[most_frequent]

# print(f"The most frequent character is '{most_frequent}' with {frequency} occurrences.")




# Problem-11: Find the most frequent character in the paragraph
# rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
# rhyme=rhyme.lower()

# # Create a dictionary to store character counts
# char_count = {}

# # Count occurrences of each character
# for char in rhyme:
#     # Skip spaces and punctuation if you want to count only letters
#     if char.isalpha():
#         char_count[char] = char_count.get(char, 0) + 1

# # Find the character with maximum count
# most_frequent_char = max(char_count.items(), key=lambda x: x[1])

# print(f"The most frequent character is '{most_frequent_char[0]}' appearing {most_frequent_char[1]} times.")


from collections import Counter

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# Convert to lowercase and filter only letters
filtered = [char for char in rhyme.lower() if char.isalpha()]

# Count characters
char_count = Counter(filtered)

# Find the most common character
most_common = char_count.most_common(1)[0]

print(f"The most frequent character is '{most_common[0]}' with {most_common[1]} occurrences.")
# print("The most frequent character is '" + most_common[0] + "' with " + str(most_common[1]) + " occurrences.")


from collections import 

