proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
# List of strings to check
strings = ["3,6,9,12", "A;C;M;E", "space delimited string","Comma-spaces, might, require, typing, caution"]

# Loop
for proto_string in strings:
    
    if ',' in proto_string:
        delimiter = 'comma'
    
    elif ';' in proto_string:
        delimiter = 'semicolon'
    
    else:
        delimiter = 'space'
    
    print(f"'{proto_string}' uses {delimiter} as a delimiter.")


# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
def process_comma_string(input_string):
    
    items = input_string.split(',')
    
    
    items.reverse()
    
    
    output_string = ','.join(items)
    
    return output_string

comma_separated_string = "3,6,9,12"
processed_string = process_comma_string(comma_separated_string)
print(f"Original: '{comma_separated_string}' -> Reversed: '{processed_string}'")



# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
def process_semicolon_string(input_string):
    
    items = input_string.split(';')
    
    # Sort this alphabetically
    items.sort()
    
    
    output_string = ','.join(items)
    
    return output_string

semicolon_separated_string = "A;C;M;E"
processed_string = process_semicolon_string(semicolon_separated_string)
print(f"Original: '{semicolon_separated_string}' -> Alphabetized: '{processed_string}'")



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
def process_space_string(input_string):
    
    items = input_string.split()
        
    items.sort(reverse=True)
        
    output_string = ' '.join(items)
    
    return output_string

space_separated_string = "I love coding with launchCode"
processed_string = process_space_string(space_separated_string)
print(f"Original: '{space_separated_string}' -> Reverse Alphabetized: '{processed_string}'")



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
def process_comma_space_string(input_string):
    
    items = input_string.split(', ')
        
    items.sort()
        
    output_string = '-'.join(items)
    
    return output_string

comma_space_separated_string = "LaUnChCoDe, Data, Analyst, Excited"
processed_string = process_comma_space_string(comma_space_separated_string)
print(f"Original: '{comma_space_separated_string}' -> Alphabetized: '{processed_string}'")
