# Day 37

- [x] LC 738

# LC 738. Monotone Increasing Digits

Description:

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

Example:
```
Input: n = 10
Output: 9
```

## Ideal: 
*本题只要想清楚个例，例如98，一旦出现strNum[i - 1] > strNum[i]的情况（非单调递增），首先想让strNum[i - 1]减一，strNum[i]赋值9，这样这个整数就是89。就可以很自然想到对应的贪心解法了。

想到了贪心，还要考虑遍历顺序，只有从后向前遍历才能重复利用上次比较的结果。

最后代码实现的时候，也需要一些技巧，例如用一个flag来标记从哪里开始赋值9。


Ans:
```py
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = list(str(n))
        # 倒着for loop
        for i in range(len(a)-1,0,-1):
            print(a[i])
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)  #python不需要设置flag值，直接按长度给9就好了
        return int("".join(a)) 
```
