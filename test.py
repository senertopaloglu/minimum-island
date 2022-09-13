import unittest
import solution


class TestCalc(unittest.TestCase):
    def test_0(self):  # test_ prefix is required
        grid = [
          ['W', 'L', 'W', 'W', 'W'],
          ['W', 'L', 'W', 'W', 'W'],
          ['W', 'W', 'W', 'L', 'W'],
          ['W', 'W', 'L', 'L', 'W'],
          ['L', 'W', 'W', 'L', 'L'],
          ['L', 'L', 'W', 'W', 'W'],
        ]
        self.assertEqual(solution.minimum_island(grid), 2)

    def test_1(self):
        grid = [
          ['L', 'W', 'W', 'L', 'W'],
          ['L', 'W', 'W', 'L', 'L'],
          ['W', 'L', 'W', 'L', 'W'],
          ['W', 'W', 'W', 'W', 'W'],
          ['W', 'W', 'L', 'L', 'L'],
        ]
        self.assertEqual(solution.minimum_island(grid), 1)
        
    def test_2(self):
        grid = [
          ['L', 'L', 'L'],
          ['L', 'L', 'L'],
          ['L', 'L', 'L'],
        ]
        self.assertEqual(solution.minimum_island(grid), 9)
        
    def test_3(self):
        grid = [
          ['W', 'W'],
          ['L', 'L'],
          ['W', 'W'],
          ['W', 'L']
        ]
        self.assertEqual(solution.minimum_island(grid), 1)

if __name__ == '__main__':
    unittest.main()
