class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        sufix = []

        for i in range(len(height)):
            if i == 0:
                prefix.append(0)
            else:
                prefix.append(max(height[:i]))

            if i == len(height) - 1:
                sufix.append(0)
            else:
                sufix.append(max(height[i+1:]))
            
            #print(f'prefix: {prefix}')
            #print(f'sufix: {sufix}')
            #print('--------')

        qtd = 0
        for i in range(len(prefix)):
            qtd += max((min(prefix[i], sufix[i]) - height[i]), 0)
        return qtd