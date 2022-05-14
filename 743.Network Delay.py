def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsedTime, graph, queue = [1] + [float("inf")] * n, defaultdict(list), deque([(0, k)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1