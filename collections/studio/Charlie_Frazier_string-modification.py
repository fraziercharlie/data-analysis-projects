my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
my_string = "LaunchCode"

num_to_move = 3

if len(my_string) >= num_to_move:
    first_part = my_string[:num_to_move]
    remainder = my_string[num_to_move:]
    modified_string = remainder + first_part
else: modified_string = my_string

print("Original String:", my_string)
print("Modified String:", modified_string)

# my_string = "LaunchCode"

# print(len(my_string))

# #slice:
# modified_string = my_string[3:], my_string[:3] 
# print("Original String:", my_string)
# print("Modified String:", modified_string)



# Use a template literal to print the original and modified string in a descriptive phrase.
my_string = "LaunchCode"

num_to_move = 3

if len(my_string) >= num_to_move:
    first_part = my_string[:num_to_move]
    
    remainder = my_string[num_to_move:]
    
    # Concatenate
    modified_string = remainder + first_part
else: modified_string = my_string

print(f"Original String: {my_string}")
print(f"Modified String: {modified_string}")
print(f"After moving the first {num_to_move} characters from '{my_string}' to the end, the result is '{modified_string}'.")



# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
def modify_launchcode_string():
    
    my_string = "LaunchCode_Data_Analyst"
        
    print(f"Original string: {my_string}")
    
    number_of_letters = 5 
    
    if number_of_letters > len(my_string):
        
        print("Too long; default to 3.")

        number_of_letters = 3

    modified_string = my_string[number_of_letters:] + my_string[:number_of_letters]

    # modified string
    print(f"Modified string: {modified_string}")
    modify_launchcode_string()

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
#I can't figure this one out. 

def modify_string():

    my_string = "LaunchCode_Data_Analyst"


    print(f"Original string: {my_string}")


    input_text = input("Enter the number of letters to relocate: ")


    try:
        number_of_letters = int(input_text)
    except ValueError:
        print("Invalid input; using default of 3 letters.")
        number_of_letters = 3


    if number_of_letters > len(my_string):
        print(f"Input of {number_of_letters} exceeds string length of {len(my_string)}. Defaulting to 3.")
        number_of_letters = 3


    modified_string = my_string[number_of_letters:] + my_string[:number_of_letters]
    

    error_note = "Defaulted to 3 for excess input." if number_of_letters == 3 and int(input_text) > len(my_string) else ""

    print(f"Modified string: {modified_string} {error_note}")

modify_string()
