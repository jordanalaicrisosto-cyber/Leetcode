from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        assert 1 <= len(nums) <= 10**5
        assert 0 <= k <= 10**5

        indices = []
        data_in = set()
        dernier_index = dict()

        for i in range(len(nums)) :
            assert -10**9 <= nums[i] <= nums[i]
            if not(nums[i] in data_in) :
                data_in.add(nums[i])
                dernier_index[nums[i]] = i
            else :
                for j in dernier_index.values() :
                    if nums[j] == nums[i] :
                        indices.append([i,j])
            dernier_index[nums[i]] = i

        for indice in indices :
            if abs(indice[0] - indice[1]) <= k :
                return True

        return False
