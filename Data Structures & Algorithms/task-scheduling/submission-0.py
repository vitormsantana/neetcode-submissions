import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        frequencies = {}
        for i in range(len(tasks)):
            frequencies[tasks[i]] = frequencies.get(tasks[i], 0) + 1
        
        print(f'frequencies: {frequencies}')

        time = 0
        queue = []
        max_heap = []
        for key, value in frequencies.items():
            heapq.heappush(max_heap, -value)
        
        while len(max_heap) > 0 or len(queue) > 0:
            if len(queue) > 0:
                for j in range(len(queue) - 1, -1, -1):
                    if queue[j][1] == time:
                        heapq.heappush(max_heap, queue[j][0])
                        queue.pop(j)

            if len(max_heap) > 0:
                bigger = heapq.heappop(max_heap) + 1
                if bigger < 0:
                    queue.append([bigger, time + n + 1])
            time += 1
        return time