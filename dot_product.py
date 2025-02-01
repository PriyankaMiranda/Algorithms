class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        print(self.nums)
        print(vec.nums)
        i=0
        ans = 0
        for elem in self.nums:
            ans = ans + elem*vec.nums[i]
            i += 1
        return ans

# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)