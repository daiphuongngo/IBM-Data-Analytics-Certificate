#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:30:52 2020

@author: phuongdaingo
"""
"""
Tuples in Python
Welcome! This notebook will teach you about the tuples in the Python 
Programming Language. By the end of this lab, you'll know the basics tuple 
operations in Python, including indexing, slicing and sorting.

Table of Contents
About the Dataset
Tuples
Indexing
Slicing
Sorting
Quiz on Tuples
Estimated time needed: 15 min

About the Dataset
Imagine you received album recommendations from your friends and compiled all 
of the recommandations into a table, with specific information about each album.

The table has one row for each movie and several columns:

artist - Name of the artist
album - Name of the album
released_year - Year the album was released
length_min_sec - Length of the album (hours,minutes,seconds)
genre - Genre of the album
music_recording_sales_millions - Music recording sales (millions in USD) on 
SONG://DATABASE
claimed_sales_millions - Album's claimed sales (millions in USD) on 
SONG://DATABASE
date_released - Date on which the album was released
soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
rating_of_friends - Indicates the rating from your friends from 1 to 10

The dataset can be seen below:

*** Tuples
In Python, there are different data types: string, integer and float. These 
data types can all be contained in a tuple as follows:

Now, let us create your first tuple with string, integer and float."""

# Create your first tuple
tuple1 = ("disco",10,1.2 )
tuple1


"""The type of variable is a tuple."""

# Print the type of the tuple you created
type(tuple1)


"""Indexing
Each element of a tuple can be accessed via an index. The following table 
represents the relationship between the index and the items in the tuple. 
Each element can be obtained by the name of the tuple followed by a square 
bracket with the index number:
    
We can print out each value in the tuple:"""

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


"""We can print out the type of each value in the tuple:"""

# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


"""We can also use negative indexing. We use the same table above with 
corresponding negative values:

We can obtain the last element as follows (this time we will not use the print 
statement to display the values):"""

# Use negative index to get the value of the last element
tuple1[-1]


"""We can display the next two elements as follows:"""

# Use negative index to get the value of the second last element
tuple1[-2]

# Use negative index to get the value of the third last element
tuple1[-3]


"""Concatenate Tuples
We can concatenate or combine tuples by using the + sign:"""

# Concatenate two tuples
tuple2 = tuple1 + ("hard rock", 10)
tuple2


"""We can slice tuples obtaining multiple values as demonstrated by the figure 
below:

Slicing
We can slice tuples, obtaining new tuples with the corresponding elements:"""

# Slice from index 0 to index 2
tuple2[0:3]

"""We can obtain the last two elements of the tuple:"""

# Slice from index 3 to index 4
tuple2[3:5]


"""We can obtain the length of a tuple using the length command:"""

# Get the length of tuple
len(tuple2)


"""This figure shows the number of elements:

Sorting
Consider the following tuple:"""

# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
We can sort the values in a tuple and save it to a new tuple:

# Sort the tuple
RatingsSorted = sorted(Ratings)
RatingsSorted
Nested Tuple


"""A tuple can contain another tuple as well as other more complex data types. 
This process is called 'nesting'. Consider the following tuple with several 
elements:"""

# Create a nest tuple
NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


"""Each element in the tuple including other tuples can be obtained via an 
index as shown in the figure:

# Print element on each index"""
​
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


"""We can use the second index to access other tuples as demonstrated in the 
figure:

We can access the nested tuples :"""

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


"""We can access strings in the second nested tuples using a third index:"""

# Print the first element in the second nested tuples
NestedT[2][1][0]

# Print the second element in the second nested tuples
NestedT[2][1][1]


"""We can use a tree to visualise the process. Each new index corresponds to a 
deeper level in the tree:

Similarly, we can access elements nested deeper in the tree with a fourth index:"""

# Print the first element in the second nested tuples
NestedT[4][1][0]

# Print the second element in the second nested tuples
NestedT[4][1][1]


"""The following figure shows the relationship of the tree and the element 
NestedT[4][1][1]:

*** Quiz on Tuples

Consider the following tuple:"""
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple


"""Find the length of the tuple, genres_tuple:"""
# Write your code below and press Shift+Enter to execute
len(genres_tuple)


"""Access the element, with respect to index 3:"""
# Write your code below and press Shift+Enter to execute
genres_tuple[3]


"""Use slicing to obtain indexes 3, 4 and 5:"""
# Write your code below and press Shift+Enter to execute
genres_tuple[3:6]


"""Find the first two elements of the tuple genres_tuple:"""
# Write your code below and press Shift+Enter to execute
genres_tuple[0:2]


"""Find the first index of "disco":"""
# Write your code below and press Shift+Enter to execute
genres_tuple.index("disco")


"""Generate a sorted List from the Tuple C_tuple=(-5, 1, -3):"""
# Write your code below and press Shift+Enter to execute
C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
C_list


"""===============
Lists in Python
Welcome! This notebook will teach you about the lists in the Python Programming 
Language. By the end of this lab, you'll know the basics list operations in 
Python, including indexing, list operations and copy/clone list.

Table of Contents
About the Dataset
Lists
Indexing
List Content
List Operations
Copy and Clone List
Quiz on Lists
Estimated time needed: 15 min

About the Dataset
Imagine you received album recommendations from your friends and compiled all 
of the recommandations into a table, with specific information about each album.

The table has one row for each movie and several columns:

artist - Name of the artist
album - Name of the album
released_year - Year the album was released
length_min_sec - Length of the album (hours,minutes,seconds)
genre - Genre of the album
music_recording_sales_millions - Music recording sales (millions in USD) on 
SONG://DATABASE
claimed_sales_millions - Album's claimed sales (millions in USD) on 
SONG://DATABASE
date_released - Date on which the album was released
soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
rating_of_friends - Indicates the rating from your friends from 1 to 10

The dataset can be seen below:

Lists
Indexing
We are going to take a look at lists in Python. A list is a sequenced 
collection of different objects such as integers, strings, and other lists as 
well. The address of each element within a list is called an index. An index 
is used to access and refer to items within a list.

To create a list, type the list within square brackets [ ], with your content 
inside the parenthesis and separated by commas. Let’s try it!"""

# Create a list
L = ["Michael Jackson", 10.1, 1982]
L


"""We can use negative and regular indexing with a list :"""
# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


"""List Content
Lists can contain strings, floats, and integers. We can nest other lists, and 
we can also nest tuples and other data structures. The same indexing conventions 
apply for nesting:"""

# Sample List
["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]


"""List Operations
We can also perform slicing in lists. For example, if we want the last two 
elements, we use the following command:"""

# Sample List
L = ["Michael Jackson", 10.1,1982,"MJ",1]
L


# List slicing
L[3:5]


"""We can use the method extend to add new elements to the list:"""

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L


"""Another similar method is append. If we apply append instead of extend, 
we add one element to the list:"""

# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L


"""Each time we apply a method, the list changes. If we apply extend we add 
two new elements to the list. The list L is then modified by adding two new 
elements:"""

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L


"""If we append the list ['a','b'] we have one new element consisting of a 
nested list:"""

# Use append to add elements to list
L.append(['a','b'])
L


"""As lists are mutable, we can change them. For example, we can change the 
first element as follows:"""

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


"""We can also delete an element of a list using the del command:"""

# Delete the element based on the index
print('Before change:', A)
del(A[0])
print('After change:', A)


"""We can convert a string to a list using split. For example, the method split 
translates every group of characters separated by a space into an element in a 
list:"""

# Split the string, default is by space
'hard rock'.split()


"""We can use the split function to separate strings on a specific character. 
We pass the character we would like to split on into the argument, which in 
this case is a comma. The result is a list, and each element corresponds to 
a set of characters that have been separated by a comma:"""

# Split the string by comma
'A,B,C,D'.split(',')


"""============
Copy and Clone List
When we set one variable B equal to A; both A and B are referencing the same 
list in memory:"""

# Copy (copy by reference) the list A
A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


"""Initially, the value of the first element in B is set as hard rock. If we 
change the first element in A to banana, we get an unexpected side effect. As 
A and B are referencing the same list, if we change list A, then list B also 
changes. If we check the first element of B we get banana instead of hard rock:"""

# Examine the copy by reference
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])


"""This is demonstrated in the following figure:
You can clone list A by using the following syntax:"""

# Clone (clone by value) the list A
B = A[:]
B


"""Variable B references a new copy or clone of the original list; this is 
demonstrated in the following figure:

Now if you change A, B will not change:"""

print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])


"""=============
Quiz on List
Create a list a_list, with the following elements 1, hello, [1,2,3] and True."""

# Write your code below and press Shift+Enter to execute
a_list = [1, 'hello', [1, 2, 3] , True]
a_list


"""Find the value stored at index 1 of a_list."""

# Write your code below and press Shift+Enter to execute
a_list[1]


"""Retrieve the elements stored at index 1, 2 and 3 of a_list."""

# Write your code below and press Shift+Enter to execute
a_list[1:4]


"""Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:"""
# Write your code below and press Shift+Enter to execute
A = [1, 'a'] 
B = [2, 1, 'd']
A + B


"""=================
Sets in Python
Welcome! This notebook will teach you about the sets in the Python Programming 
Language. By the end of this lab, you'll know the basics set operations in 
Python, including what it is, operations and logic operations.

Table of Contents
Sets
Set Content
Set Operations
Sets Logic Operations
Quiz on Sets
Estimated time needed: 20 min

Sets
Set Content
A set is a unique collection of objects in Python. You can denote a set with 
a curly bracket {}. Python will automatically remove duplicate items:"""

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


"""The process of mapping is illustrated in the figure:

You can also create a set from a list as follows:"""

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


"""Now let us create a set of genres:"""

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres


"""===============
Set Operations
Let us go over set operations, as these can be used to change the set. 
Consider the set A:"""

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
A


"""We can add an element to a set using the add() method:"""

# Add element to set
A.add("NSYNC")
A


"""If we add the same element twice, nothing will happen as there can be no 
duplicates in a set:"""

# Try to add duplicate element to the set
A.add("NSYNC")
A


"""We can remove an item from a set using the remove method:"""

# Remove the element from set
A.remove("NSYNC")
A


"""We can verify if an element is in the set using the in command:"""

# Verify if the element is in the set
"AC/DC" in A


"""==============
Sets Logic Operations
Remember that with sets you can check the difference between sets, as well as 
the symmetric difference, intersection, and union:

Consider the following two sets:"""

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
album_set1, album_set2


"""As both sets contain AC/DC and Back in Black we represent these common elements 
with the intersection of two circles.

You can find the intersect of two sets as follow using &:"""

# Find the intersections
intersection = album_set1 & album_set2
intersection


"""You can find all the elements that are only contained in album_set1 using 
the difference method:"""

# Find the difference in set1 but not set2
album_set1.difference(album_set2)  


"""You only need to consider elements in album_set1; all the elements in 
album_set2, including the intersection, are not included.

The elements in album_set2 but not in album_set1 is given by:"""

album_set2.difference(album_set1)  


"""You can also find the intersection of album_list1 and album_list2, using the 
intersection method:"""

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)   


"""This corresponds to the intersection of the two circles:

The union corresponds to all the elements in both sets, which is represented 
by coloring both circles:

The union is given by:"""

# Find the union of two sets
album_set1.union(album_set2)


"""And you can check if a set is a superset or subset of another set, 
respectively, like this:"""

# Check if superset
set(album_set1).issuperset(album_set2)   

# Check if subset
set(album_set2).issubset(album_set1)     


"""Here is an example where issubset() and issuperset() return true:"""

# Check if subset
set({"Back in Black", "AC/DC"}).issubset(album_set1) 

# Check if superset
album_set1.issuperset({"Back in Black", "AC/DC"})   


"""===================
Quiz on Sets
Convert the list ['rap','house','electronic music', 'rap'] to a set:"""
# Write your code below and press Shift+Enter to execute
set(['rap','house','electronic music','rap'])


"""Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), 
does sum(A) = sum(B)"""
# Write your code below and press Shift+Enter to execute
A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))


"""Create a new set album_set3 that is the union of album_set1 and album_set2:"""
# Write your code below and press Shift+Enter to execute
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set3


"""Find out if album_set1 is a subset of album_set3:"""
# Write your code below and press Shift+Enter to execute
album_set1.issubset(album_set3)


"""================
Dictionaries in Python
Welcome! This notebook will teach you about the dictionaries in the Python 
Programming Language. By the end of this lab, you'll know the basics dictionary 
operations in Python, including what it is, and the operations on it.

Table of Contents
Dictionaries
What are Dictionaries?
Keys
Quiz on Dictionaries

Dictionaries
What are Dictionaries?
A dictionary consists of keys and values. It is helpful to compare a dictionary 
to a list. Instead of the numerical indexes such as a list, dictionaries have 
keys. These keys are the keys that are used to access values within a dictionary.

An example of a Dictionary Dict:"""

# Create the dictionary
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


"""The keys can be strings:"""

# Access to the value by the key
Dict["key1"]


"""Keys can also be any immutable object such as a tuple:"""

# Access to the value by the key
Dict[(0, 1)]


"""Each key is separated from its value by a colon ":". Commas separate the 
items, and the whole dictionary is enclosed in curly braces. An empty dictionary 
without any items is written with just two curly braces, like this "{}"."""

# Create a sample dictionary
release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


"""==============
In summary, like a list, a dictionary holds a sequence of elements. 
Each element is represented by a key and its corresponding value. Dictionaries 
are created with two curly braces containing keys and values separated by a 
colon. For every key, there can only be one single value, however, multiple 
keys can hold the same value. Keys can only be strings, numbers, or tuples, 
but values can be any data type.

It is helpful to visualize the dictionary as a table, as in the following image. 
The first column represents the keys, the second column represents the values.

Image
Keys
You can retrieve the values based on the names:"""

# Get value by keys
release_year_dict['Thriller'] 


"""This corresponds to:

Similarly for The Bodyguard"""

# Get value by key
release_year_dict['The Bodyguard'] 


"""Now let you retrieve the keys of the dictionary using the method 
release_year_dict():"""

# Get all the keys in dictionary
release_year_dict.keys() 


"""You can retrieve the values using the method values():"""

# Get all the values in dictionary
​
release_year_dict.values() 


"""We can add an entry:"""

# Append value with key into dictionary
release_year_dict['Graduation'] = '2007'
release_year_dict


"""We can delete an entry:"""

# Delete entries by key
del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


"""We can verify if an element is in the dictionary:"""

# Verify the key is in the dictionary
'The Bodyguard' in release_year_dict


"""===============
Quiz on Dictionaries
You will need this dictionary for the next two questions:"""

# Question sample dictionary
soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 

"""a) In the dictionary soundtrack_dict what are the keys ?"""
soundtrack_dic.keys() # The Keys "The Bodyguard" and "Saturday Night Fever" 
# --> dict_keys(['The Bodyguard', 'Saturday Night Fever'])


"""b) In the dictionary soundtrack_dict what are the values ?"""
soundtrack_dic.values() # The values are "1992" and "1977"
# --> dict_values(['1992', '1977'])


"""You will need this dictionary for the following questions:

The Albums Back in Black, The Bodyguard and Thriller have the following music 
recording sales in millions 50, 50 and 65 respectively:

a) Create a dictionary album_sales_dict where the keys are the album name and 
the sales in millions are the values."""

album_sales_dict = {"The Bodyguard":50, "Back in Black":50, "Thriller":65}


"""b) Use the dictionary to find the total sales of Thriller:"""

album_sales_dict["Thriller"]


"""c) Find the names of the albums from the dictionary using the method keys:"""

album_sales_dict.keys()


"""d) Find the names of the recording sales from the dictionary using the 
    method values:"""

album_sales_dict.values()