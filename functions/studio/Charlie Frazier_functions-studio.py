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
def rev_charac(s):
    return ''.join(reversed(list(s)))
var_name = 'hello, hello_kitty'
print(rev_charac(var_name))

# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
def rev_charac(item):
    if isinstance(item, (int, float)):
        reversed_num = str(item)[::-1]
        if '.' in reversed_num:
            return float(reversed_num)
        else: return int(reversed_num)
    elif isinstance(item, str):
        return item[::-1]
    else: return item
print(rev_charac('hello, why use isinstance and not type'))
print(rev_charac(1234))
print(rev_charac(str('1234')))

# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
def rev_charac(item):
    if isinstance(item, int):
        reversed_num = str(item)[::-1]
        return int(reversed_num)
    elif isinstance(item, float):
        reversed_num = str(item)[::-1]
        return float(reversed_num)
    elif isinstance(item, str):
        return item[::-1]
    else: 
        return item
print(rev_charac(1000005))
print(rev_charac([5,4,3,2,1]))


# d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
def rev_charac(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, (int, float)):
        reversed_str = str(item)[::-1]
        if '.' in reversed_str:
            return float(reversed_str)
        else: 
            return int(reversed_str)
    else:
        return item
print(rev_charac(['I love python']))

# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
def rev_charac(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, (int, float)):
        reversed_str = str(item)[::-1]
        if '.' in reversed_str:
            return float(reversed_str)
        else: 
            return int(reversed_str)
    else:
        return item

will_this_string_work = 'python_string_please_work'
print(rev_charac('python_string_please_work'))


# 3) Create a new function with one parameter, which is the list we want to change. The function should:
def compl_rev(items):
    rev_list = items[::-1]
    final_rev_list = []
    for item in rev_list:
        if isinstance(item, str):
            rev_list = item[::-1]
        elif isinstance(item, (int, float)):
            rev_item = str(item)[::-1]
            if '.' in rev_item:
                rev_item = float(rev_item)
            else: 
                rev_item = int(rev_item)
        else: 
            rev_item = item
        final_rev_list.append(rev_item)
    return final_rev_list
try_this = [['apple', 'potato', 'Capitalized Words']]
print(compl_rev(try_this)) # what am I doing wrong on this? I can't get it to reverse completely.

# a) Define and initialize an empty list.
items = []
# b) Loop through the old list.
# old_list = ['hello', 'world', 123, 'orange']
# for words in old_list:
#     print("charlie", words + "!")
# use_words = []
# for words in old_list:
#     use_words.append(words.use())
# print(use_words)

# c) For each element in the old list, call reverse_characters to flip the characters or digits.
def rev_charac(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, (int, float)):
        reversed_str = str(item)[::-1]
        if '.' in reversed_str:
            return float(reversed_str)
        else: 
            return int(reversed_str)
    else:
        return item
old_list = ['hello', 'world', 123, 'orange']
rev_list = []
for item in old_list:
    rev_item = rev_charac(item)
    rev_list.append(rev_item)
print(rev_charac('old_list'))
print('rev_list')
# d) Add the reversed string (or number) to the list defined in part ‘a’.
def rev_charac(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, (int, float)):
        reversed_str = str(item)[::-1]
        if '.' in reversed_str:
            return float(reversed_str)
        else: 
            return int(reversed_str)
    else:
        return item
# e) Return the final, reversed list.

# f) Be sure to print the results from each test case in order to verify your code.
def rev_charac(item):
    if isinstance(item, str):
        return item[::-1]
    elif isinstance(item, (int, float)):
        reversed_str = str(item)[::-1]
        if '.' in reversed_str:
            return float(reversed_str)
        else: 
            return int(reversed_str)
    else:
        return item



list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
