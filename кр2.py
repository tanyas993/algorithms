def sortedSquares(nums):
    left, right = 0, len(nums)-1
    while left < right:
        nums[left] = abs(nums[left])**2
        nums[right] = abs(nums[right])**2
        left+=1
        right-=1
    return sorted(nums)

nums = [-4, -1, 0, 3, 10]

print(sortedSquares(nums))

def isAnagram( s, t):
    return sorted(s) == sorted(t)

s1 = 'anagram'
t1 = 'nagaram'
print (isAnagram( s1, t1))

s2 = 'car'
t2 = 'rat'
print(isAnagram( s2, t2))




