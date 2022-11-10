from unittest import TestCase
from src.linalg_deluxe.linalg_deluxe import *
from math import isclose, pi


class LinAlgDeluxeTests(TestCase):

    # transpose()

    def test_transpose_012_v(self):
        """Test transpose() on a simple vertical array."""
        self.assertEqual([0, 1, 2], transpose([[0], [1], [2]]))

    def test_transpose_012_h(self):
        """Test transpose() on a simple horizontal array."""
        self.assertEqual([[0], [1], [2]], transpose([0, 1, 2]))

    def test_transpose_1234_m(self):
        """Test transpose() on a simple Matrix."""
        self.assertEqual([[1, 2], [3, 4]], transpose([[1, 3], [2, 4]]))

    def test_transpose_nonsquare(self):
        """Test transpose() on a nonsquare Matrix."""
        self.assertEqual([[1, 2], [3, 4], [5, 6]], transpose([[1, 3, 5], [2, 4, 6]]))

    def test_transpose_empty_m(self):
        """Test transpose() on an empty Matrix."""
        self.assertEqual([[]], transpose([[]]))

    def test_transpose_empty_v(self):
        """Test transpose() on an empty Vector."""
        self.assertEqual([], transpose([]))

    def test_transpose_ragged_1(self):
        """Attempt to transpose a ragged Matrix."""
        self.assertEqual([[]], transpose([[1, 3, 5], [2, 6]]))

    def test_transpose_ragged_2(self):
        """Attempt to transpose a ragged Matrix."""
        self.assertEqual([[]], transpose([[1], [2], [3, 3]]))

    # symmetric()

    def test_symmetric_false_simple(self):
        """Test symmetric() on a 2x2 asymmetric Matrix."""
        self.assertFalse(symmetric([[1, 5], [1, 5]]))

    def test_symmetric_true_simple(self):
        """Test symmetric() on a 2x2 symmetric Matrix."""
        self.assertTrue(symmetric([[1, 5], [5, 1]]))

    def test_symmetric_false_big_even(self):
        """Test symmetric() on a 4x4 asymmetric Matrix."""
        self.assertFalse(symmetric([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))

    def test_symmetric_true_big_even(self):
        """Test symmetric() on a 4x4 symmetric Matrix."""
        self.assertTrue(symmetric([[1, 2, 3, 4], [2, 1, 5, 6], [3, 5, 1, 7], [4, 6, 7, 1]]))

    def test_symmetric_false_big_odd(self):
        """Test symmetric() on a 5x5 asymmetric Matrix."""
        self.assertFalse(symmetric([[1, 9001, 3, 4, 5],
                                    [2, 1, 6, 7, 8],
                                    [3, 6, 1, 9, 10],
                                    [4, 7, 9, 1, 11],
                                    [5, 8, 10, 11, 1]]))

    def test_symmetric_true_big_odd(self):
        """Test symmetric() on a 5x5 symmetric Matrix."""
        self.assertTrue(symmetric([[1, 2, 3, 4, 5],
                                   [2, 1, 6, 7, 8],
                                   [3, 6, 1, 9, 10],
                                   [4, 7, 9, 1, 11],
                                   [5, 8, 10, 11, 1]]))

    def test_symmetric_nonsquare(self):
        """Test symmetric() on a non-square Matrix."""
        self.assertFalse(symmetric([[1, 2, 3], [1, 2, 3]]))

    def test_symmetric_empty(self):
        """Test symmetric() on an empty Matrix."""
        self.assertTrue(symmetric([[]]))

    def test_symmetric_false_ragged(self):
        """Test symmetric() on a ragged Matrix."""
        self.assertFalse(symmetric([[1, 2, 3, 4, 5],
                                    [2, 1, 6, 7, 8, 0],
                                    [3, 6, 1, 9, 10],
                                    [4, 7, 9, 1, 11],
                                    [5, 8, 10, 11, 1]]))

    # multiply_matrix_vector

    def test_multiply_m_v_simple(self):
        """Multiply a single-item Matrix with a single-item Vector."""
        self.assertEqual(multiply_matrix_vector([[2]], [1]), [2])

    def test_multiply_m_v_less_simple(self):
        """Multiply a 2x2 Matrix by a 2D Vector."""
        self.assertEqual(multiply_matrix_vector([[1, 2], [3, 4]], [1, 2]), [5, 11])

    def test_multiply_m_v_big(self):
        """Multiply a 2x3 Matrix with a 3D Vector."""
        self.assertEqual(multiply_matrix_vector([[1, 2, 3], [4, 5, 6]], [1, 2, 3]), [14, 32])

    def test_multiply_m_v_empty_matrix(self):
        """Attempt to multiply an empty Matrix by a non-empty Vector."""
        self.assertEqual(multiply_matrix_vector([[]], [1, 2]), [])

    def test_multiply_m_v_empty_vector(self):
        """Attempt to multiply a non-empty Matrix by an empty Vector."""
        self.assertEqual(multiply_matrix_vector([[1, 2], [3, 4]], []), [])

    def test_multiply_m_v_ragged_matrix(self):
        """Attempt to multiply a ragged Matrix by a Vector."""
        self.assertEqual(multiply_matrix_vector([[1, 2, 3], [4, 5]], [1, 2, 3]), [])

    # vectors_angle()

    def test_vectors_angle_simple_1(self):
        """Measure angle between two 2D Vectors which point in the same direction (i.e. 0 radians)."""
        # abs_tol parameter is needed to compare to zero, since rel_tol works as a % of the larger of the two values
        # and thus would only work if set to 1 or greater in this case
        self.assertTrue(isclose(0, angle_vectors([55, 55], [1, 1]), abs_tol=0.0000001))

    def test_vectors_angle_simple_2(self):
        """Measure the angle between two Vectors pi radians apart."""
        self.assertTrue(isclose(pi, angle_vectors([-1, 0], [80, 0])))

    def test_vectors_angle_realistic_2d(self):
        """Measure the angle between two arbitrary 2D Vectors."""
        self.assertTrue(isclose(1.5551725981744, angle_vectors([24, -90], [8, 2])))

    def test_vectors_angle_realistic_4d(self):
        """Measure the angle between two arbitrary 4D Vectors."""
        self.assertTrue(isclose(2.8913967331672, angle_vectors([1, 2, 3, 4], [-5, -6, -7, -8])))

    # outer_product()

    def test_outer_product_simple(self):
        """Generate the outer product of two 2D Vectors."""
        self.assertEqual(
            outer_product([1, 2], [3, 4]),
            [[3, 4], [6, 8]]
        )

    def test_outer_product_uneven(self):
        """Generate the outer product of a 2D Vector and a 3D Vector."""
        self.assertEqual(
            outer_product([1, 2], [3, 4, 5]),
            [[3, 4, 5], [6, 8, 10]]
        )

    def test_outer_product_empty_1(self):
        """Attempt to generate the outer product of a 2D Vector and an empty Vector."""
        self.assertEqual(
            outer_product([1, 2], []),
            [[]]
        )

    def test_outer_product_empty_2(self):
        """Attempt to generate the outer product of a 2D Vector and an empty Vector, in reverse order."""
        self.assertEqual(
            outer_product([], [1, 2]),
            [[]]
        )

    def test_outer_product_single(self):
        """Generate the outer product of two 1D Vectors."""
        self.assertEqual(
            outer_product([3], [4]),
            [[12]]
        )

    # cross_product()

    def test_cross_product_1(self):
        """Basic cross product test #1."""
        self.assertEqual(
            cross_product([2, 3, 4], [5, 6, 7]),
            [-3, 6, -3]
        )

    def test_cross_product_2(self):
        """Basic cross product test #2."""
        self.assertEqual(
            cross_product([2, -4, 4], [4, 0, 3]),
            [-12, 10, 16]
        )

    def test_cross_product_empty(self):
        """Attempt to make a cross product with one of the Vectors empty."""
        self.assertEqual(
            cross_product([], [4, 0, 3]),
            []
        )

    def test_cross_product_wrong_length(self):
        """Attempt to make a cross product with one of the Vectors having too many dimensions."""
        self.assertEqual(
            cross_product([1, 2, 3, 4], [4, 0, 3]),
            []
        )

    # multiply_matrices()

    def test_multiply_matrices_2x2(self):
        """Multiply a 2x2 Matrix by a 2x2 Matrix."""
        self.assertEqual(
            multiply_matrices(
                [[1, 2], [3, 4]],
                [[5, 6], [8, 9]]
            ),
            [[21, 24],
             [47, 54]]
        )

    def test_multiply_matrices_uneven(self):
        """Multiply a 2x2 Matrix by a 2x3 Matrix."""
        self.assertEqual(
            multiply_matrices(
                [[1, 2], [3, 4]],
                [[5, 6, 7], [8, 9, 10]]
            ),
            [[21, 24, 27],
             [47, 54, 61]]
        )

    def test_multiply_matrices_ragged(self):
        """Attempt to multiply a 2x2 Matrix by a ragged Matrix."""
        self.assertEqual(
            multiply_matrices(
                [[1, 2], [3, 4]],
                [[5, 6, 7], [8, 9, 10, 11]]
            ),
            [[]]
        )

    def test_multiply_matrices_mismatch(self):
        """Attempt to multiply a 2x3 Matrix by a 2x2 Matrix."""
        self.assertEqual(
            multiply_matrices(
                [[5, 6, 7], [8, 9, 10]],
                [[1, 2], [3, 4]]
            ),
            [[]]
        )

    def test_multiply_matrices_one_empty(self):
        """Attempt to multiply an empty Matrix by a non-empty Matrix."""
        self.assertEqual(
            multiply_matrices(
                [[5, 6, 7], [8, 9, 10]],
                [[]]
            ),
            [[]]
        )

    def test_multiply_matrices_both_empty(self):
        """Attempt to multiply two empty Matrices."""
        self.assertEqual(
            [[]],
            multiply_matrices(
                [[]],
                [[]]
            )
        )

    # matrix_truthy_square()
    # This is the function which checks the inputs of the next three functions.

    def test_matrix_truthy_square_ok(self):
        """Ensure that matrix_truthy_square returns True on truthy, square Matrices."""
        self.assertTrue(matrix_truthy_square([[1, 2], [3, 4]]))

    def test_matrix_truthy_square_falsy(self):
        """Ensure that matrix_truthy_square returns False on falsy inputs."""
        self.assertFalse(matrix_truthy_square([]))

    def test_matrix_truthy_square_empty(self):
        """Ensure that matrix_truthy_square returns False on empty Matrices."""
        self.assertFalse(matrix_truthy_square([[]]))

    def test_matrix_truthy_square_ragged(self):
        """Ensure that matrix_truthy_square returns False on ragged Matrices."""
        self.assertFalse(matrix_truthy_square([[1, 2, 3], [1, 2, 3, 4], [1, 2, 3]]))

    def test_matrix_truthy_square_nonsquare(self):
        """Ensure that matrix_truthy_square returns False on nonsquare Matrices."""
        self.assertFalse(matrix_truthy_square([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))

    # matrix_determinant()

    def test_determinant_1x1(self):
        """Calculate the determinant of a 1x1 Matrix."""
        self.assertEqual(
            11,
            determinant([[11]])
        )

    def test_determinant_2x2(self):
        """Calculate the determinant of a 2x2 Matrix."""
        self.assertEqual(
            -2,
            determinant([[1, 2], [3, 4]])
        )

    def test_determinant_3x3(self):
        """Calculate the determinant of a 3x3 Matrix."""
        self.assertEqual(
            -20,
            determinant([[4, -3, 5], [1, 0, 3], [-1, 5, 2]])
        )

    def test_determinant_4x4(self):
        """Calculate the determinant of a 4x4 Matrix."""
        self.assertEqual(
            0,
            determinant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )

    def test_determinant_falsy(self):
        """Attempt to calculate the determinant of a falsy input."""
        self.assertEqual(
            None,
            determinant([])
        )

    def test_determinant_empty(self):
        """Attempt to calculate the determinant of an empty Matrix."""
        self.assertEqual(
            None,
            determinant([[]])
        )

    def test_determinant_ragged(self):
        """Attempt to calculate the determinant of a ragged Matrix."""
        self.assertEqual(
            None,
            determinant([[1, 2, 3, 4, 1111], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )

    def test_determinant_nonsquare(self):
        """Attempt to calculate the determinant of a nonsquare Matrix."""
        self.assertEqual(
            None,
            determinant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        )

    # matrix_adjoint

    def test_adjoint_1x1(self):
        """Calculate the adjoint of a 1x1 Matrix."""
        self.assertEqual(
            [[1]],
            adjoint([[123]])
        )

    def test_matrix_adjoint_2x2(self):
        """Calculate the adjoint of a 2x2 Matrix."""
        self.assertEqual(
            [[4, -2], [-3, 1]],
            adjoint([[1, 2], [3, 4]])
        )

    def test_matrix_adjoint_3x3(self):
        """Calculate the adjoint of a 3x3 Matrix."""
        self.assertEqual(
            [[7, 3, -4], [-3, 1, 4], [-2, -10, 8]],
            adjoint([[3, 1, 1], [1, 3, -1], [2, 4, 1]])
        )

    def test_adjoint_falsy(self):
        """Attempt to calculate the adjoint of a falsy input."""
        self.assertEqual(
            [[]],
            adjoint([])
        )

    def test_adjoint_empty(self):
        """Attempt to calculate the adjoint of an empty Matrix."""
        self.assertEqual(
            [[]],
            adjoint([[]])
        )

    def test_adjoint_ragged(self):
        """Attempt to calculate the adjoint of a ragged Matrix."""
        self.assertEqual(
            [[]],
            adjoint([[1, 2, 3, 4, 1111], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )

    def test_adjoint_nonsquare(self):
        """Attempt to calculate the adjoint of a nonsquare Matrix."""
        self.assertEqual(
            [[]],
            adjoint([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        )

    # inverse_matrix

    def test_inverse_matrix_2x2(self):
        """Calculate the inverse of a 2x2 Matrix."""
        n = 2  # Side length
        original = [[1, 2], [3, 4]]
        inv = [[-2, 1], [1.5, -0.5]]
        result = inverse_matrix(original)
        self.assertTrue(
            all(
                ((isclose(inv[row][col], result[row][col]) for col in range(n)) for row in range(n))
            )
        )

    def test_inverse_matrix_3x3(self):
        """Calculate the inverse of a 3x3 Matrix."""
        n = 3  # Side length
        original = [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
        inv = [[1 / 9, -2 / 9, 1 / 9],
               [-2 / 9, -23 / 9, 16 / 9],
               [1 / 9, 22 / 9, -14 / 9]]
        result = inverse_matrix(original)
        self.assertTrue(
            all(
                ((isclose(inv[row][col], result[row][col]) for col in range(n)) for row in range(n))
            )
        )

    def test_inverse_matrix_4x4(self):
        """Calculate the inverse of a 4x4 Matrix."""
        n = 4  # Side length
        original = [[1, 0, 3, 4],
                    [1, 2, 3, 4],
                    [1, 0, -6, 4],
                    [0, 2, -4, 4]]
        inv = [[-7 / 9, 1, 7 / 9, -1],
               [-0.5, 0.5, 0, 0],
               [1 / 9, 0, -1 / 9, 0],
               [13 / 36, -.25, -1 / 9, .25]]
        result = inverse_matrix(original)
        self.assertTrue(
            all(
                ((isclose(inv[row][col], result[row][col]) for col in range(n)) for row in range(n))
            )
        )

    def test_inverse_matrix_zero_determinant(self):
        """Attempt to calculate the inverse of a Matrix with a determinant equal to zero."""
        self.assertEqual(
            [[]],
            inverse_matrix([[1, 1], [1, 1]])
        )

    def test_inverse_matrix_falsy(self):
        """Attempt to calculate the inverse Matrix of a falsy input."""
        self.assertEqual(
            [[]],
            inverse_matrix([])
        )

    def test_inverse_matrix_empty(self):
        """Attempt to calculate the inverse Matrix of an empty Matrix."""
        self.assertEqual(
            [[]],
            inverse_matrix([[]])
        )

    def test_inverse_matrix_ragged(self):
        """Attempt to calculate the inverse Matrix of a ragged Matrix."""
        self.assertEqual(
            [[]],
            inverse_matrix([[1, 2, 3, 4, 1111], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        )

    def test_inverse_matrix_nonsquare(self):
        """Attempt to calculate the inverse Matrix of a nonsquare Matrix."""
        self.assertEqual(
            [[]],
            inverse_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        )
