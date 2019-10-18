# Python Lists
list = ['abcd', 786 , 2.23, 'john', 70.20]
tinylist = [123, 'john']

# Prints complete list
print(list) # Respond: ['abcd', 786, 2.23, 'john', 70.2]

# Prints first element of the list
print(list[0]) # Respond: abcd

# Prints elements starting from 2nd till 3rd 
print(list[1:3]) # Respond: [786, 2.23]

# Prints elements starting from 3rd element
print(list[2:]) # Respond: [2.23, 'john', 70.2]

# Prints list two times
print(tinylist * 2) # Respond: [123, 'john', 123, 'john']

# Prints concatenated lists
print(list + tinylist) # Respond: ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']

# Prints count of lists
print(len(list)) # Respond: 5
