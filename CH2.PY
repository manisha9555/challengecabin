f=open("Challenge-2-Input.txt","r")         
Exp=f.readlines()                          
length=len(Exp)                             
for i in range (0,length):                 
    k=Exp[i]                                
    l=len(k)                                
    x=""                                   


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
    r=str(int(eval(x)))                           
    n=open("results.txt","a")                       
    c=""                                          
    for temp in Exp[i]:                             
        if (temp!="\n"):
            c=c+temp
    c=c+" "+r+"\n"                                
    n.write(c)                                      
