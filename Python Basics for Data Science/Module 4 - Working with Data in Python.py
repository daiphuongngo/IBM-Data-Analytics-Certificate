#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:25:24 2020

@author: phuongdaingo
"""
"""
Reading Files Python
Welcome! This notebook will teach you about reading the text file in the 
Python Programming Language. By the end of this lab, you'll know how to read 
text files.

Table of Contents
Download Data
Reading Text Files
A Better Way to Open a File

==================
Download Data"""

# Download Example file
​
!wget -O /resources/data/Example1.txt https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/example1.txt


"""==============
Reading Text Files
One way to read or write a file in Python is to use the built-in open function. 
The open function provides a File object that contains the methods and attributes
 you need in order to read, save, and manipulate the file. In this notebook,
 we will only cover .txt files. The first parameter you need is the file path 
 and the file name. An example is shown as follow:

The mode argument is optional and the default value is r. In this notebook we 
only cover two modes:

r Read mode for reading files
w Write mode for writing files
For the next example, we will use the text file Example1.txt. The file is shown as follow:

We read the file:"""
# Read the Example1.txt
example1 = "/resources/data/Example1.txt"
file1 = open(example1, "r")


"""==============
We can view the attributes of the file.

The name of the file:"""
# Print the path of file
file1.name
'/resources/data/Example1.txt'


"""
The mode the file object is in:"""
# Print the mode of file, either 'r' or 'w'
file1.mode


"""We can read the file and assign it to a variable :"""
# Read the file
FileContent = file1.read()
FileContent


"""The /n means that there is a new line.

We can print the file:"""
# Print the file with '\n' as a new line
print(FileContent)


"""The file is of type string:"""
# Type of file content
type(FileContent)


"""We must close the file object:"""
# Close file after finish
file1.close()


"""==============
A Better Way to Open a File
Using the with statement is better practice, it automatically closes the file 
even if the code encounters an exception. The code will run everything in the 
indent block then close the file object."""

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)
     
# ---> This is line 1 
# ---> This is line 2
# ---> This is line 3
    
    
"""The file object is closed, you can verify it by running the following cell:"""
# Verify if the file is closed
file1.closed
# ---> True


"""We can see the info in the file:"""

# See the content of file
print(FileContent)
# ---> This is line 1 
# ---> This is line 2
# ---> This is line 3


"""The syntax is a little confusing as the file object is after the as statement. 
We also don’t explicitly close the file. Therefore we summarize the steps in a 
figure:

We don’t have to read the entire file, for example, we can read the first 4 
characters by entering three as a parameter to the method .read():"""

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))
​#---> This


"""Once the method .read(4) is called the first 4 characters are called. If 
we call the method again, the next 4 characters are called. The output for the 
following cell will demonstrate the process for different inputs to the method 
read():"""
# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    
# ---> This
# --->  is 
# ---> line 1 
# ---> 
# ---> This is line 2
    
    
"""The process is illustrated in the below figure, and each color represents 
the part of the file read after the method read() is called:

Here is an example using the same file, but instead we read 16, 5, and then 9 
characters at a time:"""

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
​
# ---> This
# --->  is 
# ---> line 1 
# ---> 
# ---> This is line 2


"""We can also read one line of the file at a time using the method readline():"""
# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
#---> first line: This is line 1 


"""We can use a loop to iterate through each line:"""
# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;
        
#---> Iteration 0 :  This is line 1 

# ---> Iteration 1 :  This is line 2

# ---> Iteration 2 :  This is line 3
            
            
"""We can use the method readlines() to save the text file to a list:"""
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()
​

"""Each element of the list corresponds to a line of text:"""
# Print the first line​
FileasList[0]
# ---> 'This is line 1 \n'

# Print the second line​
FileasList[1]
# ---> 'This is line 2\n'

# Print the third line​
FileasList[2]
# ---> 'This is line 3'


"""=================
Write and Save Files in Python
Welcome! This notebook will teach you about write the text to file in the 
Python Programming Language. By the end of this lab, you'll know how to write 
to file and copy the file.

Table of Contents
Writing Files
Copy a File
Estimated time needed: 15 min

Writing Files
We can open a file object using the method write() to save the text file to a 
list. To write the mode, argument must be set to write w. Let’s write a file 
Example2.txt with the line: “This is line A” """

# Write line to file
with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A")
    

"""We can read the file to see if it worked:"""
# Read file
with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
# ---> This is line A
# ---> This is line B


"""We can write multiple lines:"""
# Write lines to file
with open('/resources/data/Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
​

"""The method .write() works similar to the method .readline(), except instead 
of reading a new line it writes a new line. The process is illustrated in the 
figure , the different colour coding of the grid represents a new line added 
to the file after each method call.

You can check the file to see if your results are correct"""

# Check whether write to file
with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
# ---> This is line A
# ---> This is line B


"""By setting the mode argument to append a you can append a new line as 
follows:"""
# Write a new line to text file
with open('/resources/data/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")


""""You can verify the file has changed by running the following cell:"""
# Verify if the new line is in the text file
with open('/resources/data/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
​
# ---> This is line A
# ---> This is line B
# ---> This is line C
# ---> This is line C


"""We write a list to a .txt file as follows:"""
# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines
# ---> ['This is line A\n', 'This is line B\n', 'This is line C\n']


# Write the strings in the list to text file​
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
# ---> This is line A
# ---> This is line B
# ---> This is line C


"""We can verify the file is written by reading it and printing out the values:"""
# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
# ---> This is line A
# ---> This is line B
# ---> This is line C


"""We can again append to the file by changing the second parameter to a. 
This adds the code:"""
# Append the line to the file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line D\n")
​

"""We can see the results of appending the file:"""
# Verify if the appending is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())​
# ---> This is line A
# ---> This is line B
# ---> This is line C
# ---> This is line D
# ---> This is line D


"""===============
Copy a File
Let's copy the file Example2.txt to the file Example3.txt:"""

# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


"""We can read the file to see if everything works:"""
# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
# ---> This is line B
# ---> This is line C
# ---> This is line D
# ---> This is line D


""""After reading files, we can also write data into files and save them in 
different file formats like .txt, .csv, .xls (for excel files) etc. Let's take 
a look at some examples.

Now go to the directory to ensure the .txt file exists and contains the summary
 data that we wrote."""


"""=================
QUESTION 1

Consider the dataframe df, how would you find the element in the second-row and 
first column."""

df.ix[1,0] or df.iloc[1,0]

"""=================
QUESTION 2
Will the following code run? Yes"""

import pandas as banana

df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})

df.head()


"""=================
Reading: Using loc, iloc and ix (10 min)
 Bookmark this page
Using loc, iloc and ix
There are three ways to select data from a data frame in Pandas: loc, iloc, 
and ix. 

loc
loc is primarily label based; when two arguments are used, you use column 
headers and row indexes to select the data you want. loc can also take an 
integer as a row or column number.

Examples of loc usage:


loc will return a KeyError if the requested items are not found.

iloc 
iloc is integer-based. You use column numbers and row numbers to get rows or 
columns at particular positions in the data frame. 

Examples of iloc usage:


iloc will return an IndexError if the requested indexer is out-of-bounds.

ix
By default, ix looks for a label. If ix doesn't find a label, it will use an 
integer. This means you can select data by using either column numbers and row 
numbers or column headers and row names using ix.

In Pandas version 0.20.0 and later, ix is deprecated.

Using loc and iloc for slicing
You can also use loc and iloc to slice data frames and assign the values to a 
new data frame. 

Creating a new dataframe with loc slicing
You can also slice data frames and assign the values to a new data frame using 
the column names. The code assigns the first three rows and all columns in 
between to the columns named Artist and Released. The result is a new data 
frame Z with the corresponding values.



Creating a new dataframe with iloc slicing
In this example, we assign the first two rows and the first three columns to 
the variable Z. The result is a data frame comprised of the selected rows and 
columns. """


"""====================
Get to Know a numpy Array 
You will use the dataframe df for the following:"""

import pandas as pd
df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
​
"""1) plot the first three rows:"""
df.head(3)

"""2) obtain column  'a' """
df['a']
df['a']


"""=================
Working with and Saving Data

Get to Know a Pandas Array 
You will use the dataframe df for the following:"""

import pandas as pd
df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})

"""1) find the unique values in column  'a' :"""
df['a'].unique()
# ---> array([1, 2])

"""2) return a dataframe with only the rows where column  a  is less than two"""
df1 = df[df['a']<2]
df1

# ---- OR
df['a']<2


"""=================
QUESTION 1
consider the dataframe """

df=pd.DataFrame({'a':[1,2,1],'b':[1,1,1]})

"""what type does the following return df['a']==1"""
---> bool


"""=================
QUESTION 2
what task does the following method perform?"""

df.to_csv("file.csv")

---> save a dataframe to a csv file