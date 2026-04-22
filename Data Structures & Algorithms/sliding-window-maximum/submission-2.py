class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNumArr = []
        for l in range(len(nums) - k + 1):
            window = nums[l:k]
            maxNumArr.append(max(window))
            k += 1

        return maxNumArr
