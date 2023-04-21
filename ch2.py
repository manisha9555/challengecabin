
f=open("Challenge-2-Input.txt","r")         #opening file 
Exp=f.readlines()                           #storing lines in file as string in lists
length=len(Exp)                             #finding length of the list of lines 
for i in range (0,length):                  #traversing all the strings one by one 
    k=Exp[i]                                #storing expressions one by one in another string variable  
    l=len(k)                                #finding length of the expression
    x=""                                    #initilazing empty string

#traversing the expression and converting it to make suitable for eval function using different conditions   
    for j in range(0,l):                    
        if (k[j]=="{" or k[j]=="["):
            if(k[j-1]=="*" or k[j-1]=="/" or k[j-1]=="+" or k[j-1]=="-" or k[j-1]=="^" ):
                x=x+"("
            else:
                x=x+"*"+"("
        elif(k[j]=="}"or k[j]=="]"):
            x=x+")"
        elif(k[j]==" "or k[j]=="="):
            x=x
        elif(k[j]==")"and k[j+1]==" " and k[j+2]=="("):
            x=x+k[j]+"*"
        
        elif(k[j]=="^"):
            x=x+"*"+"*"
        else: 
            x=x+k[j]
    r=str(int(eval(x)))                             #Evaluating the expression using "eval" function
    n=open("results.txt","a")                       #Creating file to store results 
    c=""                                            #taking an empty string 
    for temp in Exp[i]:                             #copying expression to empty string (removing line break) 
        if (temp!="\n"):
            c=c+temp
    c=c+" "+r+"\n"                                  # concatinating the result to the string
    n.write(c)                                      # writing to the file 
