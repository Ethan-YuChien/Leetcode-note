# LC 496 – Next Greater Element I

## Problem Summary
Given two arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each element `nums1[i]`, find the **first element greater than it**
to the **right of its position in nums2**.
If none exists, return `-1`.
## note:
use stack for FIFO, compare number in nums2
Use map to query nums in nums1

# Count Triplets
## Problem Summary
You are given an array and you need to find number of tripets of indices`(i,j,k)` such that the elements at those indices are in geometric progression for a given common ratio`r`and`(i<j<k)`.
## note:
left -> num ->right