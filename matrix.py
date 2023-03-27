# As a reminder, matrices (singular matrix) are nested lists. What I mean by 'nested' are lists inside lists.
# Here's an example:

matrix = [["b", 2], ["c", 3], ["a", 1]] # ---> Each element of the list is a list itself.

# To iterate over lists, we can use a for loop over to iterate over each element of the matrix. The common syntax for iterating over
# lists is: for element in sequence

for list in matrix:
    print(list) # ---> ["b", 2] ["c", 3] ["a", 1]
    
# To access the individual elements of the nested lists, we use an index in succession. 

for list in matrix:
    print(list[1]) # ---> 1 2 3
   
# Now to the best part, sorting matrices. This is a crucial concept to understand in your Machine Learning career.
# Recall the 'sort' method. It has two parameters (key: function to base sort on, reverse: reverse order of sort) both of which are keyword arguments. 
# We'll make a function argument that will take the second element of each list in the matrix. 

def second(list): 
    return list[1] # second element

matrix.sort(second) # sorts the matrix by the second element of each list in the matrix

print(matrix) # ---> ["a", 1] ["b", 2] ["c", 3]

# Be sure to copy this code if you need better understanding. 
