0x03. Python - Data Structures: Lists, Tuples

Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. 

Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses. This helps in understanding the Python tuples more easily.
Creating a Tuple
In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of parentheses for grouping the data sequence.

Note: Creation of Python tuple without the use of parentheses is known as Tuple Packing.  

Python program to demonstrate the addition of elements in a Tuple.
# Creating an empty Tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
 
# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
 
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 
# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)
