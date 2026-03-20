#1 1.Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        idx_nums = []
        for i in range(len(nums)):
            idx_nums.append([nums[i], i])
        idx_nums.sort()
        left, right = 0, len(nums) -1
        while left < right:
            curr = idx_nums[left][0] + idx_nums[right][0] #число 
            if curr == target:
                return [idx_nums[left][1], idx_nums[right][1]] #индекс
            elif curr < target:
                left +=1
            else:
                right -=1
        return None

#2 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

#3 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        sub = []
        max_len = 0
        for right in range(len(s)):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.append(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len

#4 11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            width = right - left
            cur_height = min(height[left], height[right])
            cur_area = width * cur_height
            max_water = max(max_water, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water



