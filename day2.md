# Day 2 

- [x] Task: LC977, LC209, LC59

## LC 977: Squares of a Sorted Array
Description: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Ideal: 
* Since this is a non-decreasing array, the beginning and the end will be the greast value whole array. 

* So first step is to find the biggest value
* And we repeat this process again til two pointer touch together
* nums = [-4,-1,0,3,10] -> [16,1,0,9,100] -> [0,1,9,16,100]

Brute force: square each of the element in the array, and sort the whole array

__Time complexity__: O(n + nlogn) or O(nlogn) depends on the sort algorithm. 

If we are using two pointer to deal with it, it may be __O(n)__


## LC 209 Minimum Size Subarray Sum

Description: Given an array of positive integers nums and a positive integer target, return the minimal length of a __subarray__ whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

### Ideal: Sliding window

~~Brutal force: Two for loop, keep looking for subsequences that meet the conditions. __Time complexity__: O(n^2)~~

Sliding window: Continuously adjust the start and end positions of the subsequence to get the result we want.

* What's in the window?
* How to move the start position? (first pointer)
* How to move the end position? (second pointer)

##### How to move the window?

The window is the smallest continuous subarray of length that satisfies the its total sum greater than or equal s (sum >= s)

Start position: If the sum of the window greater than s, then the start pointer need to move forward

End position: Keep travesal the array

__Time Complexity:__ O(n)

__Space Complexity:__ O(1)


```Python3
class Solution(object):
    def minSubArrayLen(self, target, nums):
        #起始位置；终止位置
        i = 0
        j = 0
        size = len(nums)
        sum_v = 0
        ans = float("inf")
        for j in range(size):
            sum_v += nums[j]
            while sum_v >= target:
                ans = min(ans, j-i+1)
                sum_v -= nums[i]
                i += 1
        if ans == float("inf"):
            return 0 
        else:
            return ans
```

#### LC 59
Description: Given a positive integer n, generate an n x n __matrix__ filled with elements from 1 to n2 in spiral order. 

### Ideal: 
* 循环--转多少次
*  判断左闭右开还是左闭右闭（区间的定义），只处理第一个节点 不处理最后一个节点

```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [[0] * n for i in range(n)]
        startx = starty = 0
        loop = mid = n // 2
        count = 1

        # 每循环一层偏移量加1，偏移量从1开始
        for offset in range(1, loop+1):
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1                
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count 
        return nums
```





