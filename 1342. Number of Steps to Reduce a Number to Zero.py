def numberOfSteps(self, num: int) -> int:
        '''naive iteration 
        count=0
        while num>0:
            if num%2==0:
                num/=2
            else:
                num-=1
            count+=1
        return count
        '''
        #bit counting
        steps = num == 0
        while num > 0:
            steps += 1 + (num & 1)
            num >>= 1
        return steps - 1