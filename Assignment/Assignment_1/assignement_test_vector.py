import unittest
import math

from assignement1 import Vec


class TestVec(unittest.TestCase):

    def test_mean(self):
        v = Vec((1, 2, 3, 4, 5))

        self.assertEqual(v.mean(), 3.0)

    def test_mean_with_floats(self):
        v = Vec((1.5, 2.5, 3.5))

        self.assertAlmostEqual(v.mean(), 2.5)

    def test_demean(self):
        v = Vec((1, 2, 3, 4, 5))

        result = v.demean()

        expected = (-2.0, -1.0, 0.0, 1.0, 2.0)

        self.assertEqual(result.elements, expected)

    def test_demean_mean_is_zero(self):
        v = Vec((10, 20, 30))

        demeaned = v.demean()

        self.assertAlmostEqual(demeaned.mean(), 0.0)

    def test_demean_preserves_length(self):
        v = Vec((2, 4, 6, 8))

        demeaned = v.demean()

        self.assertEqual(
            len(v.elements),
            len(demeaned.elements)
        )

    def test_std(self):
        v = Vec((1, 2, 3, 4, 5))

        self.assertAlmostEqual(v.std(), math.sqrt(2))

    def test_std_constant_vector(self):
        v = Vec((5, 5, 5, 5))

        self.assertAlmostEqual(v.std(), 0.0)

    def test_std_non_negative(self):
        v = Vec((2, 5, 8, 10))

        self.assertGreaterEqual(v.std(), 0.0)


if __name__ == "__main__":
    unittest.main()