# Take a string input and print its length.
name = input("Enter the name:")
print(len(name))



# Convert a sentence to lowercase.
name="Hem"
print(name.lower())


# Replace spaces with underscores in a string.
name=("Hem")
print(name.replace("","_"))


# Extract the first and last character of a string.
cityname="Valsad"
print("First:",cityname[0])
print("Last:",cityname[5])



# Reverse a string using slicing.
lastname="Patel"
print(lastname[::-1])




# Count how many times a letter appears in a string.
movie="Avengers"
print(movie.count("e"))




# Check if a word is present in a sentence.
sentence="Check if there is a new update"
word="update"
if(word in sentence):
    print(word,"Is persent in the sentence")
else:
    print(word,"is not present in the sentencse")





# Take name & age and print using f-string formatting.
name="Hem"
age=20
print(f"My name is {name} and I am {age} years old")



# Remove extra spaces from the start and end of a string.
text = input("Enter a string: ")
print(text.strip())




# Join a list of words into a single string with - between them.
words = ["My","name","is", "Hem"]
print("-".join(words))