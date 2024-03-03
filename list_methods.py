# Given list
ids = [4353, 2314, 2956, 3382, 9362, 3900]

# a. Remove 3382 from the list
ids.remove(3382)

# b. Get the index of 9362
index_9362 = ids.index(9362)

# c. Insert 4499 in the list after 9362
# Since we want to insert after 9362, we add 1 to the index
ids.insert(index_9362 + 1, 4499)

# d. Extend the list by adding [5566, 1830] to it
ids.extend([5566, 1830])

# e. Reverse the list
ids.reverse()

# f. Sort the list
ids.sort()

# Return the final modified list
print(ids)
