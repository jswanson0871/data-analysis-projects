food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(',')
food_list.sort()
print("food cabinet:",food_list)
equipment_list = equipment.split(',')
equipment_list.sort()
print("equipment cabinet:",equipment_list)
pets_list = pets.split(',')
pets_list.sort()
print("pets cabinet:",pets_list)
sleep_aids_list = sleep_aids.split(',')
sleep_aids_list.sort()
print("pets cabinet:",sleep_aids_list)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]
print("cargo hold list:",cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_index = int(input("Select a cabinet (0-3): "))
print("You selected cabinet", cabinet_index, ":", cargo_hold[cabinet_index])


# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
cabinet_index = int(input("select a cabinet from 0-3"))
if 0 <= cabinet_index <=3:
    selected_cabinet = cargo_hold[cabinet_index]
    print(f"You slected cabint {cabinet_index}:{selected_cabinet}")
else:
    print("Error: Please selected a number 0-3.")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
cabinet_index = int(input("Select a cabinet (0-3): "))
item = input("Enter an item to search for: ").lower()
if item in cargo_hold[cabinet_index]:
    print("Cabinet {} DOES contain {}.".format(cabinet_index, item))
else:
    print("Cabinet {} DOES NOT contain {}.".format(cabinet_index, item))