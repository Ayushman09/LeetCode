class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''if (dividend, divisor) == (-2**31, -1): # only case of overflow
            return 2**31 - 1
        neg = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while dividend >= divisor:
            q, acc = 1, divisor
            while dividend >= (acc<<1):
                q <<= 1
                acc <<= 1
            res += q
            dividend -= acc
                
        return [1,-1][neg]*res'''
        
        #without bitwise operators
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:
                the_sum <<= 1
                current_quotient <<= 1            
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))