# -*- coding: utf-8 -*-

def f(x, y):
    x = x + 3
    y.append(23)
    print(x, y)

x = 22
y = [22]
f(x, y)
print(x, y)


def sumar(x, y):
    return x + y

print(sumar(3, 2))


def f(x, y):
    return x * 2, y * 2

a, b = f(1, 2)
print(a, b)

# function definition without arguments **************************************
def hello_world():
    """
    Example function definition without arguments
    :rtype: None
    """
    print("You are in Hellow World" + "\n")

my_var = hello_world()  # calling a function
print("Return value function: " + str(type(my_var)))

# function with arguments ****************************************************
def func(pass_argument):
    """
    Example function definition with a simple argument
    :param pass_argument: string to print
    :type pass_argument: str
    :rtype: None
    """
    print(pass_argument)

str_argument = "Pass argument string"
func(str_argument)  # calling a function

# function with an arguments and return type *********************************
def sum(a, b):
    """
    sum of two numbers
    :param a: first operant
    :type a: int or long or float
    :param b: second operant
    :type b: int or long or float
    :return: suma
    :rtype: int or long or float
    """
    c = a + b
    return c

x = 10
y = 50
print("Result of addition " + str(x) + " + " + str(y) + " = " + str(sum(x, y)))

# function with default argument *********************************************
def info(name, age=18):
    """
    Example function with default argument
    :param name: Name
    :rtype: str
    :param age: Age
    :return: int
    :rtype: None
    """
    print("Name: " + name + ", age: ", age)

info("Dami", age=30)  # Name: Dami, age:  30
info("Dami")  # Name: Dami, age:  18

# function with variable lenght argument *************************************
def print_variable_argument(convencional_argument,
                            *variable_argument):
    """
    Example function with variable lenght argument
    :param convencional_argument: conventional argument
    :param variable_argument: variable argument
    """
    str_msg = "Convencional argument: " + str(convencional_argument) + ", Variable arguments: "
    for var in variable_argument :
        str_msg += str(var) + ", "
    print(str_msg)

print_variable_argument(60)
print_variable_argument(100,90,40,60)

# Pass by reference versus pass by value *************************************
def fun(a):
    a = a + 9000
    print("var value inside the function: ", a)

a = 1
fun(a)
print("var value outside the function: ", a)

def pass_ref(list1):
    """
    Example 2 pass by reference versus pass by value
    :param a: lista a imprimir
    :type a: list
    """
    list1.extend([23,89])
    print("2.- List inside the function: ", list1)

list1 = [12, 67, 90]
print("1.- List before pass: ", list1)
pass_ref(list1)
print("3.8- List outside the function: ", list1)

# Scope of variables *********************************************************
def func():
    """
    Example 1 scope of variables
    :param a: number to print
    :type a: int
    """
    a = 1
    print("Inside the function the value of a is acting as local variable", a)
a = 9000
func()
print("Outside the function the value of a is acting as global variable", a)

def func():
    """
    Example 2 scope of variables
    :param a: number to print
    :type a: int
    """
    global a
    a = a + 7
    print("2.- Variable a is now global", a)

a = 9000
print("1.- Variable a before pass: ", a)
func()
print("3.- Accesing the value a outside the function", a)