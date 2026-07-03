import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:
            print(f'neg_stones antes das acoes: {neg_stones}')
            if neg_stones[0] == neg_stones[1]:
                heapq.heappop(neg_stones)
                heapq.heappop(neg_stones)
            else:
                bigger = heapq.heappop(neg_stones) 
                little = heapq.heappop(neg_stones)
                remains = - bigger + little 
                heapq.heappush(neg_stones, -remains)

        if len(neg_stones) == 1:
            return -neg_stones[0]
        return 0