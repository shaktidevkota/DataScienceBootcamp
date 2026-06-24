import numpy as np

# 1. CREATING ARRAYS
arr_from_list = np.array([1, 2, 3, 4, 5])
zeros_matrix = np.zeros((2, 3))
ones_matrix = np.ones((3, 3), dtype=int)
sequence = np.arange(0, 10, 2)
linspace_arr = np.linspace(0, 1, 5)

# 2. ATTRIBUTES & RESHAPING
base_arr = np.arange(12)
shape_info = base_arr.shape
dimensions = base_arr.ndim
matrix_2d = base_arr.reshape(3, 4)
flattened = matrix_2d.ravel()

# 3. INDEXING & SLICING
matrix_3x3 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
single_element = matrix_3x3[1, 2]
sub_matrix = matrix_3x3[0:2, 1:3]
first_row = matrix_3x3[0, :]
second_col = matrix_3x3[:, 1]

# 4. VECTORIZED MATH
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
addition = a + b
multiplication = a * b
scalar_power = a ** 2
dot_product = np.dot(a, b)

# 5. AGGREGATIONS & AXES
agg_matrix = np.array([[1, 2, 3], [4, 5, 6]])
total_sum = agg_matrix.sum()
max_val = agg_matrix.max()
column_sums = agg_matrix.sum(axis=0)
row_means = agg_matrix.mean(axis=1)

# 6. BOOLEAN MASKING
data = np.array([12, 45, 7, 23, 56, 89, 3])
mask = data > 25
filtered_data = data[mask]
data[data > 50] = 50

# 7. RANDOM GENERATION
np.random.seed(42)
rand_floats = np.random.rand(2, 2)
rand_normal = np.random.randn(3)
rand_ints = np.random.randint(1, 100, size=5)

# PRINT RESULTS
print("--- 1. CREATING ARRAYS ---")
print(arr_from_list, "\n", zeros_matrix, "\n", ones_matrix, "\n", sequence, "\n", linspace_arr)
print("\n--- 2. ATTRIBUTES & RESHAPING ---")
print(shape_info, dimensions, "\n", matrix_2d, "\n", flattened)
print("\n--- 3. INDEXING & SLICING ---")
print(single_element, "\n", sub_matrix, "\n", first_row, "\n", second_col)
print("\n--- 4. VECTORIZED MATH ---")
print(addition, multiplication, scalar_power, dot_product)
print("\n--- 5. AGGREGATIONS & AXES ---")
print(total_sum, max_val, column_sums, row_means)
print("\n--- 6. BOOLEAN MASKING ---")
print(mask, filtered_data, data)
print("\n--- 7. RANDOM GENERATION ---")
print(rand_floats, "\n", rand_normal, "\n", rand_ints)