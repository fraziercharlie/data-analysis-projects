# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
def rev_charac(s):
    return s[::-1]
var_name = 'apple'
print(rev_charac(var_name))

# b) Within the function, use the 'list' function to split a string into a list of individual characters
def rev_charac(s):
    char_list = list(s)
    char_list.reverse()
    rev_string = ''.join(char_list)
    return rev_string
var_name = 'apple'
print(rev_charac(var_name))

# c) 'reverse' your new list.
def rev_charac(s):
    char_list = list(s)
    char_list.reverse()
    rev_string = ''.join(char_list)
    return rev_string
var_name = 'apple'
print(rev_charac(var_name))

# d) Use 'join' to create the reversed string and return that string from the function.
def rev_charac(s):
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)
var_name = 'apple'
print(rev_charac(var_name))
print(rev_charac('LC101'))
print(rev_charac('Capitalized Letters')) 
print(rev_charac('I love the smell of code in the morning.')) 

# e) Create a variable of type string to test your new function. 
def rev_charac(s):
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)
test_string = 'hello'
print(rev_charac(test_string))
print(rev_charac('Charlie Frazier'))

# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
def rev_charac(s):
    char_list = list(s)
    char_list.reverse()
    return ''.join(char_list)
var_name = 'hello'
print(rev_charac(var_name))

# g) Use method chaining to reduce the lines of code within the function.





# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.




list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
