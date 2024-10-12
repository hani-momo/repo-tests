'''
Merge sort
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0  # start indices

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    if left:
        sorted_arr += left[i:]
    if right:
        sorted_arr += right[j:]
    
    return sorted_arr

'''
Tests
'''
import unittest

class TestMergeSort(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_one_element_in_array(self):
        self.assertEqual(merge_sort([0]), [0])

    def test_unsorted_array(self):
        unsorted_array = [5, 3, 4, 2, 0, 1]
        self.assertEqual(merge_sort(unsorted_array), sorted(unsorted_array))

'''
Run Tests
'''
if __name__ == "__main__":
    unittest.main()

