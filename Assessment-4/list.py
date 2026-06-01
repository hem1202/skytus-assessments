
# Create a list of your 5 favorite movies.
moviename=["Avengers","Ironman","Spiderman","Hulk","Venom"]





# Add a new movie to the list.
moviename.append("Dr.strange")
print(moviename)

# Remove the first movie from the list.
moviename.pop()
print(moviename)




# Sort a list of numbers in ascending order.
order=[9,7,5]
order.sort()
print("Sorted:",order)


# Reverse a list.
order2=[1,2,3,4,]
order2.sort(reverse=True)
print("Revrsedlist:",order2)




# Find the largest number in a list.
largest_numbers=max(order2)
print(largest_numbers)





# Merge two lists into one.
l1=[1,2,3,4,5,]
l2=[6,7,8,9,0]
mergedlist = l1+l2
print(mergedlist)


# Access the last element of a list without using index number.
element=[10,20,99]
print(element[-1])



# Create a nested list and access a specific inner element.
nested = [[1, 2], [3, 4], [5, 6]]
print(nested[1][0])



# Count how many times an element appears in a list.
elements=[11,44,77,33,55,11,88,55,44]
print(elements.count(55))

