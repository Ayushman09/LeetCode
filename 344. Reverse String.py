def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse() #don’t use this in interviews
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]
        #two-pointer soln -> one liner