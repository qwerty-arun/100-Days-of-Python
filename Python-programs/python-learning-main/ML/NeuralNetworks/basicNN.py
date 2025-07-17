import numpy as np

# Example input (like a feature vector or word embedding)
x = np.array([2.0, 3.0])

# Initialize weights (2 inputs -> 1 output)
W = np.array([[0.4, 0.6]])  # Shape: (1, 2)
b = np.array([0.5])         # Shape: (1,)

# Linear transformation: y = Wx + b
def neural_output(W, x, b):
    return np.dot(W, x) + b

# Case 1: Original parameters
output1 = neural_output(W, x, b)
print("Output with original W and b:", output1)

# Case 2: Change weights
W_new = np.array([[1.0, -1.0]])
output2 = neural_output(W_new, x, b)
print("Output with changed W:", output2)

# Case 3: Change bias
b_new = np.array([-1.0])
output3 = neural_output(W, x, b_new)
print("Output with changed b:", output3)

