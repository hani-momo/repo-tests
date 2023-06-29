import unittest

from sum import ArrSolution

"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You can return the answer in any order.

https://leetcode.com/problems/two-sum/

"""

class TestArr(unittest.TestCase):
    def setUp(self):
        self.solution = ArrSolution()

    def test_twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected_result = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

        nums = [3, 2, 4]
        target = 6
        expected_result = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

        nums = [3, 3]
        target = 6
        expected_result = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    ##  Next tasks from FAANG or LeetCode for arrays subject
    def test_OtherTask(self):
        self.assertEqual(self.solution.otherTask(1, 2), 3)
