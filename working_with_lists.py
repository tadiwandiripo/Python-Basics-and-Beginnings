friends = ["Walter", "Raymond", "Marlon", "Memory", "Tiger"]  # creating a list which stores multiple values
# index -->   0          1          2        3         4
#                                  -1
# How can we access individual elements?
print(friends)
print(friends[1])  # to access elements refer to their index
print(friends[1:])  # to select a range of elements from Raymond onwards
print(friends[1:3])  # Starts selecting from Raymond and ends at Marlon.

friends[1] = "Mike"  # Here I was manipulating the list
print(friends)
