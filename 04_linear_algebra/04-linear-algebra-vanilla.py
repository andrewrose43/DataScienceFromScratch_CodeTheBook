
# Note: For this chapter, the exercises were simple enough that for most (not all) examples, I didn't find it
# worthwhile to do the usual regimen of repetition. I mostly just followed along with the chapter, sometimes creating
# functions from scratch on my own without reading the book's examples.


import math

# Let's make a simple Vector type.

Vector = list[float]

height_weight_age = [70,  # inches
                     170,  # pounds
                     40]  # years

grades = [95,  # exam 1
          80,  # exam 2
          75,  # exam 3
          62]  # exam 4


# Let's add some vectors.
def add(v: Vector, w: Vector) -> Vector:
    """Add corresponding elements"""
    assert len(v) == len(w), "Vectors must be of identical length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert (add([1, 2, 3], [4, 5, 6]) == [5, 7, 9])


# ...This is really basic. I'll write the next method blind without looking at the book or the above method, or the usual repetition/practice.

def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract each element of w from its corresponding element of v"""
    assert len(v) == len(w), "Vectors must have equal length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert (subtract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3])


# Componentwise sum a list of vectors.
def vector_sum(vectors: list[Vector]) -> Vector:
    """Component-wise sum a list of vectors."""
    # Check for invalid input
    assert vectors, "Please provide a valid list of vectors."

    # Check the vectors are all the same size
    num_dims = len(vectors[0])
    assert all(num_dims == len(v) for v in vectors), "The vectors must all be the same size."

    # the ith element of the result is the sum of every vector's ith element
    return [sum(v[i] for v in vectors) for i in range(num_dims)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


# Multiply a vector by a scalar.
def scalar_multiply(vector: Vector, scalar: float) -> Vector:
    assert vector and scalar, "Valid inputs please."
    return [n * scalar for n in vector]


assert [2, 4] == scalar_multiply([1, 2], 2)


# Use scalar_multiply and vector_sum to compute the component-wise means of a list of (same-sized) vectors.
def vector_mean(vectors: list[Vector]) -> Vector:
    assert vectors, "Please provide a valid list of vectors."
    return scalar_multiply(vector_sum(vectors), 1 / len(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot_product(v: Vector, w: Vector) -> float:
    '''Computes sum of component-wise products of the two input vectors.'''
    assert len(v) == len(w), "Vectors must be same length."
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot_product([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot_product(v, v)


assert sum_of_squares([2, 3]) == 13


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5


def vector_distance(v: Vector, w: Vector) -> float:
    """Computes distance between v and w"""
    return magnitude(subtract(v, w))


Matrix = list[list[float]]

# Note: The book's error prevention for this method was odd and ineffective. I've implemented a conventional assert
# statement instead.


def shape(m: Matrix):
    assert type(m) == list and type(m[0]) == list, "Please submit a Matrix"
    return len(m), len(m[0])


assert(shape([[1, 2], [3, 4], [5, 6]]) == (3, 2))


# Skipped the get_row and get_column methods because they are completely uninteresting.


from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Returns a num_rows-by-num_cols matrix whose (i, j)th entry is entry_fn(i, j).
    """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Returns an n-by-n identity matrix."""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
