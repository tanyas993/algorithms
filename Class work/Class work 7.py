#69. Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid - 1
        return high

#35. Search Insert Position
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

