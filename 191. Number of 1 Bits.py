def hammingWeight(self, n: int) -> int:
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
    
# return bin(n).count('1') #using inbuilt function bin()