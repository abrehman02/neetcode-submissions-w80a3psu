class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1] * len(s)
        def rec(i):
            #prunning

            #baseCase
            if i == len(s):
                return 1
            #cacheCheck
            if dp[i] != -1 :
                return dp[i]
            #Transition
            ans = 0

            if s[i] != '0':
                one_dig_ans = rec(i+1)
                two_dig_ans = 0
                if i + 1 < len(s) and s[i] + s[i+1] < '27' :
                    two_dig_ans = rec(i+2)
                ans = one_dig_ans + two_dig_ans

            #saveAndReturn
            dp[i] = ans
            return ans
        
        return rec(0)
