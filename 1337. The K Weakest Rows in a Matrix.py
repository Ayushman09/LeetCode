def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        '''
        #using dictionary
        x=[]

        for i in mat:
            x.append(i.count(1))

        x=(dict(enumerate(x)))


        z= sorted(x, key = x.get)
        z=z[:k]
        return z
        '''
        #optimized minheap soln
        minHeap=[]
        ans=[]
        heapq.heapify(minHeap)
        for row in range(len(mat)):
            soldiers=mat[row].count(1)
            heapq.heappush(minHeap,(soldiers,row))
        while k!=0:
            val,row=heapq.heappop(minHeap)
            ans.append(row)
            k-=1
        return ans