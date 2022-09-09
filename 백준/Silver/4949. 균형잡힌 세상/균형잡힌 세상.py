string=""
while True:
    new=input()
    if new=='.':
        break
    else:
        string+=new
string=string.split(".")
string=string[:-1]
dic={"[":1,"]":1,"(":2,")":2}
for row in string:
    stack=[]
    error=0
    for char in row:
        try:
            if char=="[" or char=="(":
                stack.append(dic[char])
                
            elif char=="]" or char==")":
                
                popping=stack.pop(-1)
                
                if dic[char]!=popping:
                    error=1
                    break
                    
        except IndexError:
            error=1
            break
    if error:
        print("no")

    elif not stack:
        print("yes")
    
    else:
        print("no")

    error=0

