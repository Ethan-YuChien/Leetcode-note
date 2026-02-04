from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        key_dict = defaultdict(int)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                key_dict[smaller] = num
        while stack:
            key_dict[stack.pop()] = -1
        
        result = []
        for num in nums1:
            result.append(key_dict.get(num,-1))
        
        return result