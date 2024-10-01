ingredient_1 = input("Name an ingredient in a salad: ")
ingredient_2 = input("Name another ingredient in a salad: ")
ingredient_3 = input("Name a final ingredient in a salad: ")

portion_1 = float(input(f"How many ounces of {ingredient_1} should there be? "))
portion_2 = float(input(f"How many ounces of {ingredient_2} should there be? "))
portion_3 = float(input(f"How many ounces of {ingredient_3} should there be? "))

serving = int(input("How many servings do you want to eat? "))
                    
print(f"Total ounces of {ingredient_1}: {portion_1*serving}")
print(f"Total ounces of {ingredient_2}: {portion_2*serving}")
print(f"Total ounces of {ingredient_3}: {portion_3*serving}")
print("Enjoy your salad!")