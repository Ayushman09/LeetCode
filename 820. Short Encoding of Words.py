def minimumLengthEncoding(self, words: List[str]) -> int:
        n, p = 0, ''
        for w in sorted(w[::-1] for w in words):
            if not w.startswith(p):
                n += len(p) + 1
            p = w
        return n + len(p) + 1