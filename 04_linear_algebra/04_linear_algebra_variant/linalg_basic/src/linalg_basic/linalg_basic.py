"""This is 04_linear_algebra_vanilla copied and pasted, with deletions, documentation, reformatting, and other minor
alterations to optimize it for use as a library for the chapter project.

Since this library was largely copied from the book, I haven't bothered writing tests for it like I have done for the
code I've written myself (which I've written through full TDD)."""

import math
from typing import Callable

"""A pair of simple type declarations used throughout this library."""
Vector = list[float]
Matrix = list[Vector]  # This, the book's definition of a Matrix, includes column vectors and ragged lists,
# unhelpfully. Accordingly, I routinely handle such conditions in my code.


def add(v: Vector, w: Vector) -> Vector:
    """Add the corresponding elements of each of the two Vectors.

    Parameters
    ----------
    v
        The first Vector to add.
    w
        The second Vector to add.

    Returns
    -------
    Vector
        The sum of v and w.

    """
    assert len(v) == len(w), "Vectors must be of identical length."
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Subtract each element of the second input Vector from its corresponding element in the first input Vector.

    Parameters
    ----------
    v
        The Vector to be subtracted from.
    w
        The Vector to subtract from v.

    Returns
    -------
    Vector
        The result of the subtraction.

    """
    assert len(v) == len(w), "Vectors must have equal length."
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: list[Vector]) -> Vector:
    """Sum a list of Vectors component-wise.

    Parameters
    ----------
    vectors
        A list of Vectors of equal length.

    Returns
    -------
    Vector
        The component-wise sum of the input list.

    """
    assert vectors, "Please provide a valid list of vectors."  # Check for invalid input
    num_dims = len(vectors[0])  # Check the vectors are all the same size
    assert all(num_dims == len(v) for v in vectors), "The vectors must all be the same size."
    # The ith element of the result is the sum of every vector's ith element
    return [sum(v[i] for v in vectors) for i in range(num_dims)]


def scalar_multiply(vector: Vector, scalar: float) -> Vector:
    """Multiply a Vector by a scalar.

    Parameters
    ----------
    vector
        The Vector to be multiplied.
    scalar
        The scalar multiplying factor.

    Returns
    -------
    Vector
        The product of the two inputs.
    """
    assert vector and scalar, "Valid inputs, please."
    return [n * scalar for n in vector]


def vector_mean(vectors: list[Vector]) -> Vector:
    """Compute the component-wise means of a list of (same-sized) Vectors.

    Parameters
    ----------
    vectors
        A list of Vectors of equal length.

    Returns
    -------
    Vector
        The component-wise mean of the input list.
    """
    assert vectors, "Please provide a valid list of Vectors."
    return scalar_multiply(vector_sum(vectors), 1 / len(vectors))


def dot_product(v: Vector, w: Vector) -> float:
    """Compute the dot product of two vectors.

    Parameters
    ----------
    v
        The first Vector.
    w
        The second Vector.

    Returns
    -------
    float
        The dot product of the two Vectors.
    """
    assert len(v) == len(w), "Vectors must be same length."
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Compute the sum of squares of a Vector.

    Parameters
    ----------
    v
        The Vector whose sum of squares will be computed.

    Returns
    -------
    float
        The sum of squares of v.
    """
    return dot_product(v, v)


def magnitude(v: Vector) -> float:
    """Compute the magnitude of the input Vector.

    Parameters
    ----------
    v
        The Vector to compute the magnitude of.

    Returns
    -------
    float
        The magnitude of v.
    """
    return math.sqrt(sum_of_squares(v))


def vector_distance(v: Vector, w: Vector) -> float:
    """Compute the distance between the two input Vectors.

    Parameters
    ----------
    v
        The first input Vector.
    w
        The second input Vector.

    Returns
    -------
    float
        The distance between v and w.
    """
    return magnitude(subtract(v, w))


# Note: The book's error prevention for this method was odd and ineffective. I've implemented a conventional assert
# statement instead.
def shape(m: Matrix) -> tuple[int, int]:
    """Return the number of rows and the number of columns in the input Matrix.

    Parameters
    ----------
    m
        The Matrix.

    Returns
    -------
    tuple[int]
        A tuple of 2 quantities: the number of rows and the number of columns in m.
    """
    assert type(m) == list and type(m[0]) == list, "Please submit a Matrix."
    return len(m), len(m[0])


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """Returns a num_rows-by-num_cols Matrix whose (i, j)th entry is entry_fn(i, j).

    Parameters
    ----------
    num_rows
        The number of rows in the generated Matrix.
    num_cols
        The number of columns in the generated Matrix.
    entry_fn
        The function which generates each entry in the Matrix.

    Returns
    -------
    Matrix
        A Matrix assembled by applying entry_fn to each entry.
    """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Generate an n-by-n identity Matrix.

    Parameters
    ----------
    n
        The number of rows and columns in the Matrix.

    Returns
    -------
    Matrix
        The identity Matrix.
    """
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)
