N = 4
a = [["Mildred","born","in","previous","Dragon","year","from","Bessie"],
      ["Gretta","born","in","previous","Monkey","year","from","Mildred"],["Elsie","born","in","next","Ox","year","from","Gretta"],
      ["Paulina","born","in","next","Dog","year","from","Bessie"]]


yearCycle = ["Ox","Tiger","Rabit","Dragon","Snake","Horse","Goat","Monkey","Roost","Dog","Pig","Rat"]
years = [0,3,7,0,9]
Bessie = 0

for i in range(N):
    if a[i][3] == "previous":
        if  years[i] <= years[i+1]:
            chaE = years[i] - years[i+1] + 12
        elif years[i] > years[i+1]:
            chaE = years[i] - years[i+1]
    elif a[i][3] == "next":
        if  years[i] >= years[i+1]:
            chaE = years[i] - years[i+1] - 12
        elif years[i] < years[i+1]:
            chaE = years[i] - years[i+1]
       
    globals()[a[i][0]] = globals()[a[i][7]] - chaE

#print(Mildred)
#print(Gretta)
#print(Elsie)
#print(Paulina)
