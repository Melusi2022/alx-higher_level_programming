0x02. Python - import & modules

Import in python is similar to #include header_file in C/C++. Python modules can get access to code from another module by importing the file/function using import. The import statement is the most common way of invoking the import machinery, but it is not the only way.

import module_name

When the import is used, it searches for the module initially in the local scope by calling __import__() function. The value returned by the function is then reflected in the output of the initial code. 

import math
pie = math.pi
print("The value of pi is : ",pie)

Output:

The value of pi is : ', 3.141592653589793
import module_name.member_name 

In the above code module, math is imported, and its variables can be accessed by considering it to be a class and pi as its object. 
The value of pi is returned by __import__(). pi as a whole can be imported into our initial code, rather than importing the whole module. 


