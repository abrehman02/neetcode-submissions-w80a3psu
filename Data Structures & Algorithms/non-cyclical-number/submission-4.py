class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        num = 0
        while n:
            r = n % 10
            num += r*r
            n //= 10
            if n == 0 :
                if num == 1 :
                    return True
                else:
                    if num in hashset :
                        return False
                    else:
                        hashset.add(num)
                        n = num
                        num = 0
            # print(hashset)
        # return True
                
        
    


