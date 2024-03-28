def find_elder_brother_age(age1, age2):
    if age1 > age2:
        return "The first brother is elder."
    elif age1 < age2:
        return "The second brother is elder."
    else:
        return "Both brothers are of the same age."


age_of_brother1 = input("Enter age of brother 1: ")
age_of_brother2 = input("Enter age of brother 2: ")
result = find_elder_brother_age(age_of_brother1, age_of_brother2)
print(result)
