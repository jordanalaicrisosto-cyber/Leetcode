from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        assert 1 <= len(height) <= 10**4
        for high in height :
            assert 0 <= high <= 10**5

        unit_rain = 0
        for i in range(len(height) - 2) :
            if height[i] > height[i+1] and height[i+1] < height[i+2] :
                unit_rain += min(height[i], height[i+2]) - height[i+1]
        return unit_rain