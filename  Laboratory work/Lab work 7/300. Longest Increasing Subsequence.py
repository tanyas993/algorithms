class Solution(object):
    def lengthOfLIS(self, nums):
        """:type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sub = []
        for num in nums:
            left = 0
            right = len(sub)
            while left < right:
                mid = (left + right) // 2
                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            idx = left
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)