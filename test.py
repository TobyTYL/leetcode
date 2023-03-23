# We will call a sequence of integers a spike if they first increase (strictly) and then decrease (also strictly, including the last element of t increasing part).
# For example(4, 5, 7, 6, 3, 2) is a spike, but(1, 1, 5, 4, 3) and (1, 4, 3, 5) are not.
#  Note that the increasing and decreasing parts always intersect, e.g.: for spike(3, 5, 2) sequence(3, 5) is an increasing part and sequence(5, 2) is a decreasing part, and for spik (2) sequence(2) is both an increasing and a decreasing part.
# Your are given an array A of N integers. Your task is to calculate the length of the longest possible spike, which can be created from numbers from array A. Note that you are NOT supposed to find the longest spike as a sub-sequence of A, but rather choose some numbers from A and reorder them to create the longest spike.

def solution(lst):
