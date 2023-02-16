# Day 1 
- [x] Task: LC 704, LC 27

Elements of an array cannot be deleted, they can only be overwritten.

### LC 704: Binary search

#### Use binary search: 数组为有序数组，同时题目还强调数组中无重复元素。

写二分法经常写乱，主要是因为对区间的定义没有想清楚，区间的定义就是不变量。要在二分查找的过程中，保持不变量，就是在while寻找中每一次边界的处理都要坚持根据区间的定义来操作，这就是循环不变量规则。

写二分法，区间的定义一般为两种:
左闭右闭即 [left, right]
左闭右开即 [left, right)

1. 左闭右闭 [left, right]
第一种写法，我们定义 target 是在一个在左闭右闭的区间里，也就是[left, right] （这个很重要非常重要）。

区间的定义这就决定了二分法的代码应该如何写，因为定义target在[left, right]区间，所以有如下两点：

while (left <= right) 要使用 <= ，因为left == right是有意义的，所以使用 <=
if (nums[middle] > target) right 要赋值为 middle - 1，因为当前这个nums[middle]一定不是target，那么接下来要查找的左区间结束下标位置就是 middle - 1
例如在数组：1,2,3,4,7,9,10中查找元素2，如图所示：

<img  alt="Alt text" src="https://img-blog.csdnimg.cn/20210311153055723.jpg">

2. 左闭右开  [left, right)
如果说定义 target 是在一个在左闭右开的区间里，也就是[left, right) ，那么二分法的边界处理方式则截然不同。

有如下两点：

while (left < right)，这里使用 < ,因为left == right在区间[left, right)是没有意义的
if (nums[middle] > target) right 更新为 middle，因为当前nums[middle]不等于target，去左区间继续寻找，而寻找区间是左闭右开区间，所以right更新为middle，即：下一个查询区间不会去比较nums[middle]
在数组：1,2,3,4,7,9,10中查找元素2，如图所示：（注意和方法一的区别）

<img  alt="Alt text" src="https://img-blog.csdnimg.cn/20210311153123632.jpg">

### LC 27: Remove elements

target 为2
[2,2,3,3] -> [3,3, _, _] -> [3,3]
#### Idea: 双指针，慢的从0开始，当快指针指向的位置的值等于target时候。慢指针指向的地方的值 = 快指针指的地方的值。（覆盖而不是删除）

