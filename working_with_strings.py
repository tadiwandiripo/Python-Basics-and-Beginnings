print("Giraffe Academy")
# new line --> \n
print("Giraffe\nAcademy")
# quotation mark --> \"
print("Giraffe\"Academy")
print("Giraffe\Academy")

phrase = "Giraffe Academy"
print(phrase)

# Concatinating
print(phrase + " is cool")
print(phrase.lower()) # converting to lowercase
print(phrase.upper()) # converting to uppercase
print(phrase.islower()) #returns boolean value after compasrison
print(phrase.isupper())

print(len(phrase)) # length of a string
print(phrase[0]) #accessing specific elements of the string using zero indexing.

#index function
print(phrase.index("G")) #more of reverse of what we just did.

print(phrase.replace("Giraffe", "Elephant"))