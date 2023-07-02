from typing import List


class ArrSolution:
    # Optimal solution for O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, value in enumerate(nums):
            if target - value in values:
                return [values[target - value], idx]
            else:
                values[value] = idx
            

    def subtract2int(self, a, b : int) -> int:
        return b -a