import numpy as np

# 0D array or scalar
mathScores = np.array((10, 33, 21, 45, 29))

# 1D array
scores = np.array([20, 12, 24, 23, 11, 9])

# 2D array
testScores = np.array([[1, 2, 4], [3, 5, 6]])

# 3D array
newTestScores =np.array([[[4, 6, 2], [6, 7, 3], [4, 2, 9]]])

# check number of dimensions in array
scores.ndim
testScores.ndim
newTestScores.ndim

# Higher dimension arrays

# 5D array
physicsScores = np.array([1, 2, 3], ndmin=5)


print(scores)


# indexing numpy array
