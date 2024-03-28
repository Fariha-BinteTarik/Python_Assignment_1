def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"


width = input("Enter the width: ")
height = input("Enter the height: ")
result = isLandscape(width, height)
print("Image is:", result)
