def isSubsequence(s: str, t: str) -> bool:
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n