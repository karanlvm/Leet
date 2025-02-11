"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

The idea is to use to pointers left and right to check if the adjacent plots are empty or not and also handle cases
for the first and last plot and keep incrementing a "vacant" variable to keep track of the number of empty plots.
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        bed_len = len(flowerbed)
        vacant = 0

        for i in range(bed_len):
            if flowerbed[i] == 0:
                left = (i == 0) or (flowerbed[i-1] == 0)
                right = (i == bed_len-1) or (flowerbed[i+1] == 0)

                if left and right:
                    vacant += 1
                    flowerbed[i] = 1
        if n > vacant:
            return False
        return True