def countBits(self, n: int):
        return [format(i,'b').count('1') for i in range(n+1)]