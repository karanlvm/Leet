class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        answer = [1] * n

        left = 1
        # Left to right
        for i in range (n):
            answer[i] = left
            left *= nums[i]
        right = 1
        # Right to left
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer
