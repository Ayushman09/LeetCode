def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        sol = []
        
        for c in range(len(matrix[0])):
            tmp = []
            for r in range(len(matrix)):
                tmp.append(matrix[r][c])
            
            sol.append(tmp)
        
        return sol 
    
    #one liner using Zip
        #return list(zip(*matrix))