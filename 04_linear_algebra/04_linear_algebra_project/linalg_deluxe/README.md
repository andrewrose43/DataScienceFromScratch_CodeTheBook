# Linalg Deluxe
An extension of Joel Grus's linear algebra Python library as he wrote it in chapter 4 of *Data Science from Scratch*. I have added transposition, symmetry checking, multiplication of vectors by matrices, the angle between two vectors, outer products, cross products, matrix multiplication, determinants, adjoint matrices, and inverse matrices (plus some input-checking helper functions).

### Installation
```
pip install linalg-basic
pip install linalg-deluxe
```

### Get started
The following code walks through just a few of the library's features:
```
from linalg_deluxe.linalg_deluxe import transpose, multiply_matrix_vector, symmetric, inverse_matrix

# Create a Vector and a Matrix (the two data types the library runs on)
v = [1, 2, 3]
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose v and m
v_vertical = transpose(v)
m_transposed = transpose(m)

# Multiply m by v
m_x_v = multiply_matrix_vector(m, v)

# Is m symmetric?
m_sym = symmetric(m)

# Attempt to generate m's inverse
# This will fail, because m's determinant is not zero in this case
m_inv = inverse_matrix(m)
```