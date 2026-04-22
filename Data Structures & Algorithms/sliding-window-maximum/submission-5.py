class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        output = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            left_boundary = r - k + 1

            if q[0] < left_boundary:
                q.popleft()

            if r >= k - 1:
                output.append(nums[q[0]])

        return output