class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_area=0

        while left<right:
            current_width=right-left
            current_height=min(height[left], height[right])
            current_area=(current_width)*(current_height)
            max_area=max(max_area , current_area)
            
            if height[right]>height[left]:
                left+=1
            else:
                right-=1

        return max_area




        