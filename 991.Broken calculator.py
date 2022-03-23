import math
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        opsCnt = 0
        
        while (target > startValue):
            print(startValue, target, opsCnt)
            opsCnt += (1 + target % 2)
            target = math.ceil(target/ 2)
            
        return opsCnt + abs(startValue - target)