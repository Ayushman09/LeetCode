def maximumWealth(self, accounts):
        ans=0
        for i in accounts:
            ans=max(ans,sum(i))
        return ans