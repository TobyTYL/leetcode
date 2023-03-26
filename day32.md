# Day 32

- [x] LC 122, 55, 45

# LC 122. Best Time to Buy and Sell Stock II

Description: 

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
```

Ans:

``` py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_v = 0
        for i in range(1, len(prices)):
            gap = prices[i]-prices[i-1]
            if gap > 0:
                max_v += gap
        return max_v
```

# LC 55. Jump Game

Description:

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Ans:

``` py
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                # 比较经过的步数中哪个数字最大
                cover = max(i + nums[i], cover)
                # 假设可以覆盖最后一个数字
                if cover >= len(nums) - 1: return True
        return False
```


# LC 45. Jump Game II

Description:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Ans:

```py
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        cover = 0
        for i in range(len(nums)):
            cover = max(i + nums[i], cover)
            # i 等于最大的移动范围的位置了
            if i == curDistance: 
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = cover
                    if cover >= len(nums) - 1: 
                        break
        return ans
```