q = int(input())
stack = []
S = ''
for i in range(q):
    oper = list(input().split())
    #append string "1"
    if oper[0] == '1':
        stack.append(S)
        S = S + oper[1]
    
    #delete characters
    elif oper[0] == '2':
        stack.append(S)
        S = S[:-int(oper[1])]
        
    #print
    elif oper[0] == '3':
        print(S[int(oper[1]) - 1])
        
    #Undo
    else:
        S = stack.pop()
        