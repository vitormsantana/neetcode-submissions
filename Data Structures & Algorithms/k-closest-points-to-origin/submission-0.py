import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for coords in points:
            dist = math.sqrt(coords[0] ** 2 + coords[1] ** 2)
            heapq.heappush(distances, [-dist, coords])
        
        while len(distances) > k:
            heapq.heappop(distances)
        
        distances_formated = [x[1] for x in distances]
        return distances_formated
