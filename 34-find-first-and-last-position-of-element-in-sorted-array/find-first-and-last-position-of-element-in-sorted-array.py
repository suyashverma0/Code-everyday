class Solution:
    def lowerBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def upperBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        lb = self.lowerBound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = self.upperBound(nums, target)

        return [lb, ub - 1]