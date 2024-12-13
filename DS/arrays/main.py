import numpy as np

# 0D array or scalar
mathScores = np.array((10, 33, 21, 45, 29))

# 1D array
scores = np.array([20, 12, 24, 23, 11, 9])

# 2D array
testScores = np.array([[1, 2, 4], [3, 5, 6]])

# 3D array
newTestScores =np.array([[[4, 6, 2], [6, 7, 3]], [[4, 2, 9], [2, 7, 9]]])

# check number of dimensions in array
scores.ndim
testScores.ndim
newTestScores.ndim

# Higher dimension arrays

# 5D array
physicsScores = np.array([1, 2, 3], ndmin=5)


print(scores)


# indexing numpy array
# Access 1D array
scores[2]

# Access 2D array
testScores[0, 1] # 2nd element first row

# Access 3D array 
newTestScores[0, 1, 2]

# negative indexing
scores[1, -1]  # second element second dimension



# SLicing Arrays
# slicing 2D arrays
testScores[1, 1:3]  # from second element slice from idx 1 to idx 3
testScores[0:2, 2]  # from both elements return index 2


