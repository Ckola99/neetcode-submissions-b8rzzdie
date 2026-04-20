class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sortedNums = sorted(set(nums))
        longestStreak = 1
        currentStreak = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] == sortedNums[i - 1] + 1:
                currentStreak += 1
            else:
                longestStreak = max(longestStreak, currentStreak)
                currentStreak = 1

        return max(longestStreak, currentStreak)