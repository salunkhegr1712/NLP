# here with the help of this function we have to print the rules inside our cfg grammer 
def stringMaker(l):
    s=""
    for i in l[1:]:
        s=s+" " +str(i)
    return f"{ l[0]} --> "+s

def printRules(l):
    for i in l:
        print(stringMaker(i))

# lets declare some grammer rules such that we can be able to draw sentenses from themselves 

# firstly there are two types of states and these are terminals and non terminals
# non terminals 
nonTerminals=["S","NN","VBP","VP","AUX",""]

# here we are going to use the the list and the tupple in order to store the results and
# in further step we also going to print it 
# here i will store all nonTerminals to nonTerminals rules 
ntRules=[("S","NP","VP"),("S","X1",'VP'),('X1','AUX','NP'),('S','VERB','NP'),('S','X2','PP'),
('S','VERB','PP'),('S','VP','PP'),('NP','DET','NOMIAL'),('NOMIAL','NOMIAL','NOUN'),('NOMIAL','NOMIAL','PP'),
('VP','VERB','NP'),('VP','X2','PP'),('X2','VERB','NP'),('VP','VERB','PP'),('VP','VP','PP'),('PP',"PREPOSITION","NP")]


# printRules(ntRules)

tRules=[('NP','i'),('NP',"she"),('NP',"me"),('NP',"twa"),("NP",'houston'),('NOMIAL',"book"),('NOMIAL',"flight")
,('NOMIAL',"meal"),('NOMIAL',"money"),('VP',"include"),('VP',"prefer"),("VP","book"),
("Det",'that'),('DET','this'),("DET",'the'),("DET",'a'),("AUX",'does'),('PREPOSITION','from'),('PREPOSITION','near')
,('PREPOSITION','to'),('PREPOSITION','through'),('PREPOSITION','on')]
# printRules(tRules)

# a matrix creator function which will help us to give matrix according to size of the sentense 
def createMatrix(m):
    k=0
    l=[]
    for i in range(m):
        l.append(["PHI"]*(m-k))
        k=k+1
    return l

# function to print the matrix which help us to visialize how the matrix is filling
def printMatrix(m):
    s=len(m[0])
    k=0
    for i in m:
        print(str(i))
        k=k+1

# this will give rules which are related to terminals 
def getTerminalRule(word):
    k=[]
    for i in tRules:
        if(i[1]==word):
            k.append(i[0])
    return k

# this will give rules related to non terminals 
def getNonTerminalRule(a,b):
    k=[]
    if a==[] or b==[]:
        return []
    for i in ntRules:
        if i[1] in a and i[2] in b:
            k.append(i[0])
    return k

# this will help us to get the rules related to the non terminals 
def getNonTerminalRule(a,b):
    k=[]
    if a==[] or b==[]:
        return []
    for i in ntRules:
        if i[1] in a and i[2] in b:
            k.append(i[0])
    return k

# this will give rules for inner elements of the matrix 
def getNumberedPairs(a,k):
    i=int(a[0])
    j=int(a[1])
    # print(i,j)
    kk=[]
    # printMatrix(k)
    for m in range(j):
        gg=getNonTerminalRule(k[i][m],k[m+1][j-m-1])
        kk=kk+[gg]
    return kk

# this will find that are we getting s tag or not 
def find(a):
    for i in a:
        for j in range(len(i)):
            if i[j]=="S":
                return True
    return False


s="she book flight meal through book money include"
# s="she on through" 
s=s.lower()
def cky(s):
    gg=s.split(" ")
    # print(gg)
    k=createMatrix(len(gg))
    # printMatrix(k)
    m=0
    # print('')
    # assigning initial rules and iteration for the corner element where we have to deal with terminals
    for i in k:
        i[0]=getTerminalRule(gg[m])
        m+=1
    # printMatrix(k)
    
    kk=len(gg)
    jj=0
    f=False
    if(find(k)):
        return True

    # this will help us to iterate digonally and then we will reach our answer 
    while (kk!=-1):
        # print()
        ss=0
        for i in k[:kk]:
            
            if i[jj]=="PHI":
                i[jj]=getNumberedPairs(f"{ss}{jj}",k)
                if(find(i[jj])):
                    f=True
            ss+=1
        # print("")
        kk=kk-1
        jj+=1
    # print(k.index("S"))
    # printMatrix(k)
    if f:
        return True
    return False

# printing final verdict that is our statement is following our CFG grammer or not  
if cky(s):
    print(f"the sentense '{s}' will follow our grammer")
else:
    print(f"the sentense '{s}' will not follow our grammer")