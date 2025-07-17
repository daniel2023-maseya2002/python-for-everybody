# &nbsp; PYTHON

# \_\_\_\_\_\_\_\_\_\_



Variables, Expressions, and Statements

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Constants

\_\_\_\_\_\_\_\_\_\_



. Fixed values such as numbers, letters, and strings are called "constants" because their values doesn't change



&nbsp;	- Numeric constants are as you aspects

&nbsp;	- String constants use single quotes(')

&nbsp;         or double quotes(")



# CHAP3: Conditional Execution

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



< : Less than

<= : Less than or equal to

== : Equal to

>= : Greater than or Equal to

> : Greater than

!= : Not Equal 

= : is used for assignment



# CHAP4: Max Function

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





def: that stands for defined function, is like if statement.

def is not running the code but it just remember the code and that's what we call the "store phase".



In python there are two types of functions:



1\. BUILT-IN Function: that are provided as part of python-print(), input, type(), float(), int().....



2\. FUCTION THAT WE DEFINE OURSELVES and then use





BUILDING OUR OWN FUCTIONS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Declare the def function then declare any word you want with par



entheses(),

example:



x = 5

def call():

&nbsp;	print('Dani')

&nbsp;	print('How was your day')

print('Hello')

call()

x = x + 2

print(x)





ARGUMENTS

\_\_\_\_\_\_\_\_\_



An argument is a value we pass into the function as its input when we call the function



example: big = max('Hello world')  Hello World is an argument





Parameters

\_\_\_\_\_\_\_\_\_\_



A parameter is a variable which we use in the function definition.

example: def greet(lang), greet is the parameter



Return Values

\_\_\_\_\_\_\_\_\_\_\_\_\_



Often a function will take its arguments, do some computation, and return a value to be used as he value of the function call in the calling expression.



def greet():

&nbsp;	return "Hello"

print(greet(), "Dan")

print(greet(), "Maseya")



# CHAP 5: Loop and Iterations

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



&nbsp;\*Definite Loops

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



define loops is th loop run once for each of the items in a set using the python construct.



Example:



1\. with Integer:

&nbsp;	for i in \[5, 4, 3, 2, 1]:

&nbsp;		Print(i)

&nbsp;	print('blastoff!')



2\. with string:

&nbsp;	friends = \['Peter', 'Glenn', 'Dan']

&nbsp;	for friend in friends:

&nbsp;		print('Happy New Year:', friend)

&nbsp;	print('Done!')



\*Loop Idioms:

\_\_\_\_\_\_\_\_\_\_\_\_\_



Example:

num1:

&nbsp;	print('Before')

&nbsp;	for thing in \[9, 41, 12, 3, 74, 15] :

&nbsp;		print(thing)

&nbsp;	print('After')

num2:

&nbsp;	largest\_so\_far = -1

&nbsp;	print('Before', largest\_so\_far)

&nbsp;	for the\_num in \[9, 41, 12, 3, 74, 15] :

&nbsp;   		if the\_num > largest\_so\_far:

&nbsp;       		largest\_so\_far = the\_num

&nbsp;   		print(largest\_so\_far, the\_num)

&nbsp;	print('After', largest\_so\_far)





Exercises

\_\_\_\_\_\_\_\_\_



1\. Write a program which repeatedly reads numbers until the users enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

num = 0

tot = 0.0

while True:

&nbsp;   sval = input('Enter a number: ')

&nbsp;   if sval == 'done' :

&nbsp;       break

&nbsp;   try:

&nbsp;       fval = float(sval)

&nbsp;   except:

&nbsp;       print('Invalid input')

&nbsp;       continue

&nbsp;   #print(fval)

&nbsp;   num = num + 1

&nbsp;   tot = tot + fval



\#print('ALL DONE')

print(tot, num, tot/num)



\* Counting in a Loop

--------------------



To count how many times we execute a loop, we introduce a counter variable that starts at 0 and add one to each time though the Loop.



example:

zork = 0

print('Before', zork)

for thing in \[9, 42, 12, 3, 74, 15] :

&nbsp;   zork = zork + 1

&nbsp;   print(zork, thing)

print('After', zork)





\* Summing in a Loop

-------------------



To add up a value we encounter in a loop. we introduce a sum variable start at 0 and add the values to the sum each time through the loop



example:

zork = 0

print('Before', zork)

for thing in \[9, 42, 12, 3, 74, 15] :

&nbsp;   zork = zork + thing

&nbsp;   print(zork, thing)

print('After', zork)



The "is" and "is not" Operations

--------------------------------



\- Python has an is operator that can be used in logical expressions

\- implies "is the same as"

\- Similar to, but stronger than ==

\- is not also is a logical operator





# CHAP 6: String

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_



\* Looking Inside Strings

------------------------

-We can get at any single character in a string using an index specified in square brackets.



Looping Through Strings

----------------------- 

name = 'danielmaseya'

count = 0

for letter in name:

&nbsp;   if letter == 'a':

&nbsp;       count = count + 1

print(count) 



Slicing Strings

---------------

d = 'daniel maseya'

print(d\[0:4])

print(d\[7:11])



\# String Concatenation

a = 'Hello'

b = a + 'papou'

print(b)

c = a + ' ' + 'papou'

print(c)

print(c\[0:3])

print(c\[6:9])



String Library

--------------



d = 'daniel maseya'

print(d\[0:4])

print(d\[7:11])



\# String Concatenation

a = 'Hello'

b = a + 'papou'

print(b)

c = a + ' ' + 'papou'

print(c)

print(c\[0:3])

print(c\[6:9])





\# String Library

greet = 'Hello DANI'

zap = greet.lower();

print(zap)

print(greet)

print('Hey Papou' .lower())



\#Make Upper

print(greet.upper())



\# Search String



mec = greet.find('el')

print(mec)



\# Replace String



str = greet.replace('DANI', 'Maseya')

print(str)



mpg = greet.replace('e', 'a')

print(mpg)





# CHAP7: Reading Files

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



Before to use file you must open this 



\* Opening a file

-----------------



\- Before to use the file, we must tell python which file we are going to work with and what we will be doing with the file.

\- This is done with the open() function

\- open() returns a "file handle" -a variable used to perform operations on the file.

\- Similar to File -> Open" in a Word Processor



\* File Handle as a Sequence

----------------------------

xfile = open('DANIEL MASEYA MUBU.txt')

for cheese in xfile:

&nbsp;   print(cheese)



\* Counting Lines in a File

---------------------------



\- Open a file read-only

\- Use a for loop to read each line

\- Count the lines and print out the number of lines



xfile = open('DANIEL MASEYA MUBU.txt')

count = 0

for cheese in xfile:

&nbsp;   count = count + 1

print('Line Count:', count)



# CHAP8: Python Lists

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





Programming

-----------



\* Algorithms:

&nbsp;	A set of rules or steps used to solve a problem.



\* Data Structures:

&nbsp;	A particular way of organizing data in a computer.





What's not a collection and what's a collection?

------------------------------------------------



\- A not collection doesn't allow us to put many values in single variable

&nbsp;	Ex:

&nbsp;		x = 2

&nbsp;		x = 4

&nbsp;		print(x)

&nbsp;		output: 4

\- A collection allow us to put many values in single value



&nbsp;	Ex:

&nbsp;		friends = \['Joseph', 'Glenn', 'Sally']



Using the range function

------------------------



\- The range function returns a list of numbers that range from zero to one less than the parameter.

\- We can construct an index loop using for and an integer iterator



Concatenating Lists Using +

---------------------------



t = \[9, 41, 12, 3, 74, 15]

print(t)

x = t\[1:3]

print(x)

y = t\[:4]

print(y)

z = t\[3:]

print(z)

w = t\[:]

print(w)



Building a List from Scratch

----------------------------



\- We can create an empty list and then add elements using the \*append\* method.



\- The list stays in order and new elements are added at the end of the list.



Best Friends: String and Lists

------------------------------



&nbsp;abc = 'With three words'

stuff = abc.split()

print(stuff)

print(len(stuff))

print(stuff\[0])

print(stuff)

for w in stuff :

&nbsp;   print(w)



# CHAP9: Python Dictionaries

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



\* A Story of Two Collections..

------------------------------



\- List:

&nbsp;	A list collection of values that stay in order



\- Dictionary: 

&nbsp;	A 'bag' of values, each with its own label, So in dictionary each item must have chuck label



\* Dictionaries

--------------



\- Dictionaries are python's most powerful data collection.



\- Dictionaries allow us to do fast database-like operation in python



\- Dictionaries have different names in different languages

&nbsp;	- Associative Arrays - Perl / PHP

&nbsp;	- Properties or Map or HashMap - Java

&nbsp;	- Property Bag - C#/ .Net



\* Dictionary Literals

---------------------



\- Dictionary literals use curly braces and have a list of key: value pairs



\- You can make an empty dictionary using empty curly braces





\* Most Common Name?

-------------------



\- marquard

\- zhen

\- csev

&nbsp;

Counting

---------

\# Counting

counts = dict()

names = \['csev', 'cwen', 'csev', 'zqian', 'cwen']

for name in names :

&nbsp;   if name not in counts :

&nbsp;       counts\[name] = 1

&nbsp;   else:

&nbsp;       counts\[name] = counts\[name] + 1

print(counts)



\* The get method for dictionaries

---------------------------------



\- The pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called get() that does this for us.



\- Default value if key does not exist(and no Traceback).





\* Counting Words in Text

-------------------------



# CHAP10: The Tuples Collection

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



-The tuples are another kind of sequence that functions much like a list they have elements which are indexed starting at 0



-You can't add the thing like appened or sort in tuples 





\* Sorting Lists of Tuples

--------------------------

We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence





# CHAP11: Regular Expressions

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_





import re



hand = open('PYTHON.txt')

for line in hand:

&nbsp;   line = line.rstrip()

&nbsp;   if re.search('^function: ', line):

&nbsp;       print(line)





# CHAP12: Networked Programs

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# 



Application Protocol

--------------------



\- Since TCP (and Python)gives us a reliable socket, what do we want to do with the socket? what problem do we want to solve?



\- Application Protocols

&nbsp;	-Mail



&nbsp;	-World Wide Web





An HTTP Request in Python

-------------------------



import socket



mysock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)

mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/Dictionary.txt HTTP/1.0\\n\\n'.encode()

mysock.send(cmd)



while True :

&nbsp;   data = mysock.recv(512)

&nbsp;   if (len(data) < 1):

&nbsp;       break

&nbsp;   print(data.decode())

mysock.close()





About Characters and Strings

----------------------------





Using urllib in Python

----------------------

Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file



What Is Web Scraping ?

----------------------



\- When a program or script pretends to  be a browser and retrieves web pages, looks at those web pages, extracts information, and then looks at more web pages.



\- Search engines scrape web pages - we call this "spidering the web" or "web crawling".





# **CHAP13: USING WEB SERVICES**

# **\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**



In the web services we have two(2) formats XML and JSON(JavaScript Object Notation),



what's the formats ?

&nbsp;	the formats is that sending the data into the net and get the response.



&nbsp;1. XML: we have to agree on a format that is gonna represent the data,

&nbsp;2. JSON: It is simpler and easier, but is not as precise and descriptive as XML is





1. ###### ***XML(eXtensible Markup Language)***

<i>----------------------------------</i>



Making up data to send across the network........



&nbsp;	- Start Tag

&nbsp;	- End Tag

&nbsp;	- Text Content

&nbsp;	- Attribute

&nbsp;	- Self Closing Tag



*Example:*

*--------*

<person>

&nbsp;   <name>Daniel</name>

&nbsp;   <phone type ="intl">

&nbsp;    +250 791 434 027

&nbsp;   </phone>

&nbsp;   <email hide="yes"/>

</person>



*XML Schema*

*----------*

\- Describing a "contact" as to what is acceptable XML

\- XML Schema is a language that allows you to decide 





###### ***Many XML Schema Languages***



* Document Type Definition(DTD)

&nbsp;	http://en.wikipedia.org/wiki/Document\_Type\_Definition

* Standard Generalized Markup Language(ISO 8879:1986 SGML)

&nbsp;	http://en.wikipedia.org/wiki/SGML

* XML Schema from W3C - (XSD)

&nbsp;	http://en.wikipedia.org/wiki/XML\_Schema(W3C)



***XSD Structure***

***-------------***

* xs: element
* xs: sequence
* xs:complexType



###### **2. JSON(JavaScript Object Notation)**

**--------------------------------------------**



JSON is best for just pulling data, in this step is best than xml



input = '''\[

&nbsp;   {   "id" : "001",

&nbsp;       "x" : "2",

&nbsp;       "name" : "Dani",

&nbsp;       "phone" : {

&nbsp;           "type" : "intl",

&nbsp;           "number" : "+250 791 434 027"

&nbsp;       }

&nbsp;   },

&nbsp;   {   "id" : "009",

&nbsp;       "x" : "7",

&nbsp;       "name" : "Maseya",

&nbsp;       "phone" : {

&nbsp;           "type" : "intl",

&nbsp;           "number" : "+243 895 485 491"

&nbsp;       }

&nbsp;   }

]'''



info = json.loads(input)

print('User count:' ,len(info))

for item in info:

&nbsp;   print('Name:' ,item\['name'])

&nbsp;   print('Id:' ,item\['id'])

&nbsp;   print('Attribute:' ,item\['x'])

&nbsp;   print('Phone:' ,item\['phone']\['number'])



###### **Service Oriented Approach**

###### **-------------------------**



* Most non-trivial web application use services.
* They use services from other applications

&nbsp;	- Credit Card Charge

&nbsp;	- Hotel Reservation Systems

* Services Publish the "rules" applications must follow to make use of the service(API)



###### **Web Services**

###### **------------**



1. **API(Application Program Interface)**
1. 
**-------------------------------------**



An API is typically defined in terms of the programming language used to build an application.

