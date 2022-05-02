def sortArrayByParity(self, A: List[int]) -> List[int]:
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            if A[beg] % 2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A