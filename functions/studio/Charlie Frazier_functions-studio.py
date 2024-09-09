`# # # # We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# # # # a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# # # def rev_charac(s):
# # #     return s[::-1]
# # # var_name = 'apple'
# # # print(rev_charac(var_name))

# # # # b) Within the function, use the 'list' function to split a string into a list of individual characters
# # # def rev_charac(s):
# # #     char_list = list(s)
# # #     char_list.reverse()
# # #     rev_string = ''.join(char_list)
# # #     return rev_string
# # # var_name = 'apple'
# # # print(rev_charac(var_name))

# # # # c) 'reverse' your new list.
# # # def rev_charac(s):
# # #     char_list = list(s)
# # #     char_list.reverse()
# # #     rev_string = ''.join(char_list)
# # #     return rev_string
# # # var_name = 'apple'
# # # print(rev_charac(var_name))

# # # # d) Use 'join' to create the reversed string and return that string from the function.
# # # def rev_charac(s):
# # #     char_list = list(s)
# # #     char_list.reverse()
# # #     return ''.join(char_list)
# # # var_name = 'apple'
# # # print(rev_charac(var_name))
# # # print(rev_charac('LC101'))
# # # print(rev_charac('Capitalized Letters')) 
# # # print(rev_charac('I love the smell of code in the morning.')) 

# # # # e) Create a variable of type string to test your new function. 
# # # def rev_charac(s):
# # #     char_list = list(s)
# # #     char_list.reverse()
# # #     return ''.join(char_list)
# # # test_string = 'hello'
# # # print(rev_charac(test_string))
# # # print(rev_charac('Charlie Frazier'))

# # # # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# # # def rev_charac(s):
# # #     char_list = list(s)
# # #     char_list.reverse()
# # #     return ''.join(char_list)
# # # var_name = 'hello'
# # # print(rev_charac(var_name))

# # # # g) Use method chaining to reduce the lines of code within the function.
# # # def rev_charac(s):
# # #     return ''.join(reversed(list(s)))
# # # var_name = 'hello, hello_kitty'
# # # print(rev_charac(var_name))

# # # # 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# # # def rev_charac(item):
# # #     if isinstance(item, (int, float)):
# # #         reversed_num = str(item)[::-1]
# # #         if '.' in reversed_num:
# # #             return float(reversed_num)
# # #         else: return int(reversed_num)
# # #     elif isinstance(item, str):
# # #         return item[::-1]
# # #     else: return item
# # # print(rev_charac('hello, why use isinstance and not type'))
# # # print(rev_charac(1234))
# # # print(rev_charac(str('1234')))

# # # # a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# # # def rev_charac(item):
# # #     if isinstance(item, int):
# # #         reversed_num = str(item)[::-1]
# # #         return int(reversed_num)
# # #     elif isinstance(item, float):
# # #         reversed_num = str(item)[::-1]
# # #         return float(reversed_num)
# # #     elif isinstance(item, str):
# # #         return item[::-1]
# # #     else: 
# # #         return item
# # # print(rev_charac(1000005))
# # # print(rev_charac([5,4,3,2,1]))


# # # # d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# # # def rev_charac(item):
# # #     if isinstance(item, str):
# # #         return item[::-1]
# # #     elif isinstance(item, (int, float)):
# # #         reversed_str = str(item)[::-1]
# # #         if '.' in reversed_str:
# # #             return float(reversed_str)
# # #         else: 
# # #             return int(reversed_str)
# # #     else:
# # #         return item
# # # print(rev_charac(['I love python']))

# # # # e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
# # # def rev_charac(item):
# # #     if isinstance(item, str):
# # #         return item[::-1]
# # #     elif isinstance(item, (int, float)):
# # #         reversed_str = str(item)[::-1]
# # #         if '.' in reversed_str:
# # #             return float(reversed_str)
# # #         else: 
# # #             return int(reversed_str)
# # #     else:
# # #         return item

# # # will_this_string_work = 'python_string_please_work'
# # # print(rev_charac('python_string_please_work'))


# # # # 3) Create a new function with one parameter, which is the list we want to change. The function should:
# # # def compl_rev(items):
# # #     rev_list = items[::-1]
# # #     final_rev_list = []
# # #     for item in rev_list:
# # #         if isinstance(item, str):
# # #             rev_list = item[::-1]
# # #         elif isinstance(item, (int, float)):
# # #             rev_item = str(item)[::-1]
# # #             if '.' in rev_item:
# # #                 rev_item = float(rev_item)
# # #             else: 
# # #                 rev_item = int(rev_item)
# # #         else: 
# # #             rev_item = item
# # #         final_rev_list.append(rev_item)
# # #     return final_rev_list
# # # try_this = [['apple', 'potato', 'Capitalized Words']]
# # # print(compl_rev(try_this)) # what am I doing wrong on this? I can't get it to reverse completely.

# # # # a) Define and initialize an empty list.
# # # items = []
# # # # b) Loop through the old list.
# # # # old_list = ['hello', 'world', 123, 'orange']
# # # # for words in old_list:
# # # #     print("charlie", words + "!")
# # # # use_words = []
# # # # for words in old_list:
# # # #     use_words.append(words.use())
# # # # print(use_words)

# # # # c) For each element in the old list, call reverse_characters to flip the characters or digits.
# # # def rev_charac(item):
# # #     if isinstance(item, str):
# # #         return item[::-1]
# # #     elif isinstance(item, (int, float)):
# # #         reversed_str = str(item)[::-1]
# # #         if '.' in reversed_str:
# # #             return float(reversed_str)
# # #         else: 
# # #             return int(reversed_str)
# # #     else:
# # #         return item
# # # old_list = ['hello', 'world', 123, 'orange']
# # # rev_list = []
# # # for item in old_list:
# # #     rev_item = rev_charac(item)
# # #     rev_list.append(rev_item)
# # # print(rev_charac('old_list'))
# # # print('rev_list')
# # # # d) Add the reversed string (or number) to the list defined in part ‘a’.
# # # def rev_charac(item):
# # #     if isinstance(item, str):
# # #         return item[::-1]
# # #     elif isinstance(item, (int, float)):
# # #         reversed_str = str(item)[::-1]
# # #         if '.' in reversed_str:
# # #             return float(reversed_str)
# # #         else: 
# # #             return int(reversed_str)
# # #     else:
# # #         return item
# # # # e) Return the final, reversed list.

# # # # f) Be sure to print the results from each test case in order to verify your code.
# # # def rev_charac(item):
# # #     if isinstance(item, str):
# # #         return item[::-1]
# # #     elif isinstance(item, (int, float)):
# # #         reversed_str = str(item)[::-1]
# # #         if '.' in reversed_str:
# # #             return float(reversed_str)
# # #         else: 
# # #             return int(reversed_str)
# # #     else:
# # #         return item



# # # list_test1 = ['apple', 'potato', 'Capitalized Words']
# # # list_test2 = [123, 8897, 42, 1168, 8675309]
# # # list_test3 = ['hello', 'world', 123, 'orange']


# import numpy as np

# # Create a NumPy array from a list
# array1 = np.array([8, 5, 3, 2, 1, 1])
# print(array1)
# # import numpy as np

# # Create a NumPy multi-dimensional array from nested lists
# array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# print(array2)
# # import numpy as np

# # Create a NumPy multi-dimensional array from nested lists
# # array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# # Number of dimensions of array2
# print(array2.ndim)
# # Number of elemets (rows & columns in this instance) of array2
# print(array2.shape)
# # import numpy as np

# # Create a NumPy array from a list
# # array1 = np.array([8, 5, 3, 2, 1, 1])
# # Sort array1
# print(np.sort(array1))

# # import numpy as np

# # Create a NumPy array from a list
# # array1 = np.array([8, 5, 3, 2, 1, 1])
# # Split array1 into three separate arrays
# newarray1 = np.array_split(array1, 3)
# print(newarray1)

# # import numpy as np

# # Create a NumPy multi-dimensional array from nested lists
# # array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# print('Mean of array2:', np.mean(array2))
# print('Standard Deviation of array2:', np.std(array2))
# print('Sum of array2:', np.sum(array2))

# # import numpy as np

# # Create a NumPy multi-dimensional array from nested lists
# # array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# print('Mean of elements in axis 0 of array2:', np.mean(array2, axis=0))
# print('Mean of elements in axis 1 of array2:', np.mean(array2, axis=1))

# import pandas
# import pandas as pd

# # Create a pandas Series by providing a list
# example_list = pd.Series(["apple", "banana", "avocado", "honey dew"])

# # Create a pandas Series from a pre-existing list of values
# pre_existing_list = ["apple", "banana", "avocado", "honey dew"]

# series_from_existing_list = pd.Series(pre_existing_list)

# # import pandas
# import pandas as pd

# # Create a pandas Series by providing a dictionary, the i represents the index of the dictionary
# example_dictionary = pd.Series({'0': "apple", '1': "banana", '2': "avocado", '3': "honey dew"})

# # Create a pandas Series from a pre-existing dictionary, the i represents the index of the dictionary
# pre_existing_dictionary = {'0': "apple", '1': "banana", '2': "avocado", '3': "honey dew"}

# series_from_existing_dictionary = pd.Series(pre_existing_dictionary)

# # import pandas
# import pandas as pd

# # Create a pandas Series by providing a tuple
# example_tuple = pd.Series(("Interstellar", "Pride and Prejudice", "Inception", "Barbie"))

# # Create a pandas Series by providing a pre-existing tuple
# pre_existing_tuple = ("Interstellar", "Pride and Prejudice", "Inception", "Barbie")

# series_from_existing_tuple = pd.Series(pre_existing_tuple)

# custom_index_labels = pd.Series(["apple", "banana", "avocado", "honey dew"], index = ["red", "yellow", "green", "green"])

# # import pandas
# import pandas as pd

# # Create a pandas Series from a pre-existing dictionary, the i represents the index of the dictionary
# fruit_data = {'0': "apple", '1': "banana", '2': "avocado", '3': "honey dew"}

# # create a series from the fruit_data
# fruit_series = pd.Series(fruit_data)

# # Subset the existing series
# subset_fruit = fruit_series[:2]

# # Print the subset
# print(subset_fruit)

# # Subset Series to include elements from index 1 to 3
# subset_fruit_twice = fruit_series[1:4]
# # Print the series
# print("Subset elements from index 1 to 3")
# print(subset_fruit_twice)

# # import pandas
# import pandas as pd

# # Create a pandas DataFrame by providing a list of lists
# movie_list_of_lists = pd.DataFrame([["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],["Marley & Me", "Two Weeks Notice", "The Guardian", "Bridesmaids"]])

# # Create a pandas DataFrame from a pre-existing list of lists
# movies_dataframe_data = [["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],["Marley & Me", "The Proposal", "The Guardian", "Bridesmaids"]]

# dataframe_from_existing_list = pd.DataFrame(movies_dataframe_data)

# # import pandas
# import pandas as pd

# # Create a pandas DataFrame by providing a dictionary
# movie_dictionary_dataframe = pd.DataFrame(movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003]})

# # Create a pandas DataFrame from a pre-existing dictionary
# movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003]}

# dataframe_from_movies_dictionary = pd.DataFrame(movies)


# # import pandas
# import pandas as pd

# # Create a pandas DataFrame by providing a dictionary
# movie_dictionary_dataframe = pd.DataFrame(movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003]})

# # Create a pandas DataFrame from a pre-existing dictionary
# movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003]}

# dataframe_from_movies_dictionary = pd.DataFrame(movies)



# # import pandas
# import pandas as pd

# # Create a pandas DataFrame by providing a tuple
# movies_tuple_dataframe = pd.DataFrame(("Interstellar", "Pride and Prejudice"), ("Inception", "Barbie"))

# # Create a pandas DataFrame by providing a pre-existing tuple
# movies_data = (("Interstellar", "Pride and Prejudice"), ("Inception", "Barbie"))

# dataframe_from_existing_tuple = pd.DataFrame(movies_data).

# import pandas as pd

# movies = pd.Series(["Interstellar", "Pride and Prejudice", "Inception", "Barbie"], index=['1', '2', '3', '4'], name = 'movies')

# genres = pd.Series(["Science Fiction", "Novel", "Science Fiction", "Comedy"], index=['1', '2', '3', '4'], name='genres')

# # Using the two series above we can concatenate the two together in order to create a DataFrame.

# movies_genres_dataframe = pd.concat([movies, genres], axis=1) # axis 1 specifies that the operations will be performed down each column

# # import pandas
# import pandas as pd

# movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003]}

# movies_dataframe = pd.DataFrame(movies)

# movie_names = movies_dataframe["Name"]

import pandas as pd

# read a data file and assign to variable
data_file = pd.read_csv('path-to-file.csv')

# print out various info within the DataFrame
## first 10 rows of the DataFrame
print(data_file.head(10))

## last 15 rows of the DataFrame
print(data_file.tail(15))

## list out all columns within the DataFrame
print(data_file.columns)
# import pandas
import pandas as pd

# Create a pandas DataFrame using a dictionary
movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003], 'Genre': ["Science Fiction", "Novel", "Science Fiction", "Comedy"]}

movies_dataframe = pd.DataFrame(movies)

# Select only movies from the Science Fiction genre
science_fiction = movies_dataframe[movies_dataframe['Genre'] == "Science Fiction"]

# Print the data
print(science_fiction)

# import pandas
import pandas as pd

# Create a pandas DataFrame using a dictionary
movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003], 'Genre': ["Science Fiction", "Novel", "Science Fiction", "Comedy"]}

movies_dataframe = pd.DataFrame(movies)

# Select only movies from the Science Fiction genre
science_fiction = movies_dataframe[(movies_dataframe['Genre'] == "Science Fiction") & (movies_dataframe['Release'] <= 2010)]

# Print the data
print(science_fiction)

# import pandas
import pandas as pd

# Create a pandas DataFrame using a dictionary
movies = {'Name': ["Interstellar", "Pride and Prejudice", "Inception", "Barbie"],'Release': [2014, 2005, 2010, 2003], 'Genre': ["Science Fiction", "Novel", "Science Fiction", "Comedy"]}

movies_dataframe = pd.DataFrame(movies)

# Select only movies from the Science Fiction genre
science_fiction = movies_dataframe[(movies_dataframe['Genre'] == "Science Fiction") & (movies_dataframe['Release'] <= 2010)]

# Print the data
print(science_fiction)