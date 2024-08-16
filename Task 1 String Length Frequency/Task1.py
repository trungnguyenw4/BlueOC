from collections import Counter
from typing import List
import unittest

def most_frequent_string_lengths(strings: List[str]) -> List[str]:
    # Calculate the length of each string
    lengths = [len(s) for s in strings]
    
    # Count the frequency of each length
    length_counts = Counter(lengths)
    
    # Find the maximum frequency
    max_frequency = max(length_counts.values())
    
    # Find all lengths that have the maximum frequency
    most_frequent_lengths = [length for length, count in length_counts.items() if count == max_frequency]
    
    # Filter and return strings that have the most frequent lengths
    result = [s for s in strings if len(s) in most_frequent_lengths]
    
    return result

# Test cases
print(most_frequent_string_lengths(['a', 'ab', 'abc', 'cd', 'def', 'gh'])) # ['ab', 'cd', 'gh']
print(most_frequent_string_lengths(['apple', 'banana', 'cherry', 'date', 'fig'])) # ['banana', 'cherry']
print(most_frequent_string_lengths(['x', 'y', 'z'])) # ['x', 'y', 'z']
print(most_frequent_string_lengths(['hi', 'hello', 'hey', 'hola'])) # ['hi', 'hello', 'hey', 'hola']
print(most_frequent_string_lengths(['abc', 'def', 'ghi', 'jkl'])) # ['abc', 'def', 'ghi', 'jkl']



class TestMostFrequentStringLengths(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(most_frequent_string_lengths(['a', 'ab', 'abc', 'cd', 'def', 'gh']), ['ab', 'cd', 'gh'])

    def test_case_2(self):
        self.assertEqual(most_frequent_string_lengths(['apple', 'banana', 'cherry', 'date', 'fig']), ['banana', 'cherry'])

    def test_case_3(self):
        self.assertEqual(most_frequent_string_lengths(['x', 'y', 'z']), ['x', 'y', 'z'])

    def test_case_4(self):
        self.assertEqual(most_frequent_string_lengths(['hi', 'hello', 'hey', 'hola']), ['hello', 'hola'])

    def test_case_5(self):
        self.assertEqual(most_frequent_string_lengths(['abc', 'def', 'ghi', 'jkl']), ['abc', 'def', 'ghi', 'jkl'])

if __name__ == '__main__':
    unittest.main()