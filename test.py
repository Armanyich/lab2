import unittest
from tetris_shift import shift_down

class TestTetrisShift(unittest.TestCase):

    def test_shift_down_basic(self):
        field = [
            [1, 1, 1],
            [0, 0, 0],
            [0, 0, 0]
        ]
        new_row = [1, 1, 1]
        result = shift_down(field, new_row)
        expected = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.assertEqual(result, expected)

    def test_shift_down_empty_field(self):
        field = []
        new_row = [1, 1, 1]
        result = shift_down(field, new_row)
        self.assertEqual(result, [[1, 1, 1]])

    def test_shift_down_different_row(self):
        field = [
            [5, 5],
            [3, 3],
        ]
        new_row = [9, 9]
        result = shift_down(field, new_row)
        expected = [
            [9, 9],
            [5, 5]
        ]
        self.assertEqual(result, expected)

    def test_shift_multiple_times(self):
        field = [
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        new_row = [1, 1]
        shift_down(field, new_row)
        shift_down(field, new_row)
        shift_down(field, new_row)
        expected = [
            [1, 1],
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(field, expected)
        
    def test_another_len(self):
        field = [
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        new_row = [1, 1, 1, 1]
        shift_down(field, new_row)
        expected = [
            [1, 1, 1, 1]
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(field, expected)

if __name__ == "__main__":
    unittest.main()
