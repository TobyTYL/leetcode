# Day 7
- [x] LC 454, 383, 15, 18

## LC 454. 4Sum II

Description: 
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

* 0 <= i, j, k, l < n
* nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

```
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
```

Ideal:

* 将四个list转换成两两相加
* hashmap中放入a和b两数之和
* 遍历c和d得到两数之和，然后取反
* 在hashmap中搜索是否有匹配项，假设有就加1


Ans:
```py
class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1+n2] += 1
                else:
                    hashmap[n1+n2] = 1
        
        # if the -(a+b) exists in nums3 and nums4, we shall add the count
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                key = - n3 - n4
                if key in hashmap:
                    count += hashmap[key]
        return count

```

## LC 383. Ransom Note

Descrption: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

Ideal:

* create a array to store the 26 letter
* simple logic in magazine and ransomNote (+1/-1)
* when you iterate the ransomNote, if there's 0 for some key, then return False




Ans:
```py
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = [0] * 26
        for i in magazine:
            note[ord(i) - ord('a')] += 1

        for i in ransomNote:
            if note[ord(i) - ord('a')] == 0:
                return False
            else:
                note[ord(i) - ord('a')] -= 1
        return True
```

## LC 15. 3Sum

Description: 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example:
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

Notice that the order of the output and the order of the triplets does not matter.


Ans:
```py

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        # sort the nums array
        nums.sort()
        # loop the array  
	    # 找出a + b + c = 0
        # a = nums[i], b = nums[left], c = nums[right]
        for i in range(n):
            left = i + 1
            right = n - 1
	    # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
        # 因为已经sort过了，所以后面的元素不可能比0小
            if nums[i] > 0: 
                break
            if i >= 1 and nums[i] == nums[i - 1]: # 去重a
                continue
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
		    # 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return ans
```

## LC 18. 4Sum

Description:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example:
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

__Ideal: Two pointers__
* 移动left 和right呢， 如果nums[i] + nums[left] + nums[right] > 0 就说明 此时三数之和大了，因为数组是排序后了，所以right下标就应该向左移动，这样才能让三数之和小一些。

* 如果 nums[i] + nums[left] + nums[right] < 0 说明 此时 三数之和小了，left 就向右移动，才能让三数之和大一些，直到left与right相遇为止。
Ans:

```py
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
       # 在三数之和上添加一个for loop 
        nums.sort()
        size = len(nums)
        ans = []
        # 数组顺序
        # i, k, left, ...., right
        for i in range(size):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue  # 对nums[i]去重
            for k in range(i+1, size):
                if k > i + 1 and nums[k] == nums[k-1]: 
                    continue  # 对nums[k]去重
                left = k + 1
                right = size - 1

                while left < right:
                    total = nums[i] + nums[left] + nums[right] + nums[k]
                    if total > target: 
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        ans.append([nums[i], nums[k], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]: 
                            left += 1
                        while left < right and nums[right] == nums[right - 1]: 
                            right -= 1

                        left += 1
                        right -= 1
        return ans
```

