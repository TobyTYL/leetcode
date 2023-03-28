# Day 36

- [x] LC 435, 763, 56

# LC 435. Non-overlapping Intervals

Description:
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```


Ans:

```py
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count = 0
        if len(intervals) == 0:
            return 0
        # list中第一个数字
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        for i in range(1, len(intervals)):
            # interval list index 为1的数字
            print(intervals[i])
            if intervals[i][0] < intervals[i-1][1]:
                count += 1
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
            print("diff",intervals[i])
        return count
```

# LC 763. Partition Labels

Description:

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

## Ideal:
<img src =https://code-thinking-1253855093.file.myqcloud.com/pics/20201222191924417.png>

Ans:
```py
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hash = [0] * 26
        # 记录位置
        for i in range(len(s)):
            # 最远处出现的元素的下标会将前面经历过下标给覆盖
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
```

# LC 56. Merge Intervals

Description:

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

Ans:
```py
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0: return intervals
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            # list 中最后一个元素
            last = result[-1]
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result

```
