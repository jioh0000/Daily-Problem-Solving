N = input()
count = 0
for i in N:
    if i == '*':
        count += 1

if count == 0:
    print(N)
    
elif count == 1:
    print(N.replace("*", "0"))
    print(N.replace("*", "1"))

elif count == 2:
    #1*0*0 -> 100*0, 110*0
    idx = N.find("*")
    temp1 = N[:idx]+"1"+N[idx+1:]
    print(temp1.replace("*", "0"))
    print(temp1.replace("*", "1"))

    temp2 = N[:idx]+"0"+N[idx+1:]
    print(temp2.replace("*", "0"))
    print(temp2.replace("*", "1"))

    