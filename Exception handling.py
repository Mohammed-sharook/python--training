'''
Exception Handling:
    1.Errors detected during execution called exception
    2.Exceptions are raised when code is syntactically correct but the code resulted in an error
    3.Try: test a block of code for errors
    4.except: Handle the errors
    5.If try block raises an error the except block will be executed
    6.finally: will be executed regardless if try block raises an error or not

Raise an Exception
    We can throw an exception(or raise) using raise keyword.(if condition occurs)
'''

# Exception handling
try:
    print("Aydensharook")
except NameError:
    print("This is an error")

finally:
        print("This will run always if error occurs or not")

# Built-in Exceptions
try:
    print(110/0)
except ZeroDivisionError:
    print("not divide by zeros")

# Raise an exception
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise