#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 15:11:54 2020

@author: phuongdaingo
"""

"""
Python - Writing Your First Python Code!
Welcome! This notebook will teach you the basics of the Python programming 
language. Although the information presented here is quite basic, it is an 
important foundation that will help you read and write Python code. By the end 
of this notebook, you'll know the basics of Python, including how to write basic 
commands, understand some basic types, and how to perform simple operations on 
them.

Table of Contents
- Say "Hello" to the world in Python
What version of Python are we using?
Writing comments in Python
Errors in Python
Does Python know about your error before it runs your code?
Exercise: Your First Program
- Types of objects in Python
Integers
Floats
Converting from one object type to a different object type
Boolean data type
Exercise: Types
- Expressions and Variables
Expressions
Exercise: Expressions
Variables
Exercise: Expression and Variables in Python

Say "Hello" to the world in Python
When learning a new programming language, it is customary to start with an 
"hello world" example. As simple as it is, this one line of code will ensure 
that we know how to print a string in output and how to execute code within 
cells in a notebook.

[Tip]: To execute the Python code in the code cell below, click on the cell to 
select it and press Shift + Enter.
# Try your first Python output"""
​
print('Hello, Python!')
Hello, Python!


"""===========After executing the cell above, you should see that Python prints 
Hello, Python!. Congratulations on running your first Python code!

[Tip:] print() is a function. You passed the string 'Hello, Python!' as an 
argument to instruct Python on what to print.
What version of Python are we using?
There are two popular versions of the Python programming language in use today: 
    Python 2 and Python 3. The Python community has decided to move on from 
    Python 2 to Python 3, and many popular libraries have announced that they 
    will no longer support Python 2.

Since Python 3 is the future, in this course we will be using it exclusively. 
How do we know that our notebook is executed by a Python 3 runtime? We can look 
in the top-right hand corner of this notebook and see "Python 3".

We can also ask directly Python and obtain a detailed answer. Try executing the 
following code:

# Check the Python Version"""
​
import sys
print(sys.version)
​
import sys
print(sys.version)


"""[Tip:] sys is a built-in module that contains many system-specific parameters 
and functions, including the Python version in use. Before using it, we must 
explictly import it.
Writing comments in Python
In addition to writing code, note that it's always a good idea to add comments 
to your code. It will help others understand what you were trying to accomplish
 (the reason why you wrote a given snippet of code). Not only does this help 
 other people understand your code, it can also serve as a reminder to you when 
 you come back to it weeks or months later.

To write comments in Python, use the number symbol # before writing your comment.
 When you run your code, Python will ignore everything past the # on a given line.

# Practice on writing comments"""
​
print('Hello, Python!') # This line prints a string
# print('Hi')


"""After executing the cell above, you should notice that This line prints a 
string did not appear in the output, because it was a comment (and thus ignored 
by Python).

The second line was also not executed because print('Hi') was preceded by the 
number sign (#) as well! Since this isn't an explanatory comment from the 
programmer, but an actual line of code, we might say that the programmer 
commented out that second line of code.

Errors in Python
Everyone makes mistakes. For many types of mistakes, Python will tell you that 
you have made a mistake by giving you an error message. It is important to read
 error messages carefully to really understand where you made a mistake and how
 you may go about correcting it.

For example, if you spell print as frint, Python will display an error message. 
Give it a try:

# Print string as error message"""
​
print("Hello, Python!")


"""The error message tells you:

where the error occurred (more useful in large notebook cells or scripts), and
what kind of error it was (NameError)
Here, Python attempted to run the function frint, but could not determine what 
frint is since it's not a built-in function and it has not been previously 
defined by us either.

You'll notice that if we make a different type of mistake, by forgetting to 
close the string, we'll obtain a different error (i.e., a SyntaxError). Try it 
below:

# Try to see build in error message"""
​
print("Hello, Python!)


"""=============
Does Python know about your error before it runs your code?
Python is what is called an interpreted language. Compiled languages examine 
your entire program at compile time, and are able to warn you about a whole 
class of errors prior to execution. In contrast, Python interprets your script 
line by line as it executes it. Python will stop executing the entire program 
when it encounters an error (unless the error is expected and handled by the 
programmer, a more advanced subject that we'll cover later on in this course).

Try to run the code in the cell below and see what happens:

# Print string and error to see the running order"""
​
print("This will be printed")
print("This will cause an error")
print("This will NOT be printed")


"""=============
Exercise: Your First Program
Generations of programmers have started their coding careers by simply printing 
"Hello, world!". You will be following in their footsteps.

In the code cell below, use the print() function to print out the phrase: Hello,
 world!
"""
print("Hello, world!")

"""Now, let's enhance your code with a comment. In the code cell below, print 
out the phrase: Hello, world! and comment it with the phrase Print the 
traditional hello world all in one line of code.
"""
print("Hello, world!") #Print the traditional hello world


"""=========
Types of objects in Python
Python is an object-oriented language. There are many different types of 
objects in Python. Let's start with the most common object types: strings, 
integers and floats. Anytime you write words (text) in Python, you're using 
character strings (strings for short). The most common numbers, on the other 
hand, are integers (e.g. -1, 0, 100) and floats, which represent real numbers 
(e.g. 3.14, -42.0).

The following code cells contain some examples."""

# Integer
int(11)

# Float
float(2.14)

# String
str("Hello, Python 101!")

"""You can get Python to tell you the type of an expression by using the 
built-in type() function. You'll notice that Python refers to integers as int, 
floats as float, and character strings as str."""

# Type of 12
type(12)

# Type of 2.14
type(2.14)

# Type of "Hello, Python 101!"
type("Hello, Python 101!")


"""In the code cell below, use the type() function to check the object type of 
12.0."""

type(12.0)


"""=====Integers
Here are some examples of integers. Integers can be negative or positive 
numbers:

We can verify this is the case by using, you guessed it, the type() function:"""

# Print the type of -1
type(-1)

# Print the type of 4
type(4)

# Print the type of 0
type(0)


"""===========
Floats
Floats represent real numbers; they are a superset of integer numbers but also 
include "numbers with decimals". There are some limitations when it comes to 
machines representing real numbers, but floating point numbers are a good 
representation in most cases. You can learn more about the specifics of floats 
for your runtime environment, by checking the value of sys.float_info. This 
will also tell you what's the largest and smallest number that can be 
represented with them.

Once again, can test some examples with the type() function:"""

# Print the type of 1.0
type(1.0) # Notice that 1 is an int, and 1.0 is a float

# Print the type of 0.5
type(0.5)

# Print the type of 0.56
type(0.56)

# System settings about float type
sys.float_info
sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, 
               min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, 
               dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, 
               rounds=1)

"""Converting from one object type to a different object type
You can change the type of the object in Python; this is called typecasting. 
For example, you can convert an integer into a float (e.g. 2 to 2.0).
Let's try it:"""

# Verify that this is an integer
type(2)


"""Converting integers to floats
Let's cast integer 2 to float:"""

# Convert 2 to a float
float(2)

# Convert integer 2 to a float and check its type
type(float(2))


"""When we convert an integer into a float, we don't really change the value 
(i.e., the significand) of the number. However, if we cast a float into an 
integer, we could potentially lose some information. For example, if we cast 
the float 1.1 to integer we will get 1 and lose the decimal information 
(i.e., 0.1):"""

# Casting 1.1 to integer will result in loss of information
int(1.1)


"""Converting from strings to integers or floats
Sometimes, we can have a string that contains a number within it. If this is 
the case, we can cast that string that represents a number into an integer 
using int():"""

# Convert a string into an integer
int('1')


"""But if you try to do so with a string that is not a perfect match for a 
number, you'll get an error. Try the following:"""

# Convert a string into an integer with error
int('1 or 2 people')

# Convert the string "1.2" into a float
float('1.2')


"""[Tip:] Note that strings can be represented with single quotes ('1.2') or 
double quotes ("1.2"), but you can't mix both (e.g., "1.2')."""


"""=============
Converting numbers to strings
If we can convert strings to numbers, it is only natural to assume that we can 
convert numbers to strings, right?"""

# Convert an integer to a string
str(1)

"""And there is no reason why we shouldn't be able to make floats into strings 
as well:"""

# Convert a float to a string
str(1.2)


"""=============
Boolean data type
Boolean is another important type in Python. An object of type Boolean can take 
on one of two values: True or False:"""

# Value true
True


"""Notice that the value True has an uppercase "T". The same is true for False 
(i.e. you must use the uppercase "F")."""

# Value false
False


"""When you ask Python to display the type of a boolean object it will show 
bool which stands for boolean:"""

# Type of True
type(True)
# ---> bool

# Type of False
type(False)
# ---> bool


"""We can cast boolean objects to other data types. If we cast a boolean with 
a value of True to an integer or float we will get a one. If we cast a boolean 
with a value of False to an integer or float we will get a zero. Similarly, if
we cast a 1 to a Boolean, you get a True. And if we cast a 0 to a Boolean we 
will get a False. Let's give it a try:""""

# Convert True to int
int(True)

# Convert 1 to boolean
bool(1)
#---> True

# Convert 0 to boolean
bool(0)
#---> False

# Convert True to float
float(True)
#---> 1.0


"""============
Exercise: Types
What is the data type of the result of: 6 / 2?"""

6 / 2

"""What is the type of the result of: 6 // 2? (Note the double slash //.)"""

6 // 2


"""============
Expression and Variables
Expressions
Expressions in Python can include operations among compatible types (e.g., 
integers and floats). For example, basic arithmetic operations like adding 
multiple numbers:"""

# Addition operation expression
43 + 60 + 16 + 41


"""We can perform subtraction operations using the minus operator. In this case 
the result is a negative number:"""

# Subtraction operation expression
50 - 60


"""We can do multiplication using an asterisk:"""

# Multiplication operation expression
5 * 5


"""We can also perform division with the forward slash:"""

# Division operation expression
25 / 5

# Division operation expression
25 / 6


"""As seen in the quiz above, we can use the double slash for integer division, 
where the result is rounded to the nearest integer:"""

# Integer division operation expression
25 // 5

# Integer division operation expression
25 // 6


"""===============
Exercise: Expression
Let's write an expression that calculates how many hours there are in 160 minutes:"""

160/60
160//60


"""Python follows well accepted mathematical conventions when evaluating 
mathematical expressions. In the following example, Python adds 30 to the 
result of the multiplication (i.e., 120)."""

# Mathematical expression
30 + 2 * 60


"""And just like mathematics, expressions enclosed in parentheses have priority.
So the following multiplies 32 by 60."""

# Mathematical expression
(30 + 2) * 60


"""==============
Variables
Just like with most programming languages, we can store values in variables, 
so we can use them later on. For example:"""

# Store value into variable
x = 43 + 60 + 16 + 41


"""==============
To see the value of x in a Notebook, we can simply place it on the last line 
of a cell:"""

# Print out the value in variable
x


"""We can also perform operations on x and save the result to a new variable:"""

# Use another variable to store the result of the operation between variable 
#and value
y = x / 60
y


"""If we save a value to an existing variable, the new value will overwrite 
the previous value:"""

# Overwrite variable with new value
​
x = x / 60
x


"""It's a good practice to use meaningful variable names, so you and others 
can read the code and understand it more easily:"""

# Name the variables meaningfully
total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min

# Name the variables meaningfully
total_hours = total_min / 60 # Total length of albums in hours 
total_hours


"""In the cells above we added the length of three albums in minutes and 
stored it in total_min. We then divided it by 60 to calculate total length 
total_hours in hours. You can also do it all at once in a single expression, 
as long as you use parenthesis to add the albums length before you divide, as 
shown below."""

# Complicate expression
total_hours = (43 + 42 + 57) // 60  # Total hours in a single expression
total_hours


"""If you'd rather have total hours as an integer, you can of course replace 
the floating point division with integer division (i.e., //)."""

"""Exercise: Expression and Variables in Python
What is the value of x where x = 3 + 2 * 2"""

x = 3 + 2 * 2
x


"""What is the value of y where y = (3 + 2) * 2?"""

y = (3 + 2) * 2
y


"""What is the value of z where z = x + y?"""

z = x + y
z    
    

"""==============
String Operations
Welcome! This notebook will teach you about the string operations in the Python 
Programming Language. By the end of this notebook, you'll know the basics 
string operations in Python, including indexing, escape sequences and 
operations.

Table of Contents
What are Strings?
Indexing
- Negative Indexing
- Slicing
- Stride
- Concatenate Strings
Escape Sequences
String Operations
Quiz on Strings

What are Strings?
The following example shows a string contained within 2 quotation marks:"""

# Use quotation marks for defining string
"Michael Jackson"


"""We can also use single quotation marks:"""

# Use single quotation marks for defining string
'Michael Jackson'


"""A string can be a combination of spaces and digits:"""

# Digitals and spaces in string
'1 2 3 4 5 6 '


"""A string can also be a combination of special characters :"""

# Special characters in string
'@#2_#]&*^%$'


"""We can print our string using the print statement:"""

# Print the string
print("hello!")


"""We can bind or assign a string to another variable:"""

# Assign string to variable
Name = "Michael Jackson"
Name


"""==============
Indexing
It is helpful to think of a string as an ordered sequence. Each element in the 
sequence can be accessed using an index represented by the array of numbers:

The first index can be accessed as follows:

[Tip]: Because indexing starts at 0, it means the first index is on the index 0."""

# Print the first element in the string
​
print(Name[0])


"""We can access index 6:"""

# Print the element on index 6 in the string
print(Name[6])


"""Moreover, we can access the 13th index:"""

# Print the element on the 13th index in the string
print(Name[13])


"""Negative Indexing
We can also use negative indexing with strings:

Negative index can help us to count the element from the end of the string.

The last element is given by the index -1:"""

# Print the last element in the string
print(Name[-1])


"""The first element can be obtained by index -15:"""

# Print the first element in the string
print(Name[-15])


"""We can find the number of characters in a string by using len, short for 
length:"""

# Find the length of string
len("Michael Jackson")


"""================
Slicing
We can obtain multiple characters from a string using slicing, we can obtain 
the 0 to 4th and 8th to the 12th element:

[Tip]: When taking the slice, the first number means the index (start at 0), 
and the second number means the length from the index to the last element you 
want (start at 1)"""

# Take the slice on variable Name with only index 0 to index 3
Name[0:4]

# Take the slice on variable Name with only index 8 to index 11
Name[8:12]


"""================
Stride
We can also input a stride value as follows, with the '2' indicating that we 
are selecting every second variable:"""

# Get every second element. The elments on index 1, 3, 5 ...
Name[::2]


"""We can also incorporate slicing with the stride. In this case, we select 
the first five elements and then use the stride:"""

# Get every second element in the range from index 0 to index 4
Name[0:5:2]


"""===============
Concatenate Strings
We can concatenate or combine strings by using the addition symbols, and the 
result is a new string that is a combination of both:"""

# Concatenate two strings
Statement = Name + "is the best"
Statement


"""To replicate values of a string we simply multiply the string by the number 
of times we would like to replicate it. In this case, the number is three. 
The result is a new string, and this new string consists of three copies of 
the original string:"""

# Print the string for 3 times
3 * "Michael Jackson"
# ---> 'Michael JacksonMichael JacksonMichael Jackson'


"""You can create a new string by setting it to the original variable. 
Concatenated with a new string, the result is a new string that changes from 
Michael Jackson to “Michael Jackson is the best".""""

# Concatenate strings
Name = "Michael Jackson"
Name = Name + " is the best"
Name


"""==================
Escape Sequences
Back slashes represent the beginning of escape sequences. Escape sequences 
represent strings that may be difficult to input. For example, back slash "n" 
represents a new line. The output is given by a new line after the back slash 
"n" is encountered:"""

# New line escape sequence
print(" Michael Jackson \n is the best" )


"""Similarly, back slash "t" represents a tab:"""

# Tab escape sequence
print(" Michael Jackson \t is the best" )


"""If you want to place a back slash in your string, use a double back slash:"""

# Include back slash in string
print(" Michael Jackson \\ is the best" )


"""We can also place an "r" before the string to display the backslash:"""

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )


"""================
String Operations
There are many string operation methods in Python that can be used to 
manipulate the data. We are going to use some basic string operations on the 
data.

Let's try with the method upper; this method converts lower case characters 
to upper case characters:"""

# Convert all the characters in string to upper case
A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)


"""The method replace replaces a segment of the string, i.e. a substring with 
a new string. We input the part of the string we would like to change. The 
second argument is what we would like to exchange the segment with, and the 
result is a new string with the segment changed:"""

# Replace the old substring with the new target substring is the segment has 
#been found in the string
A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B


"""The method find finds a sub-string. The argument is the substring you would 
like to find, and the output is the first index of the sequence. We can find 
the sub-string jack or el. """ 

# Find the substring in the string. Only the index of the first elment of 
# substring in string will be the output
Name = "Michael Jackson"
Name.find('el')


# Find the substring in the string.
Name.find('Jack')


"""If the sub-string is not in the string then the output is a negative one. 
For example, the string 'Jasdfasdasdf' is not a substring:"""

# If cannot find the substring in the string
Name.find('Jasdfasdasdf')


"""===============
Quiz on Strings
What is the value of the variable A after the following code is executed?"""

# Write your code below and press Shift+Enter to execute 
A = "1"
"1"


"""What is the value of the variable B after the following code is executed?"""

# Write your code below and press Shift+Enter to execute
B = "2"
"2"


"""What is the value of the variable C after the following code is executed?"""

# Write your code below and press Shift+Enter to execute 
C = A + B
C

"""Consider the variable D use slicing to print out the first three elements:"""

# Write your code below and press Shift+Enter to execute
D = "ABCDEFG"
D[:3]


"""Use a stride value of 2 to print out every second character of the string E:"""

# Write your code below and press Shift+Enter to execute
E = 'clocrkr1e1c1t'
E[::2]
# ---> 'correct'


"""Print out a backslash:"""
print("\\")
print(r" \ ")
# ---> \
# --->  \ 


"""Convert the variable F to uppercase:"""

# Write your code below and press Shift+Enter to execute
F = "You are wrong"
F.upper()
'YOU ARE WRONG'


"""Consider the variable G, and find the first index of the sub-string snow:"""

# Write your code below and press Shift+Enter to execute
G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
G.find("snow")
# ---> 95


"""In the variable G, replace the sub-string Mary with Bob:"""

G.replace("Mary", "Bob")




