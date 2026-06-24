class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minn = float('inf')
        
        while l <= r:
            mid = l + (r - l) // 2

            if self.iteratingOverBananas(mid, piles, h):
                minn = min(minn, mid)
                r = mid - 1
            
            else:
                l = mid + 1
        
        return minn
        
    def iteratingOverBananas(self, k, piles, h):
        counter = 0
        for pile in piles:
            counter += (pile + k - 1) // k

            if counter > h:
                return False

        return True