def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur = 0
        for c in s:
            if c=='(':
                stack.append(cur)
                cur=0
            else:
                cur = stack.pop() + max(1, 2*cur)
        return cur