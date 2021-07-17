#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:54:50 2020

@author: phuongdaingo
"""

"""Conditions in Python
Welcome! This notebook will teach you about the condition statements in the 
Python Programming Language. By the end of this lab, you'll know how to use the 
condition statements in Python, including operators, and branching.

Table of Contents
Condition Statements
Comparison Operators
Branching
Logical operators
Quiz on Condition Statement

Condition Statements
Comparison Operators

Comparison operations compare some value or operand and, based on a condition, 
they produce a Boolean. When comparing two values you can use these operators:

equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=

Let's assign a a value of 5. Use the equality operator denoted with 
two equal == signs to determine if two values are equal. The case below 
compares the variable a with 6."""

# Condition Equal
a = 5
a == 6
# ---> False


"""=================
The result is False, as 5 does not equal to 6.

Consider the following equality comparison operator i > 5. If the value of the 
left operand, in this case the variable i, is greater than the value of the 
right operand, in this case 5, then the statement is True. Otherwise, the 
statement is False. If i is equal to 6, because 6 is larger than 5, the output 
is True."""

# Greater than Sign
i = 6
i > 5
# ---> True


"""Set i = 2. The statement is false as 2 is not greater than 5:"""

# Greater than Sign
i = 2
i > 5
# ---> False


""""===================
Lets display some values for i in the figure. Set the values greater than 
5 in green and the rest in red. The green region represents where the condition 
is True, the red where the statement is False. If the value of i is 2, we get 
False as the 2 falls in the red region. Similarly, if the value for i is 6 we 
get a True as the condition falls in the green region.

The inequality test uses an exclamation mark preceding the equal sign, if two 
operands are not equal then the condition becomes True. For example, the 
following condition will produce True as long as the value of i is not equal 
to 6:"""

# Inequality Sign
i = 2
i != 6
True


"""When i equals 6 the inequality expression produces False."""

# Inequality Sign
i = 6
i != 6
# ---> False


"""===================
See the number line below. when the condition is True the corresponding 
numbers are marked in green and for where the condition is False the 
corresponding number is marked in red. If we set i equal to 2 the operator 
is true as 2 is in the green region. If we set i equal to 6, we get a False as 
the condition falls in the red region.

We can apply the same methods on strings. For example, use an equality operator 
on two different strings. As the strings are not equal, we get a False."""

# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson"
# ---> False


"""If we use the inequality operator, the output is going to be True as the 
strings are not equal."""

# Use Inequality sign to compare the strings
"ACDC" != "Michael Jackson"
# --> True


"""===================
Inequality operation is also used to compare the letters/words/symbols 
according to the ASCII value of letters. The decimal value shown in the 
following table represents the order of the character:

For example, the ASCII code for ! is 21, while the ASCII code for + is 43. 
Therefore + is larger than ! as 43 is greater than 21.

Similarly, the value for A is 101, and the value for B is 102 therefore:"""

# Compare characters
'B' > 'A'
# ---> True


"""When there are multiple letters, the first letter takes precedence in ordering:"""

# Compare characters
'BA' > 'AB'
# ---> True


"""Note: Upper Case Letters have different ASCII code than Lower Case Letters, 
which means the comparison between the letters in python is case-sensitive."""


"""===================
Branching
Branching allows us to run different statements for different inputs. It is 
helpful to think of an if statement as a locked room, if the statement is True 
we can enter the room and your program will run some predefined tasks, but if 
the statement is False the program will ignore the task.

For example, consider the blue rectangle representing an ACDC concert. If the 
individual is older than 18, they can enter the ACDC concert. If they are 18 or 
younger than 18 they cannot enter the concert.

Use the condition statements learned before as the conditions need to be checked 
in the if statement. The syntax is as simple as  if condition statement :, which 
contains a word if, any condition statement, and a colon at the end. Start your 
tasks which need to be executed under this condition in a new line with an indent. The lines of code after the colon and with an indent will only be executed when the if statement is True. The tasks will end when the line of code does not contain the indent.

In the case below, the tasks executed print(“you can enter”) only occurs if the
 variable age is greater than 18 is a True case because this line of code has 
 the indent. However, the execution of print(“move on”) will not be influenced 
 by the if statement."""

# If statement example
​
age = 19
#age = 18
​
#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
​
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")



"""===================
Try uncommenting the age variable

It is helpful to use the following diagram to illustrate the process. 
On the left side, we see what happens when the condition is True. 
The person enters the ACDC concert representing the code in the indent being 
executed; they then move on. On the right side, we see what happens when the 
condition is False; the person is not granted access, and the person moves on. 
In this case, the segment of code in the indent does not run, but the rest of 
the statements are run.

The else statement runs a block of code if none of the conditions are True 
before this else statement. Lets use the ACDC concert analogy again. 
If the user is 17 they cannot go to the ACDC concert, but they can go to the 
Meatloaf concert. The syntax of the else statement is similar as the syntax of 
the if statement, as else :. Notice that, there is no condition statement for else. Try changing the values of age to see what happens:
==================="""

# Else statement example
age = 18
# age = 19
​
if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


"""===================
The process is demonstrated below, where each of the possibilities is 
illustrated on each side of the image. On the left is the case where the age 
is 17, we set the variable age to 17, and this corresponds to the individual 
attending the Meatloaf concert. The right portion shows what happens when the 
individual is over 18, in this case 19, and the individual is granted access 
to the concert.

The elif statement, short for else if, allows us to check additional conditions 
if the condition statements before it are False. If the condition for the elif 
statement is True, the alternate expressions will be run. Consider the concert 
example, where if the individual is 18 they will go to the Pink Floyd concert 
instead of attending the ACDC or Meat-loaf concert. The person of 18 years of 
age enters the area, and as they are not older than 18 they can not see ACDC, 
but as they are 18 years of age, they attend Pink Floyd. After seeing Pink 
Floyd, they move on. The syntax of the elif statement is similar in that we 
merely change the if in if statement to elif."""

# Elif statment example
age = 18
​
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


"""================
The three combinations are shown in the figure below. The left-most region 
shows what happens when the individual is less than 18 years of age. The 
central component shows when the individual is exactly 18. The rightmost shows 
when the individual is over 18.

Look at the following code:"""

# Condition statement example
album_year = 1983
album_year = 1970
​
if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


"""================
Feel free to change album_year value to other values -- you'll see that the 
result changes!

Notice that the code in the above indented block will only be executed if the 
results are True.

As before, we can add an else block to the if block. The code in the else block
 will only be executed if the result is False.

***Syntax:

if (condition): # do something else: # do something else

If the condition in the if statement is False, the statement after the else 
block will execute. This is demonstrated in the figure:"""

# Condition statement example
album_year = 1983
#album_year = 1970
​
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
​
print('do something..')


"""===============
Feel free to change the album_year value to other values -- you'll see that 
the result changes based on it!

Logical operators
Sometimes you want to check more than one condition at once. For example, 
you might want to check if one condition and another condition is True. 
Logical operators allow you to combine or modify conditions.

and
or
not

These operators are summarized for two variables using the following truth tables:

The and statement is only True when both conditions are true. The or statement 
is true if one condition is True. The not statement outputs the opposite truth 
value.

Let's see how to determine if an album was released after 1979 (1979 is not 
included) and before 1990 (1990 is not included). The time periods between 1980 
and 1989 satisfy this condition. This is demonstrated in the figure below. The 
green on lines a and b represents periods where the statement is True. The green 
on line c represents where both conditions are True, this corresponds to where 
the green regions overlap.

The block of code to perform this check is given by:"""

# Condition statement example
album_year = 1980
​
if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


"""================
To determine if an album was released before 1980 (~ - 1979) or 
after 1989 (1990 - ), an or statement can be used. Periods before 1980 ( - 1979) 
or after 1989 (1990 - ~) satisfy this condition. This is demonstrated in the 
following figure, the color green in a and b represents periods where the 
statement is true. The color green in c represents where at least one of the 
conditions are true.

The block of code to perform this check is given by:"""

# Condition statement example
album_year = 1990
​
if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


"""The not statement checks if the statement is false:"""

# Condition statement example
album_year = 1983
​
if not (album_year == '1984'):
    print ("Album year is not 1984")


"""===============
*** Quiz on Conditions

Write an if statement to determine if an album had a rating greater than 8. 
Test it using the rating for the album “Back in Black” that had a rating of 8.5. 
If the statement is true print "This album is Amazing!" """

rating = 8.5 
if rating > 8:
    print("This album is Amazing!")


""" Write an if-else statement that performs the following. If the rating is 
larger then eight print “this album is amazing”. If the rating is less than or 
equal to 8 print “this album is ok”. """

rating = 8.5
if rating > 8:
    print("this album is amazing")
else:
    print("this album is ok")


"""Write an if statement to determine if an album came out before 1980 or in 
the years: 1991 or 1993. If the condition is true print out the year the album 
came out."""

album_year = 1979
if album_year < 1980 or album_year == 1991 or album_year == 1993:
    print("this album came out already")



"""=====================================
Loops in Python
Welcome! This notebook will teach you about the loops in the Python Programming 
Language. By the end of this lab, you'll know how to use the loop statements in 
Python, including for loop, and while loop.

Table of Contents
Loops
Range
What is for loop?
What is while loop?
Quiz on Loops

Loops
Range
Sometimes, you might want to repeat a given operation many times. Repeated 
executions like this are performed by loops. We will look at two types of loops, 
for loops and while loops.

Before we discuss loops lets discuss the range object. It is helpful to think 
of the range object as an ordered list. For now, let's look at the simplest case. 
If we would like to generate a sequence that contains three elements ordered 
from 0 to 2 we simply use the following command:"""

# Use the range
range(3)


"""What is for loop?
The for loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.
Let's try to use a for loop to print all the years presented in the list dates:

This can be done as follows:"""

# For loop example
dates = [1982,1980,1973]
N = len(dates)
​
for i in range(N):
    print(dates[i])     


"""The code in the indent is executed N times, each time the value of i is 
increased by 1 for every execution. The statement executed is to print out 
the value in the list at index i as shown here:

In this example we can print out a sequence of numbers from 0 to 7:"""

# Example of for loop
for i in range(0, 8):
    print(i)


"""In Python we can directly access the elements in the list as follows:"""

# Exmaple of for loop, loop through list
for year in dates:  
    print(year)   


"""For each iteration, the value of the variable years behaves like the value 
of dates[i] in the first example:

We can change the elements in a list:"""

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
​
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])


"""We can access the index and the elements of a list as follows:"""

# Loop through the list and iterate on both index and element value
​
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)
    
    
"""==============
What is while loop?
As you can see, the for loop is used for a controlled flow of repetition. 
However, what if we don't know when we want to stop the loop? What if we want 
to keep executing a code block until a certain condition is met? The while loop 
exists as a tool for repeated execution based on a condition. The code block will 
keep being executed until the given logical condition returns a False boolean 
value.

Let’s say we would like to iterate through list dates and stop at the year 1973,
then print out the number of iterations. This can be done with the following 
block of code:"""

# While Loop Example
dates = [1982, 1980, 1973, 2000]
​
i = 0
year = 0
​
while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)
​
print("It took ", i ,"repetitions to get out of loop.")


"""A while loop iterates merely until the condition in the argument is not met, 
as shown in the following figure:"""


"""===============
Quiz on Loops

Write a for loop the prints out all the element between -5 and 5 using the 
range function."""

# Write your code below and press Shift+Enter to execute
for i in range(-5, 6):
    print(i)


"""Print the elements of the following list: 
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 
Make sure you follow Python conventions."""

# Write your code below and press Shift+Enter to execute
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)


"""Write a for loop that prints out the following list: 
squares=['red', 'yellow', 'green', 'purple', 'blue'] """

# Write your code below and press Shift+Enter to execute
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)


"""Write a while loop to display the values of the Rating of an album playlist 
stored in the list PlayListRatings. If the score is less than 6, exit the loop. 
The list PlayListRatings is given by: 
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10] """

# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1


"""Write a while loop to copy the strings 'orange' of the list squares to the 
list new_squares. Stop and exit the loop if the value on the list is not 'orange':"""

# Write your code below and press Shift+Enter to execute
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)


"""=============
For Loops 
Use loops to print out the elements in the list A"""

A=[1,2,3,4,5]
print(A)


"""=============
While Loops
Find the value of  x  that will print out the sequence  1,2,..,10 """

x=11
y=1
while(y< x):
    print(y)
    y=y+1
    
    
"""================================================================
Functions in Python
Welcome! This notebook will teach you about the functions in the Python 
Programming Language. By the end of this lab, you'll know the basic concepts 
about function, variables, and how to use functions.

Table of Contents
Functions
- What is a function?
- Variables
- Functions Make Things Simple
Pre-defined functions
Using if/else Statements and Loops in Functions
Setting default argument values in your custom functions
Global variables
Scope of a Variable
Quiz on Loops

Functions
A function is a reusable block of code which performs operations specified 
in the function. They let you break down tasks and allow you to reuse your code 
in different programs.

There are two types of functions :
- Pre-defined functions
- User defined functions

What is a Function?
You can define functions to provide the required functionality. Here are simple 
rules to define a function in Python:

Functions blocks begin def followed by the function name and parentheses ().
There are input parameters or arguments that should be placed within these 
parentheses.
You can also define parameters inside these parentheses.
There is a body within every function that starts with a colon (:) and is indented.
You can also place documentation before the body
The statement return exits a function, optionally passing back a value
An example of a function that adds on to the parameter a prints and returns the 
output as b:"""

# First function example: Add 1 to a and store as b
def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)


"""The figure below illustrates the terminology:

We can obtain help about a function :"""

# Get a help on add function
help(add)


"""We can call the function:"""

# Call the function add()
add(1)


"""If we call the function with a new input we get a new result:"""

# Call the function add()
add(2)

"""We can create different functions. For example, we can create a function 
that multiplies two numbers. The numbers will be represented by the variables 
a and b:"""

# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    
    
"""The same function can be used for different data types. For example, we can 
multiply two integers:"""

# Use mult() multiply two integers
Mult(2, 3)


"""Two Floats:"""

# Use mult() multiply two floats
Mult(10.0, 3.14)


"""We can even replicate a string by multiplying with an integer:"""

# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")


"""================
Variables
The input to a function is called a formal parameter.

A variable that is declared inside a function is called a local variable. 
The parameter only exists within the function (i.e. the point where the 
function starts and stops).

A variable that is declared outside a function definition is a global variable, 
and its value is accessible and modifiable throughout the program. We will 
discuss more about global variables at the end of the lab."""

# Function Definition
def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


"""The labels are displayed in the figure:

We can call the function with an input of 3:"""

# Initializes Global variable  
x = 3

# Makes function call and return function a y
y = square(x)
y


"""We can call the function with an input of 2 in a different manner:"""

# Directly enter a number as parameter
square(2)


"""If there is no return statement, the function returns None. The following 
two functions are equivalent:"""

# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output
MJ()

# See the output
MJ1()


"""Printing the function after a call reveals a None is the default return 
statement:"""

# See what functions returns are
print(MJ())
print(MJ1())


"""Create a function con that concatenates two strings using the addition 
operation:"""

# Define the function for combining strings
def con(a, b):
    return(a + b)
    
# Test on the con() function
con("This ", "is")


"""[Tip] How do I learn more about the pre-defined functions in Python? 

We will be introducing a variety of pre-defined functions to you as you learn 
more about Python. There are just too many functions, so there's no way we can 
teach them all in one sitting. But if you'd like to take a quick peek, here's 
a short reference card for some of the commonly-used pre-defined functions: Reference


==================
Functions Make Things Simple
Consider the two lines of code in Block 1 and Block 2: the procedure for each 
block is identical. The only thing that is different is the variable names and 
values.

Block 1:"""

# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   


"""Block 2:"""

# a and b calculation block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   


"""We can replace the lines of code with a function. A function combines many 
instructions into a single line of code. Once a function is defined, it can be 
used repeatedly. You can invoke the same function many times in your program. 
You can save your function and use it in another program or use someone else’s 
function. The lines of code in code Block 1 and code Block 2 can be replaced 
by the following function:"""

# Make a Function for the calculation above
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


"""This function takes two inputs, a and b, then applies several operations to 
return c. We simply define the function, replace the instructions with the 
function, and input the new values of a1, b1 and a2, b2 as inputs. The entire 
process is demonstrated in the figure:

Code Blocks 1 and Block 2 can now be replaced with code Block 3 and code Block 4.

Block 3:"""

a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1


"""Block 4:"""
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2


"""=================
Pre-defined functions
There are many pre-defined functions in Python, so let's start with the 
simple ones.

The print() function:"""

# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


"""The sum() function adds all the elements in a list or tuple:"""

# Use sum() to add every element in a list or tuple together
sum(album_ratings)


"""The len() function returns the length of a list or tuple:"""

# Show the length of the list or tuple
len(album_ratings)


"""Using if/else Statements and Loops in Functions
The return() function is particularly useful if you have any IF statements 
in the function, when you want your output to be dependent on some condition:"""

# Function example
def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


"""We can use a loop in a function. For example, we can print out each element 
in a list:"""

# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)


# Implement the printlist function​
PrintList(['1', 1, 'the man', "abc"])


"""Setting default argument values in your custom functions
You can set a default value for arguments in your function. For example, in the 
isGoodRating() function, what if we wanted to create a threshold for what we 
consider to be a good rating? Perhaps by default, we should have a default 
rating of 4:"""

# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)
​

# Test the value with default value and with input
isGoodRating()
isGoodRating(10)


"""====================
Global variables
So far, we've been creating variables within functions, but we have not 
discussed variables outside the function. These are called global variables.
Let's try to see what printer1 returns:"""

# Example of global variable
artist = "Michael Jackson"
def printer1(artist):
    internal_var = artist
    print(artist, "is an artist")
    
printer1(artist)


"""If we print internal_var we get an error.

We got a Name Error: name 'internal_var' is not defined. Why?

It's because all the variables we create in the function is a local variable, 
meaning that the variable assignment does not persist outside the function.

But there is a way to create global variables from within a function as follows:"""

artist = "Michael Jackson"
​
def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")
​
printer(artist) 
printer(internal_var)


"""=====================
Scope of a Variable
The scope of a variable is the part of that program where that variable is 
accessible. Variables that are declared outside of all function definitions, 
such as the myFavouriteBand variable in the code shown here, are accessible 
from anywhere within the program. As a result, such variables are said to have 
global scope, and are known as global variables. myFavouriteBand is a global 
variable, so it is accessible from within the getBandRating function, and we 
can use it to determine a band's rating. We can also use it outside of the 
function, such as when we pass it to the print function to display it:"""

# Example of global variable
myFavouriteBand = "AC/DC"
​
def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
​
print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


"""Take a look at this modified version of our code. Now the myFavouriteBand 
variable is defined within the getBandRating function. A variable that is 
defined within a function is said to be a local variable of that function. 
That means that it is only accessible from within the function in which it is 
defined. Our getBandRating function will still work, because myFavouriteBand 
is still defined within the function. However, we can no longer print 
myFavouriteBand outside our function, because it is a local variable of our 
getBandRating function; it is only defined within the getBandRating function:"""

# Example of local variable
def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
​
print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


"""===================
Finally, take a look at this example. We now have two myFavouriteBand 
variable definitions. The first one of these has a global scope, and the 
second of them is a local variable within the getBandRating function. Within 
the getBandRating function, the local variable takes precedence. Deep Purple 
will receive a rating of 10.0 when passed to the getBandRating function. 
However, outside of the getBandRating function, the getBandRating s local 
variable is not defined, so the myFavouriteBand variable we print is the 
global variable, which has a value of AC/DC:"""

# Example of global variable and local variable with the same name
myFavouriteBand = "AC/DC"
​
def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0
​
print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


"""===================
Quiz on Functions

Come up with a function that divides the first input by the second input:"""
# Write your code below and press Shift+Enter to execute
def div(a, b):
    return(a/b)


"""Use the function con for the following question."""
# Use the con function for the following question
def con(a, b):
    return(a + b)
    
    
"""Can the con function we defined before be used to add to integers or strings?"""
# Write your code below and press Shift+Enter to execute
yes, for example: 
con(2, 2)


"""Can the con function we defined before be used to concentrate a list or tuple?"""
# Write your code below and press Shift+Enter to execute
yes,for example: 
con(['a', 1], ['b', 1])


"""===============
Function
Complete the function  f  so that it returns the product of  a  and  b  , 
you the next cell to test the function"""
def f(a,b):
    return 


"""Test the function using the next cell:"""
a=4
b=2
if a*b==f(a,b):   
    print("correct")   
else:    
    print("incorrect")


"""Complete the function  g  such that the input  c  is a list of integers and 
the output is the sum of all the elements in the list"""
def g(c):
    return 


"""Test the function using the next cell:"""
c=[1,2,3,4,5]
if sum(c)==g(c):   
    print("correct")   
else:    
    print("incorrect")

    
"""=========================================
Classes and Objects in Python
Welcome! Objects in programming are like objects in real life. Like life, 
there are different classes of objects. In this notebook, we will create two 
classes called Circle and Rectangle. By the end of this notebook, you will 
have a better idea about :

what a class is
what an attribute is
what a method is
Don’t worry if you don’t get it the first time, as much of the terminology is 
confusing. Don’t forget to do the practice tests in the notebook.

Table of Contents

Introduction to Classes and Objects
- Creating a class
- Instances of a Class: Objects and Attributes
- Methods
Creating a class
Creating an instance of a class Circle
The Rectangle Class

Introduction to Classes and Objects
Creating a Class
The first part of creating a class is giving it a name: In this notebook, 
we will create two classes, Circle and Rectangle. We need to determine all the 
data that make up that class, and we call that an attribute. Think about this 
step as creating a blue print that we will use to create objects. In figure 1 
we see two classes, circle and rectangle. Each has their attributes, they are 
variables. The class circle has the attribute radius and color, while the 
rectangle has the attribute height and width. Let’s use the visual examples of 
these shapes before we get to the code, as this will help you get accustomed to 
the vocabulary.

Figure 1: Classes circle and rectangle, and each has their own attributes. The 
class circle has the attribute radius and colour, the rectangle has the 
attribute height and width.

Instances of a Class: Objects and Attributes
An instance of an object is the realisation of a class, and in Figure 2 we see 
three instances of the class circle. We give each object a name: red circle, 
yellow circle and green circle. Each object has different attributes, so let's 
focus on the attribute of colour for each object.

Figure 2: Three instances of the class circle or three objects of type circle.

The colour attribute for the red circle is the colour red, for the green circle 
object the colour attribute is green, and for the yellow circle the colour 
attribute is yellow.

Methods
Methods give you a way to change or interact with the object; they are functions 
that interact with objects. For example, let’s say we would like to increase 
the radius by a specified amount of a circle. We can create a method called 
add_radius(r) that increases the radius by r. This is shown in figure 3, where 
after applying the method to the "orange circle object", the radius of the 
object increases accordingly. The “dot” notation means to apply the method to 
the object, which is essentially applying a function to the information in the 
object.

Figure 3: Applying the method “add_radius” to the object orange circle object.

Creating a Class
Now we are going to create a class circle, but first, we are going to import a 
library to draw the objects:"""

# Import the library
import matplotlib.pyplot as plt
%matplotlib inline  


"""The first step in creating your own class is to use the class keyword, 
then the name of the class as shown in Figure 4. In this course the class 
parent will always be object:

Figure 4: Three instances of the class circle or three objects of type circle.

The next step is a special method called a constructor __init__, which is used 
to initialize the object. The input are data attributes. The term self contains 
all the attributes in the set. For example the self.color gives the value of 
the attribute color and self.radius will give you the radius of the object. 
We also have the method add_radius() with the parameter r, the method adds the 
value of r to the attribute radius. To access the radius we use the syntax 
self.radius. The labeled syntax is summarized in Figure 5:

Figure 5: Labeled syntax of the object circle.

The actual object is shown below. We include the method drawCircle to display 
the image of a circle. We set the default radius to 3 and the default colour 
to blue:"""

# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
        
        
"""=================
Creating an instance of a class Circle
Let’s create the object RedCircle of type Circle to do the following:"""

# Create an object RedCircle
RedCircle = Circle(10, 'red')


"""We can use the dir command to get a list of the object's methods. Many of 
them are default Python methods."""

# Find out the methods can be used on the object RedCircle
dir(RedCircle)


"""We can look at the data attributes of the object:"""

# Print the object attribute radius
RedCircle.radius

# Print the object attribute color
RedCircle.color


"""We can change the object's data attributes:"""

# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius


"""We can draw the object by using the method drawCircle():"""

# Call the method drawCircle
RedCircle.drawCircle()


"""We can increase the radius of the circle by applying the method add_radius(). 
Let increases the radius by 2 and then by 5:"""

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',
      RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',
      RedCircle.radius)


"""Let’s create a blue circle. As the default colour is blue, all we have to do 
is specify what the radius is:"""

# Create a blue circle with a given radius
​
BlueCircle = Circle(radius=100)


"""As before we can access the attributes of the instance of the class by 
using the dot notation:"""

# Print the object attribute radius
BlueCircle.radius

# Print the object attribute color
BlueCircle.color


"""We can draw the object by using the method drawCircle():"""

# Call the method drawCircle
BlueCircle.drawCircle()


"""Compare the x and y axis of the figure to the figure for RedCircle; they 
are different."""


"""=======================
The Rectangle Class
Let's create a class rectangle with the attributes of height, width and color. 
We will only add the method to draw the rectangle object:"""

# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


"""Let’s create the object SkinnyBlueRectangle of type Rectangle. Its width 
will be 2 and height will be 3, and the color will be blue:"""
# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 10, 'blue')


"""As before we can access the attributes of the instance of the class by using 
the dot notation:"""
# Print the object attribute height
SkinnyBlueRectangle.height 

# Print the object attribute width
SkinnyBlueRectangle.width

# Print the object attribute color
SkinnyBlueRectangle.color


"""We can draw the object:"""
# Use the drawRectangle method to draw the shape
SkinnyBlueRectangle.drawRectangle()


"""Let’s create the object FatYellowRectangle of type Rectangle :"""
# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')


"""We can access the attributes of the instance of the class by using the dot 
notation:"""
# Print the object attribute height
FatYellowRectangle.height 

# Print the object attribute width
FatYellowRectangle.width

# Print the object attribute color
FatYellowRectangle.color


"""We can draw the object:"""
# Use the drawRectangle method to draw the shape
FatYellowRectangle.drawRectangle()


"""=============
You will need the class Car for the next exercises. 
The class Car has four data attributes: make, model, colour and number of 
owners (owner_number). The method  car_info()  prints out the data attributes 
and the method sell() increments the number of owners."""

class Car(object):
    def __init__(self,make,model,color):
        self.make=make;
        self.model=model;
        self.color=color;
        self.owner_number=0 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number=self.owner_number+1
        

"""==============
Create a Car object 
Create a  Car  object my_car with the given data attributes:"""

make="BMW"
model="M3"
color="red"
my_car = Car(make, model, color)


"""=============
Data Attributes 
Use the method car_info() to print out the data attributes"""

car_info = print(my_car)
# ---> <__main__.Car object at 0x7fee7012e160>


"""============
Methods 
Call the method  sell()  in the loop, then call the method  car_info() again"""

for i in range(5):
    my_car.sell()
    my_car.car_info()
    
​