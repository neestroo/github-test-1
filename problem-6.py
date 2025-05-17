# Problem-6: Write a function named "isLandscape" that takes 2 numbers (image width and height) as arguments
# and the function returns Landscape if the image width has a higher value than height. Returns Portrait otherwise


def isLandscape(image_width, height):
    if image_width > height:
        print("landscape")
    elif height > image_width:
        print("Portrait")
    else:
        print("Input size are same")

isLandscape(image_width=int(input("image width : ")), height=int(input("image height : ")))


# def isLandscape(image_width, height):
#     if image_width > height:
#         return "Landscape"
#     else:
#         return "Portrait"

# # Test the function
# image_width = int(input("image width : "))
# height = int(input("image height : "))
# result = isLandscape(image_width, height)
# print(result)