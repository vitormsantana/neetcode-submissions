class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        qtd_nums = 0

        for i in range(len(tokens)):
            #print(f'i: {i}')
            if tokens[i].isdigit() or (tokens[i].startswith('-') and tokens[i][1:].isdigit()):
                #print(f'tokens[i]: {tokens[i]}')
                my_stack.append(tokens[i])
            else:
                if tokens[i] == "/":
                    to_append = int(my_stack[-2]) / int(my_stack[-1])
                if tokens[i] == "*":
                    to_append = int(my_stack[-2]) * int(my_stack[-1])
                if tokens[i] == "+":
                    to_append = int(my_stack[-2]) + int(my_stack[-1])
                if tokens[i] == "-":
                    to_append = int(my_stack[-2]) - int(my_stack[-1])
                
                my_stack.pop()
                my_stack.pop()
                my_stack.append(to_append)
            
            #print(f'tokens: {tokens}')
            #print(f'my_stack: {my_stack}')
            #print(f'---------')
        
        return int(my_stack[0])