class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        left=0
        right=n-1
        area =0
        while(left<=right):
            mini = min(height[left],height[right])
            currentArea=mini*(right - left)
            area = max(area,currentArea)
            if (height[left]<=height[right]):
                left+=1
            else:
                right-=1
        return area