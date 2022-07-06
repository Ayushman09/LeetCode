def fib(self, n: int) -> int:
        if n == 0: return 0
        f0 = 0
        f1 = 1
        for i in range(n-1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return f1