
#1
def maxProfit(prices):
    n = len(prices)
    left = 0
    max_prof = 0
    for right in range(1, n):
        if prices[left] < prices[right]:
            profit = prices[right] -prices[left]
            max_prof = max(max_prof, profit)
        else:
            left +=1
    return max_prof

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices1))
print(maxProfit(prices2))

#2
def findMaxAverage (nums, k):
    n = len(nums)
    if n<k:
        return 0

    window = sum(nums[:k])
    max_sum = window

    for i in range (k, n):
        window += nums[i] - nums[i - k]
        max_sum = max(max_sum, window)

    return max_sum/k

nums = [1, 12, -5, -6, 50, 3]
k=4
print(findMaxAverage(nums, k))
