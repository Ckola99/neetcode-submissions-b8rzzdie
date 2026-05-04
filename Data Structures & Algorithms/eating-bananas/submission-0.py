class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if self.hoursNeeded(piles, mid) <= h:
                r = mid - 1    
            else:
                l = mid + 1  
        return l

    def hoursNeeded(self, piles, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
        return total