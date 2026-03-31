class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is maximise(minimize) kind of pattern means Binary Search

        def check(mid):
            time = 0
            for i in range(len(piles)):
                if piles[i] % mid != 0 :
                    time += piles[i] // mid + 1
                else:
                    time += piles[i] // mid
            return True if time <= h else False



        low = 0 
        high = max(piles)

        ans = -1

        while low <= high :
            mid = low + (high - low) // 2

            if mid != 0 and check(mid) :
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans