class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # [4, 1, 0, 7] - [2, 2, 1, 1]
        # [7, 4, 1, 0] - [1, 2, 1, 2]
        # [(10-7)/1, (10-4)/2, (10-1)/1, (10-0)/2]
        # [3, 3, 9, 5]

        stack = []
        times = []
        positionSpeed = []
        for i in range(len(position)):
            positionSpeed.append([position[i], speed[i]])

        positionSpeed.sort(key=lambda x: x[0], reverse=True)

        

        for i in range(len(position)):
            times.append((target-positionSpeed[i][0])/positionSpeed[i][1])
        
        print(f'times: {times}')

        for j in range(len(times)):
            if len(stack) == 0 or times[j] > stack[-1]:
                stack.append(times[j])
        
        print(f'stack: {stack}')
        
        return len(stack)