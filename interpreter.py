code=input("please enter the brainf*ck code\n")
values=[0]
pointer=0

for x in code:
    if x=="+":
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

    elif x==",":
        user=input("character:")
        values[pointer]=ord(user)


print(values)
    