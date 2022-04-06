def threeSumMulti(self, arr: List[int], target: int) -> int:
        c = Counter(arr)
        ans, M = 0, 10**9 + 7
        for i, j in permutations(c, 2):
            if i < j < target - i - j:
                ans += c[i]*c[j]*c[target - i - j]

        for i in c:
            if 3*i != target:
                ans += c[i]*(c[i]-1)*c[target - 2*i]//2
            else:
                ans += c[i]*(c[i]-1)*(c[i]-2)//6
                
        return ans % M