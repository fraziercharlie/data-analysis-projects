food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(',')
food_list.sort()

equipment_list = equipment.split(',')
equipment_list.sort()

pets_list = pets.split(',')
pets_list.sort()

sleep_aids_list = sleep_aids.split(',')
sleep_aids_list.sort()

print("Sorted Food Items:", food_list)
print("Sorted Equipment Items:", equipment_list)
print("Sorted Pets Items:", pets_list)
print("Sorted Sleep Aids Items:", sleep_aids_list)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = []

cargo_hold.append(food_list)
cargo_hold.append(equipment_list)
cargo_hold.append(pets_list)
cargo_hold.append(sleep_aids_list)

print("Cargo Hold Contents:")
for index, cabinet in enumerate(cargo_hold):
    print(f"Cabinet {index}: {cabinet}")



# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
# Function to prompt user and validate selection
def select_cabinet(cargo_hold):
    while True:  
        user_input = input("Select a cabinet number (0-3) to view its contents: ")
        try:
            cabinet_index = int(user_input)  
            if 0 <= cabinet_index = 3:  
                
                print(f"Contents of Cabinet {cabinet_index}: {cargo_hold[cabinet_index]}")
                break  
            else:
                                print("Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
                        print("Invalid input. Please enter a valid integer.")

select_cabinet(cargo_hold)



# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
def display_cabinet_contents(cargo_hold):
    try:
        
        cabinet_index = int(input("Select a cabinet number (0-3) to view its contents: "))
        
        
        if 0 <= cabinet_index < len(cargo_hold):
            
            print(f"Contents of Cabinet {cabinet_index}: {cargo_hold[cabinet_index]}")
        else:
            
            print(f"Invalid cabinet number. Please select a number between 0 and {len(cargo_hold) - 1}.")
    except ValueError:
        
        print("Invalid input. Please enter a valid integer number.")


display_cabinet_contents(cargo_hold)



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
# def check_cabinet_item(cargo_hold):
#     try:
        
#         cabinet_index = int(input("Select a cabinet number (0-3) to view its contents: "))
        
        
#         if 0 <= cabinet_index < len(cargo_hold):
            
#             item = input("Enter the item you are looking for: ").strip()
            
            
#             if item in cargo_hold[cabinet_index]:
#                 print(f"Cabinet {cabinet_index} DOES contain {item}.")
#             else:
#                 print(f"Cabinet {cabinet_index} DOES NOT contain {item}.")
#         else:
#             print(f"Invalid cabinet number. Please select a number between 0 and {len(cargo_hold) - 1}.")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer number.")


# check_cabinet_item(cargo_hold)
