def minRemoveToMakeValid(self, s: str) -> str:
        '''#Space: O(1)
        cnt_open, cnt_close, res = 0, 0, ''
        for ch in s:
            if ch == '(': cnt_open += 1
            if ch == ')': cnt_close += 1
            if cnt_open < cnt_close:
                cnt_close -= 1
            else:
                res = res + ch

        s = res
        
        cnt_open, cnt_close, res = 0, 0, ''
        for ch in reversed(s):
            if ch == '(': cnt_open += 1
            if ch == ')': cnt_close += 1
            if cnt_close < cnt_open:
                cnt_open -= 1
            else:
                res = ch + res
                
        return res
        '''
        s=list(s)
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if len(stack)>0:
                    stack.pop()
                else:
                    s[i] = ''
        while len(stack)>0:
            s[stack[-1]]=''
            stack.pop()
        return ''.join(s)