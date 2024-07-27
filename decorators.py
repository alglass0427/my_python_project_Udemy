def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2

def calcualte(calc_function,n1= 1,n2 = 2):
    return calc_function(n1,n2)
##function passed
print(calcualte(add))

# first class object

def outer_function():
    print("I am Outer")

    def nested_function():
        print ("i am inner")
    
    return nested_function   ###retuns the inner Function to be accessed globally
    # nested_function()
outer_function()
# nested_function() ### no access As it is local to outer
inner_function = outer_function()   ### outer Funtion returns inner_function now "inner_function" varialble becomes the actual nested funtion itself 
inner_function()   ## inner funtion is now a Funtion  to     print ("i am inner")

import time

#############PYTHON DECORATORS
###function that wraps another function to give additional functionality
# decorator function take a funtionas a parameter
# in below case -   any funtion is passed in
# and the wrapper function will run that function but delay it by 2 seconds

#####   SYNTACTIC SUGAR
def decorator_function (function):
    def wrapper_function():
        print("Before Delay")
        time.sleep(2) ###delay by two seconds
        print("Delayed")
        function()
        function()
        function()
        print("After Function")
    return wrapper_function   ###no ()




@decorator_function
def say_hello():
    print("Hello")
say_hello()

# decorator_function(hello("Alan"))


###same as passing a Function into a function


current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(end_time)
        print(start_time)
        print(f"{function.__name__} run speed: {end_time-start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000):
        i*i

@speed_calc_decorator
def slow_function():
    for i in range(1000000):
        i*i

fast_function()
slow_function()