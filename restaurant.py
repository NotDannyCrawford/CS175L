#CS175
#Danny Crawford
#restaurant


vegetarian = False
vegan = False
gluten_free = False
search = True


while search == True:
    response1 = input("\nIs anyone in your party a vegetarian? (yes/no) ").lower()
    while response1 != "yes" and response1 != "no":
        response1 = input("Please type 'Yes' or 'No': ").lower()
    if response1 == "yes":
        vegetarian = True
    response2 = input("Is anyone in your party a vegan? (yes/no) ").lower()
    while response2 != "yes" and response2 != "no":
        response2 = input("Please type 'Yes' or 'No': ").lower()
    if response2 == "yes":
        vegan = True
    response3 = input("Is anyone in your party a gluten-free? (yes/no) ").lower()
    while response3 != "yes" and response3 != "no":
        response3 = input("Please type 'Yes' or 'No': ").lower()
    if response3 == "yes":
        gluten_free = True

    print("\nHere are your restaurant choices.")
    if vegetarian == False and vegan == False and gluten_free == False:
        print("Joe's Gourmet Burgers")
    if vegan == False and gluten_free == False:
        print("Mama's Fine Italian")
    if vegan == False:
        print("Main Street Pizza")
    print("Corner Cafe\nChef's Kitchen")

    response4 = input("\nEnter 'yes' if you would like to do another restaurant search (enter 'no' to end): ").lower()
    while response4 != "yes" and response4 != "no":
        response4 = input("Please type 'Yes' or 'No': ").lower()
    if response4 == "no":
        search = False
