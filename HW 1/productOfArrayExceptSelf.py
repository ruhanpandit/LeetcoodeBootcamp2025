class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = [0]*len(nums)

        first = 1
        for i in range(len(nums)):
            array[i] = first
            first *= nums[i]

        second = 1
        for i in range(len(nums)-1, -1, -1):
            array[i] *= second
            second *= nums[i]
        
        return array