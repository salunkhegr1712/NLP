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

# here we are going to use the the list and the tupple in order to store the results and
# in further step we also going to print it 
# here i will store all nonTerminals to nonTerminals rules 
ntRules=[("S","NP","VP"),("S","X1",'VP'),('X1','AUX','NP'),('S','VERB','NP'),('S','X2','PP'),
('S','VERB','PP'),('S','VP','PP'),('NP','DET','NOMIAL'),('NOMIAL','NOMIAL','NOUN'),('NOMIAL','NOMIAL','PP'),
('VP','VERB','NP'),('VP','X2','PP'),('X2','VERB','NP'),('VP','VERB','PP'),('VP','VP','PP')]

tRules=[('NP','i'),('NP',"she"),('NP',"me"),('NP',"twa"),("NP",'houston'),('NOMIAL',"book"),('NOMIAL',"flight")
,('NOMIAL',"book"),('NOMIAL',"meal"),('NOMIAL',"money"),('VP',"include"),('VP',"prefer"),("VP","book"),
("DET","the"),("DET","a"),("DET","an")]
printRules(tRules)

# so lets declare some grammer and for that we will go for the cky algo implementation


def ckyAlgorithm(s):
    s

# NP → I | she | me
# NP → TWA | Houston
# Nominal → book | flight | meal | money
# VP → book | include | prefer
