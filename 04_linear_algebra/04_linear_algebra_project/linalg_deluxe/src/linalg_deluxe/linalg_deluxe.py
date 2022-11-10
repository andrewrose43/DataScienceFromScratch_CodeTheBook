"""A collection of additional linear algebra functions to build upon the incomplete library provided by the book."""

from linalg_basic import *  # I know this is normally bad practice, but for this weird project which is an extension
# of Grus's work, it makes sense to treat these imports as simply another part of this library and thus allow them to
# share a namespace with the rest of the code.
from typing import Union
from math import acos


def matrix_ragged(m: Matrix) -> bool:
    """Helper function. Returns true if a Matrix is ragged.

    Parameters
    ----------
    m
        The Matrix to be checked for raggedness.

    Returns
    -------
    bool
        True if m is ragged; False if not.
    """
    col_count = len(m[0])
    return any(len(row) != col_count for row in m[1:])


def matrix_is_square(m: Matrix) -> bool:
    """Helper function. Checks that a Matrix is square. Assumes raggedness and non-emptiness have already been checked.

    Parameters
    ----------
    m
        The Matrix to be checked for squareness.

    Returns
    -------
    bool
        True if m is square; False if not.
    """
    return len(m) == len(m[0])


def matrix_truthy_square(m: Matrix) -> bool:
    """Runs all the input checking required for the functions which accept a single Matrix as a parameter.

    Parameters
    ----------
    m
        The Matrix to be analyzed.

    Returns
    -------
    bool
        True if the Matrix is truthy, non-ragged, and square. False otherwise.
    """
    result = m and m[0] and not matrix_ragged(m) and matrix_is_square(m)

    try:
        assert result
    except AssertionError:
        print("Please provide a non-empty, square Matrix.")

    return result


# This function would be a lot less annoying to code if the Vector type were a list of lists with one item each.
# Unfortunately, conversion to/from [] from/to [[]] requires some fiddling.
def transpose(m: Union[Vector, Matrix]) -> Union[Vector, Matrix]:
    """Transposes an input Vector or Matrix. Works on non-square Matrices, but not ragged Matrices.

    Parameters
    ----------
    m
        A Vector or Matrix to be transposed.

    Returns
    -------
    Union[Vector, Matrix]
        The transposed Vector or Matrix, or [[]] if the input was a ragged Matrix.

    """

    # Handle odd cases
    if m == [] or m == [[]]:
        return m

    # Case 1: Matrix
    if all((type(m[i]) == list for i in range(len(m)))):
        # Handle ragged Matrix case
        if matrix_ragged(m):
            return [[]]
        if len(m[0]) > 1:
            return [[m[row_ind][col_ind] for row_ind in range(len(m))] for col_ind in range(len(m[0]))]

        # Case 2: column Vector
        return [row[0] for row in m]

    # Case 3: row Vector
    return [[i] for i in m]


def symmetric(m: Matrix) -> bool:
    """Determines whether a Matrix is symmetric. Returns False if provided a non-square or ragged Matrix.

    Parameters
    ----------
    m
        The Matrix to be checked for symmetry.

    Returns
    -------
    bool
        True if m is symmetric; False otherwise.
    """

    # Handle odd case
    if m == [[]]:
        return True

    # If input is ragged or non-square, return False
    if matrix_ragged(m) or not matrix_is_square(m):
        return False

    # Note how cutting short the inner generator with range(row) prevents redundant comparisons
    return all((all((m[row][col] == m[col][row] for col in range(row))) for row in range(len(m))))


def multiply_matrix_vector(m: Matrix, v: Vector) -> Vector:
    """Multiplies a Matrix and a Vector together.

    Parameters
    ----------
    m
        The Matrix to be multiplied by v.
    v
        The Vector to be multiplied by m.

    Returns
    -------
    Vector
        The product of m and v.
    """

    # Handle empty parameters
    try:
        assert m != [[]] and v
        # Make sure ALL rows of the Matrix match the length of the Vector
        v_len = len(v)
        assert all((len(m[row_ind]) == v_len) for row_ind in range(len(m)))
    except AssertionError:
        print("Please provide non-empty inputs.")
        return []

    return [sum((v_i * m_i for v_i, m_i in zip(v, row))) for row in m]


def angle_vectors(v: Vector, w: Vector) -> float:
    """Calculates the angle between two vectors in radians.

    Parameters
    ----------
    v
        The first Vector.
    w
        The second Vector.

    Returns
    -------
    float
        The angle between v and w, in radians.
    """

    # Handle empty parameters
    try:
        assert v and w
    except AssertionError:
        print("Please provide non-empty inputs.")
        return -1

    return acos(dot_product(v, w)/(magnitude(v)*magnitude(w)))


def outer_product(v: Vector, w: Vector) -> Matrix:
    """Calculates the outer product of two vectors.

    Parameters
    ----------
    v
        The first Vector.
    w
        The second Vector.

    Returns
    -------
    Matrix
        The outer product of v and w.
    """

    # Handle empty parameters
    try:
        assert v and w
    except AssertionError:
        print("Please provide non-empty inputs.")
        return [[]]

    return [[w_i*v_i for w_i in w] for v_i in v]


def cross_product(v: Vector, w: Vector) -> Vector:
    """Calculates the cross product of two 3D vectors.

    Parameters
    ----------
    v
        The first Vector.
    w
        The second Vector.

    Returns
    -------
    Vector
        The cross product of v and w.
    """
    # Handle empty or wrong-length parameters
    try:
        assert v and w
        assert len(v) == len(w) == 3
    except AssertionError:
        print("Please provide non-empty inputs of length 3.")
        return []

    return [v[1]*w[2]-v[2]*w[1],
            v[2]*w[0]-v[0]*w[2],
            v[0]*w[1]-v[1]*w[0]]


def multiply_matrices(m: Matrix, n: Matrix) -> Matrix:
    """Multiplies two Matrices.

    Parameters
    ----------
    m
        The first Matrix.
    n
        The second Matrix.

    Returns
    -------
    Matrix
        The product of the two Matrices, or [[]] if the input was invalid.
    """

    # Handle bad inputs
    try:
        # Check that m and n are valid and non-empty
        # Check for valid, non-empty, non-ragged inputs
        # Check that there are as many columns in m as there are rows in n
        assert m and n and m[0] and n[0] \
               and not matrix_ragged(m) and not matrix_ragged(n) \
               and len(m[0]) == len(n)
    except AssertionError:
        print("Please provide non-empty, non-ragged inputs such that the first Matrix has as many columns as the "
              "second Matrix has rows.")
        return [[]]

    n_cols = tuple(zip(*n))  # Extract and cache the columns to avoid redundant calculation
    return [[dot_product(m_row, n_col) for n_col in n_cols] for m_row in m]


def determinant(m: Matrix) -> Union[float, None]:
    """Compute the determinant of a Matrix.

    Parameters
    ----------
    m
        The Matrix to calculate the determinant of.

    Returns
    -------
    Union[float, None]
        The determinant of m, or None if the input was invalid.
    """

    # Check validity of input just once instead of recursively
    if not matrix_truthy_square(m):
        return None

    def _determinant(_m: Matrix) -> float:
        # """Recursive core of determinant()."""

        # Base case
        if len(_m) == 1:
            return _m[0][0]

        result = 0

        for row_ind in range(len(_m)):
            _m_tmp = _m[:row_ind] + _m[row_ind+1:]  # m with the current row removed
            result += (_m[row_ind][0] * (((row_ind % 2)*-2)+1)  # multiplying factor
                       * _determinant([_m_tmp[row_ind_tmp][1:] for row_ind_tmp in range(len(_m_tmp))]))  # recur

        return result

    return _determinant(m)


def adjoint(m: Matrix) -> Matrix:
    """Calculate the adjoint of a square Matrix.

    Parameters
    ----------
    m
        The Matrix to calculate the adjoint of.

    Returns
    -------
    Matrix
        The adjoint of m, or [[]] if the input was invalid.
    """

    # Check validity of input
    if not matrix_truthy_square(m):
        return [[]]

    # A mathematical fact: the adjoint of any 1x1 matrix is [[1]]
    if len(m) == 1:
        return [[1]]

    width = len(m[0])  # Cached for fast use later
    result = [[] for _ in range(len(m))]  # To be gradually appended to

    for row_ind in range(len(m)):
        m_tmp = m[:row_ind] + m[row_ind+1:]  # m_tmp = m with the current row removed
        for col_ind in range(width):
            # add on one determinant to the row
            result[row_ind].append(
                ((((row_ind+col_ind) % 2) * -2)+1) *  # 1 or -1
                determinant([(m_tmp_row[:col_ind] + m_tmp_row[col_ind+1:]) for m_tmp_row in m_tmp])
                )

    return [list(col) for col in zip(*result)]  # Swap rows and columns


def inverse_matrix(m: Matrix) -> Matrix:
    """Calculate the inverse of a Matrix.

    Parameters
    ----------
    m
        The Matrix to calculate the inverse of.

    Returns
    -------
    Matrix
        The inverse of m, or [[]] if the input was invalid.
    """

    # Check validity of input
    if not matrix_truthy_square(m):
        return [[]]

    # Handle zero-determinant case
    try:
        assert determinant(m)
    except AssertionError:
        print("Please provide a Matrix with a nonzero determinant.")
        return [[]]

    det_div = 1/determinant(m)
    return [scalar_multiply(row, det_div) for row in adjoint(m)]
