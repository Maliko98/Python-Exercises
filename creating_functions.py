# Python Built-In Functions

# print ("Hello World")
# len()
# range()
# type()
# .upper()
# .lower()

# A Function is a block of code that we can reuse.
#Below are examples of user-defined functions

# def name_of_the_function():
#       definition of the function


#define a function
# def greeting(name):
#     print("Welcome to Skill City ",name)

# # Then call the function
# greeting("Maliko")
# greeting("John Dutton")
# greeting("Franklin Saint")

# # Calling a Function, the name in the bracket is an Argument
# # The Parameter, is whats listed in the brackets after you define a function, you can have multiple parameters aside from name
# # This is what is called user-defined function

# # Better example below
# def greet(firstName, lastName, age, city):
#     print("Welcome to Skill City ",firstName, lastName)
#     print("Your age is ", age)
#     print("You are from ", city)

# # Then call the function
# greet("Maliko", "Ani", 26, "Nigeria")
# greet("John", "Dutton", 55, "YellowStone Branch")
# greet("Franklin", "Saint", 28, "California")

#If you provide 4 parameters you must provide 4 arguments, otherwise it will provide an error
#You can define your default parameters i.e. firstName = Unknown, if we do not know some of the values

# #Arithmetic Functions

# def sum(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a / b

# # Let's now call these functions
# print(sum(2,3))
# print(div(61,6))
# print(mul(21,3))
# print(div(9,4))

#Difference between a function and a procedure? - Common Interview Question#
# A function is a block of code that performs a specific task and returns a value, while a procedure is a block of code that performs a task but does not return any value

# When you define a variable outside the function, they can become global variables

#Example

name = "Tommy" #Global Variable - Accessible to all functions

def my_function():
    age = 12 #Local Variable - Accessible to this function
    print("Hello",name)

my_function()

#A Local variable exists within the function
#Try to minimize your global variables as it can get confusing

#Important tip

#You can use import name_of_file to access functions in a different file.
#This way you don't have thousands of lines of code on one page, helps things look neater and much easier to read.

#i.e
import main #custom module/user defined module - whatever you name your files.
import random #built in module

#You can access your variables in other files by doing the following

#Example
#file_name.variable i.e. main.name()
#To make things simplistic, you can say import main as mn
#Hence using an alias, import file_name as abbreviated_file_name