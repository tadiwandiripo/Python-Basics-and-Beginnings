# allows python to return information from a function

def cube(num):
    return num*num*num
# allows us to return to the caller
# You can't put code after the return statement
# the break statement breaks us out of the function


result = cube(4)
print(result)
