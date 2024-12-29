code=input("please enter the brainf*ck code\n")
values=[0]
pointer=0
stack=[]
counter=0
for x in code:
    if x==",":
        user=input("character:")
        values[pointer]=ord(user)
    
    elif x=="+":
        values[pointer]=values[pointer]+1
        if values[pointer]==256:
            values[pointer]=0
        
    elif x=="-":
        values[pointer]=values[pointer]-1
        if values[pointer]==-1:
            values[pointer]=255
    
    elif x=="<":
        pointer=pointer-1
    elif x==">":
        pointer=pointer+1
        if pointer==len(values):
            values.append(0)
    
    elif x==".":
        print(chr(values[pointer]),end="")

    elif x=="[":
        stack.append(counter)

    elif x=="]":
        start=stack.pop()
        end=counter
        while values[pointer]!=0:
           new=code[start+1:counter]
           for x in new:
            if x==",":
                user=input("character:")
                values[pointer]=ord(user)
    
            elif x=="+":
                values[pointer]=values[pointer]+1
            if values[pointer]==256:
                values[pointer]=0
        
            elif x=="-":
                values[pointer]=values[pointer]-1
            if values[pointer]==-1:
                values[pointer]=255
    
            elif x=="<":
                pointer=pointer-1
            elif x==">":
                pointer=pointer+1
            if pointer==len(values):
                values.append(0)
    
            elif x==".":
                print(chr(values[pointer]),end="")
           

    counter=counter+1


