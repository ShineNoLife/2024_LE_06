import numpy as np

#-------50 MOST COMMONLY USED NUMPY FUNCTIONS-------#

# Array Creation Functions
# 1. Creates an array from a list
a = np.array([1, 2, 3])
print(a)

# 2. Creates a 2x3 array filled with zeros
a = np.zeros((2, 3))
print(a)

# 3. Creates a 2x3 array filled with ones
a = np.ones((2, 3))
print(a)

# 4. Creates an array from 0 to 10 with step 2
a = np.arange(0, 10, 2)
print(a)

# 5. Creates an array with 5 values evenly spaced between 0 and 1
a = np.linspace(0, 1, 5)
print(a)

# 6. Creates a 3x3 identity matrix
a = np.eye(3)
print(a)

# 7. Creates a 2x3 array filled with the value 7
a = np.full((2, 3), 7)
print(a)

# 8. Creates an uninitialized 2x2 array (random values)
a = np.empty((2, 2))
print(a)

# 9. Creates a 2x3 array with random values between 0 and 1
a = np.random.rand(2, 3)
print(a)

# 10. Creates a 2x3 array with random integers from 0 to 9
a = np.random.randint(0, 10, (2, 3))
print(a)

# Array Manipulation Functions
# 11. Reshapes a 1D array to a 2x3 array
a = np.arange(6).reshape((2, 3))
print(a)

# 12. Transposes rows to columns
a = np.array([[1, 2], [3, 4]])
print(np.transpose(a))

# 13. Flattens a 2D array to 1D
a = np.array([[1, 2], [3, 4]])
print(a.flatten())

# 14. Ravel flattens array like flatten but returns a view if possible
print(a.ravel())

# 15. Concatenates arrays along an axis
a = np.array([1, 2])
b = np.array([3, 4])
print(np.concatenate((a, b)))

# 16. Stacks arrays horizontally
print(np.hstack((a, b)))

# 17. Stacks arrays vertically
print(np.vstack((a, b)))

# 18. Splits an array into three sub-arrays
a = np.array([1, 2, 3, 4, 5, 6])
print(np.split(a, 3))

# 19. Expands dimensions by adding an axis
a = np.array([1, 2])
print(np.expand_dims(a, axis=0))

# 20. Squeezes dimensions of length 1
a = np.array([[[1, 2, 3]]])
print(np.squeeze(a))

# Indexing, Slicing, and Conditional Selection
# 21. Selects elements based on a condition
a = np.array([1, 2, 3, 4])
print(np.where(a > 2, a, -1))

# 22. Selects elements by index
a = np.array([10, 20, 30])
print(np.take(a, [0, 2]))

# 23. Finds indices of non-zero elements
a = np.array([1, 0, 2, 0, 3])
print(np.nonzero(a))

# 24. Finds unique elements in the array
a = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(a))

# 25. Selects elements based on choices and indices
choices = [10, 20, 30]
index = [0, 2, 1]
print(np.choose(index, choices))

# 26. Finds the index of the max value
a = np.array([1, 5, 2])
print(np.argmax(a))

# 27. Finds the index of the min value
print(np.argmin(a))

# 28. Finds where elements should be inserted to maintain order
a = np.array([1, 3, 5])
print(np.searchsorted(a, 4))

# Mathematical Functions
# 29. Adds arrays element-wise
print(np.add([1, 2], [3, 4]))

# 30. Subtracts arrays element-wise
print(np.subtract([3, 5], [1, 2]))

# 31. Multiplies arrays element-wise
print(np.multiply([2, 3], [4, 5]))

# 32. Divides arrays element-wise
print(np.divide([4, 6], [2, 3]))

# 33. Raises each element of base to the power of exp
print(np.power([2, 3], [2, 3]))

# 34. Calculates square root of each element
a = np.array([4, 9, 16])
print(np.sqrt(a))

# 35. Calculates the exponential of each element
a = np.array([1, 2, 3])
print(np.exp(a))

# 36. Calculates the natural log of each element
a = np.array([1, np.e, np.e**2])
print(np.log(a))

# 37. Calculates the sine of each element
a = np.array([0, np.pi / 2, np.pi])
print(np.sin(a))

# 38. Rounds elements to one decimal place
a = np.array([1.234, 2.345])
print(np.round(a, 1))

# 39. Rounds each element down
print(np.floor(a))

# Statistical Functions
# 40. Computes mean
a = np.array([1, 2, 3, 4])
print(np.mean(a))

# 41. Computes median
print(np.median(a))

# 42. Computes variance
print(np.var(a))

# 43. Computes standard deviation
print(np.std(a))

# 44. Computes sum of elements
print(np.sum(a))

# 45. Finds the minimum value
print(np.min(a))

# 46. Finds the maximum value
print(np.max(a))

# 47. Computes 50th percentile
print(np.percentile(a, 50))

# 48. Computes cumulative sum
print(np.cumsum(a))

# 49. Calculates histogram values and bins
#bins are equal ranges 
#hist counts how many values are in this bin's range 
hist, bins = np.histogram(a, bins=2)
print(hist, bins)

# Sample data
data = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])

# Create a histogram with 5 bins
hist, bin_edges = np.histogram(data, bins=5)

print("Histogram counts:", hist)
print("Bin edges:", bin_edges)
