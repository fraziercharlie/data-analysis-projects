# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.
fuel_level = 15000  
num_astronauts = 5  
altitude = 0 

# verify values
print(f"Initial Fuel Level: {fuel_level} kg")
print(f"Number of Astronauts: {num_astronauts}")
print(f"Starting Altitude: {altitude} km")

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 

while True:
    try:
        fuel_level = int(input("Enter the starting fuel level (between 5000 and 30000): "))
        if 5000 < fuel_level < 30000:
            print(f"Valid fuel level entered: {fuel_level} kg")
            break  # Exit the loop if the input is valid
        else:
            print("Fuel level must be between 5000 and 30000. Please re-enter.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
num_astronauts = 0

while True:
    try:
        num_astronauts = int(input("Enter the number of astronauts (1 to 7): "))
        if 1 <= num_astronauts <= 7:
            print(f"Number of astronauts entered: {num_astronauts}")
            break  # Exit the loop if the input is valid
        else:
            print("Number of astronauts must be between 1 and 7. Please re-enter.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")
    
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.
altitude = 0

while fuel_level - 100 * num_astronauts >= 0:
    fuel_level -= 100 * num_astronauts  # Decrease fuel level by 100 units per astronaut
    altitude += 50  # Increase altitude by 50 km per iteration
    
    print(f"Current fuel level: {fuel_level} kg, Current altitude: {altitude} km")
print(f"Final fuel level: {fuel_level} kg, Final altitude: {altitude} km")



# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.

print(f"The shuttle gained an altitude of {altitude} km and has {fuel_level} kg of fuel left.")

# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”
if altitude >= 2000:
    print(f"The shuttle gained an altitude of {altitude} km and has {fuel_level} kg of fuel left. Orbit achieved!")
else:
    print(f"The shuttle gained an altitude of {altitude} km and has {fuel_level} kg of fuel left. Failed to reach orbit.")