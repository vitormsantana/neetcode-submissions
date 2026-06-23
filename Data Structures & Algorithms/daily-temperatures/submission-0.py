class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [None] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) > 0 and i > 0:
                if stack[-1][0] < temperatures[i]:
                    while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                        output[stack[-1][1]] = i - stack[-1][1]
                        stack.pop()
                    stack.append([temperatures[i], i])
                else:
                    stack.append([temperatures[i], i])
            else:
                stack.append([temperatures[i], i])
            
            print(f'stack: {stack}')
            print(f'output: {output}')
            print('-----')

        for i in range(len(output)):
            if output[i] is None:
                output[i] = 0
        
        return output
                    

temperatures=[30,38,30,36,35,40,28]
