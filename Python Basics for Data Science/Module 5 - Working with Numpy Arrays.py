#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:38:48 2020

@author: phuongdaingo

Library
NumPy: https://numpy.org/

"""

"""====================
Get to Know a numpy Array 
cast the following list to a numpy array:"""

import numpy as np
a=[1,2,3,4,5]
A=np.array(a)
A
​# ---> array([1, 2, 3, 4, 5])


"""1) type using the function type"""
type(A)
# ---> numpy.ndarray


"""2) the shape of the array"""
A.shape
# ---> (5,)


"""3) the type of data in the array"""
A.dtype
# ---> dtype('int64')


"""4) find the mean of the array"""
mean_A = A.mean()
mean_A
# ---> 3.0


"""=================
Creating and Plotting Functions 

1) create the following functions using the numpy array  x """
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)+2
y

"""2) plot the function"""
import matplotlib.pyplot as plt
%matplotlib inline  
plt.plot(x,y)


"""QUESTION 1
What is the result of the following operation?"""
np.array([1,-1])*np.array([1,1])
# ---> array([ 1, -1])

"""QUESTION 2
What is the result of the following operation? """
np.dot(np.array([1,-1]),np.array([1,1]))
# ---> 0
​    
"""==================
1D Numpy in Python
Welcome! This notebook will teach you about using Numpy in the Python 
Programming Language. By the end of this lab, you'll know what Numpy is and 
the Numpy operations.

Table of Contents
Preparation
What is Numpy?
- Type
- Assign Value
- Slicing
- Assign Value with List
- Other Attributes
Numpy Array Operations
- Array Addition
- Array Multiplication
- Product of Two Numpy Arrays
- Dot Product
- Adding Constant to a Numpy Array
Mathematical Functions
Linspace

Preparation"""

# Import the libraries
import time 
import sys
import numpy as np 
​
import matplotlib.pyplot as plt
%matplotlib inline  

# Plotting functions​
def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
       

"""Create a Python List as follows:""" 

# Create a python list
a = ["0", 1, "two", "3", 4]

"""=================
We can access the data via an index: Image
We can access each element using a square bracket as follows:"""

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


"""===============================================
What is Numpy?
A numpy array is similar to a list. It's usually fixed in size and each 
element is of the same type. We can cast a list to a numpy array by first 
importing numpy:"""

# import numpy library
import numpy as np 


"""We then cast the list as follows: """
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a


"""Each element is of the same type, in this case integers: Image
As with lists, we can access each element via a square bracket:"""

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


""" =================
Type
If we check the type of the array we get numpy.ndarray:"""
# Check the type of the array
type(a)


"""As numpy arrays contain data of the same type, we can use the attribute 
"dtype" to obtain the Data-type of the array’s elements. In this case a 
64-bit integer:"""
# Check the type of the values stored in numpy array
a.dtype


"""We can create a numpy array with real numbers:"""
# Create a numpy array
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])


"""When we check the type of the array we get numpy.ndarray:"""
# Check the type of array
type(b)


"""If we examine the attribute dtype we see float 64, as the elements are 
not integers:"""
# Check the value type
b.dtype


"""===================
Assign value
We can change the value of the array, consider the array c:"""
# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c


"""We can change the first element of the array to 100 as follows:"""
# Assign the first element to 100
c[0] = 100
c


"""We can change the 5th element of the array to 0 as follows:"""
# Assign the 5th element to 0
c[4] = 0
c


"""====================
Slicing
Like lists, we can slice the numpy array, and we can select the elements 
from 1 to 3 and assign it to a new numpy array d as follows:"""
# Slicing the numpy array
d = c[1:4]
d


"""We can assign the corresponding indexes to new values as follows:"""
# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c


"""====================
Assign Value with List
Similarly, we can use a list to select a specific index. The list ' select ' 
contains several values:"""
# Create the index list
select = [0, 2, 3]


"""We can use the list as an argument in the brackets. The output is the 
elements corresponding to the particular index:"""
# Use List to select elements
d = c[select]
d


"""We can assign the specified elements to a new value. For example, we can 
assign the values to 100 000 as follows:"""
# Assign the specified elements to new value
c[select] = 100000
c


"""===================
Other Attributes
Let's review some basic array attributes using the array a:"""
# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a


"""The attribute size is the number of elements in the array:"""
# Get the size of numpy array
a.size


"""The next two attributes will make more sense when we get to higher 
dimensions but let's review them. The attribute ndim represents the number 
of array dimensions or the rank of the array, in this case, one:"""
# Get the number of dimensions of numpy array
a.ndim


"""The attribute shape is a tuple of integers indicating the size of the 
array in each dimension:"""
# Get the shape/size of numpy array
a.shape

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
mean

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array
max_b = b.max()
max_b

# Get the smallest value in the numpy array
min_b = b.min()
min_b


"""==================
Numpy Array Operations
Array Addition
Consider the numpy array u:"""
u = np.array([1, 0])
u

"""Consider the numpy array v:"""
v = np.array([0, 1])
v

"""We can add the two arrays and assign it to z:"""
# Numpy Array Addition
z = u + v
z

"""The operation is equivalent to vector addition:"""
# Plot numpy arrays
Plotvec1(u, z, v)


"""======================
Array Multiplication
Consider the vector numpy array y:"""
# Create a numpy array
y = np.array([1, 2])
y

"""We can multiply every element in the array by 2:"""
# Numpy Array Multiplication
z = 2 * y
z

"""This is equivalent to multiplying a vector by a scaler:

=======================
Product of Two Numpy Arrays

Consider the following array u:"""
# Create a numpy array
u = np.array([1, 2])
u

"""Consider the following array v:"""
# Create a numpy array
v = np.array([3, 2])
v

"""The product of the two numpy arrays u and v is given by:"""
# Calculate the production of two numpy arrays
z = u * v
z


"""====================
Dot Product
The dot product of the two numpy arrays u and v is given by:"""

# Calculate the dot product
np.dot(u, v)


"""===================
Adding Constant to a Numpy Array

Consider the following array:"""
# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
u

"""Adding the constant 1 to each element in the array:"""
# Add the constant to array
u + 1

"""The process is summarised in the following animation: Image


=======================
Mathematical Functions

We can access the value of pie in numpy as follows : """
# The value of pie
np.pi


"""We can create the following numpy array in Radians:"""
# Create the numpy array in radians
x = np.array([0, np.pi/2, np.pi])


"""We can apply the function sin to the array x and assign the values to 
the array y; this applies the sine function to each element in the array:"""
# Calculate the sin of each elements
y = np.sin(x)
y


"""====================
Linspace
A useful function for plotting mathematical functions is "linespace". 
Linespace returns evenly spaced numbers over a specified interval. 
We specify the starting point of the sequence and the ending point of 
the sequence. The parameter "num" indicates the Number of samples to 
generate, in this case 5:"""

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)


"""If we change the parameter num to 9, we get 9 evenly spaced numbers over 
the interval from -2 to 2:"""
# Makeup a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)


"""We can use the function line space to generate 100 evenly spaced samples 
from the interval 0 to 2π:"""
# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)


"""We can apply the sine function to each element in the array x and assign 
it to the array y:"""
# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)


"""========================
Quiz on 1D Numpy Array

Implement the following vector subtraction in numpy: u-v """
u = np.array([1, 0])
v = np.array([0, 1])
u - v


"""Multiply the numpy array z with -2:"""
t = np.array([2, 4])
-2 * t


"""Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1], and cast both lists 
to a numpy array then multiply them together:"""
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b


"""Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot 
the arrays as vectors using the fuction Plotvec2 and find the dot product:"""
a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))


"""Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the 
arrays as vectors using the function Plotvec2 and find the dot product:"""
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


"""Convert the list [1, 1] and [0, 1] to numpy arrays a and b. Then plot the 
arrays as vectors using the fuction Plotvec2 and find the dot product:"""
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


"""Why are the results of the dot product for [-1, 1] and [1, 1] and the dot 
product for [1, 0] and [0, 1] zero, but not zero for the dot product for 
[1, 1] and [0, 1]? 
Hint: Study the corresponding figures, pay attention to the direction the 
arrows are pointing to."""

---> The vectors used for question 4 and 5 are perpendicular (vuông góc). 
As a result, the dot product is zero. 


"""=================
Get to Know a numpy Array 
You will use the numpy array  A for the following"""

import numpy as np
A = np.array([[11,12],[21,22],[31,32]])
​
"""1) type using the function type"""
type(A)
# ---> numpy.ndarray

"""2) the shape of the array"""
A.shape
# ---> (3, 2)

"""3) the type of data in the array"""
A.dtype
# ---> dtype('int64')

"""4) Find the second row of the numpy array A:"""
A[1]
# ---> array([21, 22])


"""=================
Two kinds of Multiplying 
You will use the following numpy arrays for the next questions"""
A = np.array([[11,12],[21,22]])
B = np.array([[1, 0],[0,1]])

"""1) multiply array  A  and B"""
A*B
# ---> array([[11,  0],
            # [0, 22]])
    
"""2) plot the function"""
np.dot(A,B)
np.dot(B,A)
print(np.dot(A,B))

plt.plot(A,B)

A = np.array([[11,12],[21,22]])
B = np.array([[1, 0],[0,1]])
plt.plot(A,B)            
"""=================
QUESTION 1
How many rows is the following numpy array? """
A=np.array([[1,2],[3,4],[5,6],[7,8]])
# --> 4


"""QUESTION 2
How can you perform the following operation? """
A=np.array([[1,2],[3,4],[5,6],[7,8]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.dot(A,B)
# ---> NO


"""==========================================
2D Numpy in Python
Welcome! This notebook will teach you about using Numpy in the Python 
Programming Language. By the end of this lab, you'll know what Numpy is and 
the Numpy operations.

* Table of Contents
Create a 2D Numpy Array
Accessing different elements of a Numpy Array
Basic Operations

Create a 2D Numpy Array"""
# Import the libraries
import numpy as np 
import matplotlib.pyplot as plt


"""Consider the list a, the list contains three nested lists each of equal 
size."""
# Create a LIST
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a


"""We can cast the list to a Numpy Array as follow"""
# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A


"""We can use the attribute ndim to obtain the number of axes or dimensions 
referred to as the rank."""
# Show the numpy array dimensions
A.ndim


"""Attribute shape returns a tuple corresponding to the size or number of 
each dimension."""
# Show the numpy array shape
A.shape


"""The total number of elements in the array is given by the attribute size."""
# Show the numpy array size
A.size


"""======================
Accessing different elements of a Numpy Array
We can use rectangular brackets to access the different elements of the array.
The correspondence between the rectangular brackets and the list and the 
rectangular representation is shown in the following figure for a 3x3 array:

We can access the 2nd-row 3rd column as shown in the following figure:

We simply use the square brackets and the indices corresponding to the element 
we would like:"""
# Access the element on the second row and third column
A[1, 2]

"""We can also use the following notation to obtain the elements:"""
# Access the element on the second row and third column
A[1][2]

"""Consider the elements shown in the following figure

We can access the element as follows"""
# Access the element on the first row and first column
A[0][0]

""""We can also use slicing in numpy arrays. Consider the following figure. 
We would like to obtain the first two columns in the first row

This can be done with the following syntax"""
# Access the element on the first row and first and second columns
A[0][0:2]

"""Similarly, we can obtain the first two rows of the 3rd column as follows:"""
# Access the element on the first and second rows and third column
A[0:2, 2]


"""Corresponding to the following figure:
We can also add arrays. The process is identical to matrix addition. 
Matrix addition of X and Y is shown in the following figure:
The numpy array is given by X and Y"""
# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

"""We can add the numpy arrays as follows."""
# Add X and Y
Z = X + Y
Z


"""Multiplying a numpy array by a scaler is identical to multiplying a matrix
 by a scaler. If we multiply the matrix Y by the scaler 2, we simply multiply 
 every element in the matrix by 2 as shown in the figure.

We can perform the same operation in numpy as follows"""
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2
Z = 2 * Y
Z


"""Multiplication of two arrays corresponds to an element-wise product or 
Hadamard product. Consider matrix X and Y. The Hadamard product corresponds 
to multiplying each of the elements in the same position, i.e. multiplying 
elements contained in the same color boxes together. The result is a new 
matrix that is the same size as matrix Y or X, as shown in the following 
figure.

We can perform element-wise product of the array X and Y as follows:"""
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Multiply X with Y
Z = X * Y
Z


"""We can also perform matrix multiplication with the numpy arrays A and B as
follows:
     
First, we define matrix A and B:"""
# Create a matrix A
A = np.array([[0, 1, 1], [1, 0, 1]])
A

# Create a matrix B
B = np.array([[1, 1], [1, 1], [-1, 1]])
B

"""We use the numpy function dot to multiply the arrays together."""
# Calculate the dot product 
Z = np.dot(A,B)
Z

# Calculate the sin of Z
np.sin(Z)


"""We use the numpy attribute T to calculate the transposed matrix"""
# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C (hoán vị)
C.T




