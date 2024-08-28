# Assign the variables for exercise 1 here:



# BEFORE running the code, predict what will be printed to the console by the following statements:

# 1. Assign variables for the space shuttle
engine_indicator_light = "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200
shuttle_speed = 15000

# Print the values to check the assignments
print("Engine Indicator Light:", engine_indicator_light)
print("Space Suits On:", space_suits_on)
print("Shuttle Cabin Ready:", shuttle_cabin_ready)
print("Crew Status:", crew_status)
print("Computer Status Code:", computer_status_code)
print("Shuttle Speed:", shuttle_speed)

# 2. Examine the code below. What will be printed to the console?
# if engine_indicator_light == "green": 
#    print("engines have started")
# elif engine_indicator_light == "green blinking": 
#    print("engines are preparing to start")
# else:
#    print("engines are off")

#    if crew_status:
#    print("Crew Ready")
# else:
#    print("Crew Not Ready")

# if computer_status_code == 200:
#    print("Please stand by. Computer is rebooting.")
# elif computer_status_code == 400:
#    print("Success! Computer online.")
# else:
#    print("ALERT: Computer offline!")

#    if shuttle_speed > 17500:
#    print("ALERT: Escape velocity reached!")
# elif shuttle_speed < 8000:
#    print("ALERT: Cannot maintain orbit!")
# else:
#    print("Stable speed.")

# Assign initial values for the space shuttle conditions
engine_indicator_light = "red blinking"  # Example values: "green", "green blinking", "red blinking"
space_suits_on = True
shuttle_cabin_ready = True
crew_status = space_suits_on and shuttle_cabin_ready
computer_status_code = 200  # Example values: 200, 400, 500
shuttle_speed = 15000  # Adjust this value to see different outputs

# Check the engine indicator light status
if engine_indicator_light == "green":
    print("engines have started")
elif engine_indicator_light == "green blinking":
    print("engines are preparing to start")
else:
    print("engines are off")

# Check if the crew is ready
if crew_status:
    print("Crew Ready")
else:
    print("Crew Not Ready")

# Check computer status code
if computer_status_code == 200:
    print("Please stand by. Computer is rebooting.")
elif computer_status_code == 400:
    print("Success! Computer online.")
else:
    print("ALERT: Computer offline!")

# Check shuttle speed
if shuttle_speed > 17500:
    print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8000:
    print("ALERT: Cannot maintain orbit!")
else:
    print("Stable speed.")
