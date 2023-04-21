f=open("Challenge-3-input.txt","r", encoding="utf8")
data=f.readlines()
s=input("Enter  a string ")
for i in range (0,len(data)):
    if (s in data[i]):
        print(data[i])

