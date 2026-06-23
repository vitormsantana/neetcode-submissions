class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = []
        positionSpeed = []
        for i in range(len(position)):
            positionSpeed.append([position[i], speed[i]])

        positionSpeed.sort(key=lambda x: x[0], reverse=True)

        for i in range(len(position)):
            times.append((target-positionSpeed[i][0])/positionSpeed[i][1])
        
        for j in range(len(times)):
            if len(stack) == 0 or times[j] > stack[-1]:
                stack.append(times[j])
        
        return len(stack)