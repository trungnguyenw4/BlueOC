import unittest

def sum_of_two_largest(nums):
    if len(nums) < 2:
        raise ValueError("The array must contain at least two elements.")
    
    # Find the two largest integers
    first_max = max(nums)
    nums.remove(first_max)  # Remove the first maximum element
    second_max = max(nums)  # Find the next maximum element
    
    return first_max + second_max

# Test cases
print(sum_of_two_largest([1, 4, 2, 3, 5])) # 9
print(sum_of_two_largest([10, 20, 30, 40, 50])) # 90
print(sum_of_two_largest([-10, -20, -30, -40, -50])) # -30
print(sum_of_two_largest([1, 1, 1, 1, 1])) # 2
print(sum_of_two_largest([0, 0, 0, 0, 1])) # 1




class TestSumOfTwoLargest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_of_two_largest([1, 4, 2, 3, 5]), 9)

    def test_case_2(self):
        self.assertEqual(sum_of_two_largest([10, 20, 30, 40, 50]), 90)

    def test_case_3(self):
        self.assertEqual(sum_of_two_largest([-10, -20, -30, -40, -50]), -30)

    def test_case_4(self):
        self.assertEqual(sum_of_two_largest([1, 1, 1, 1, 1]), 2)

    def test_case_5(self):
        self.assertEqual(sum_of_two_largest([0, 0, 0, 0, 1]), 1)

    def test_case_6(self):
        with self.assertRaises(ValueError):
            sum_of_two_largest([5])  # Array with less than 2 elements

if __name__ == '__main__':
    unittest.main()
