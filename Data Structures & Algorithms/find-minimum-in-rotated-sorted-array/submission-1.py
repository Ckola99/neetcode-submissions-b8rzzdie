class Solution:
    def findMin(self, nums: List[int]) -> int:
        # (log n) Binary search

        # we need pointers
        l,r = 0, len(nums) - 1
        minNum = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                minNum = min(nums[l], minNum)
                break

            mid = (l + r) // 2
            minNum = min(minNum, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return minNum