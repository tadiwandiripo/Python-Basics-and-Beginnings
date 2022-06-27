lucky_numbers = [1, 2, 3, 4, 5, 6]
friends = ["Walter", "Raymond", "Marlon", "Memory", "Tiger"]

print(friends)
friends.extend(lucky_numbers)  # Adding the lucky_numbers array to the end of the friends array
friends.append("Godwin")  # Adds to the end of the ist
friends.insert(1, "Kelly")  # Takes in 2 parameters (index_position, value)
friends.remove("Raymond")  # Targets a specific element within the list
friends.clear()  # Removes everything from the list
friends.pop()  # Removes the last element in the list
friends.sort()  # Alphabetical order
lucky_numbers.sort()  # ascending order
lucky_numbers.reverse()  # reversing the order of the list
friends2 = friends.copy()  # Copying list to friends2

print(friends.index("Walter"))  # Checks if an element is in the list
print(friends.count("Tiger"))  # Counts the number of element sare in the list with the same name
