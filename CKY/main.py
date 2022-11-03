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
nonTerminals=["S","NN","VBP","VP"]

# here we are going to use the the list and the tupple in order to store the results and
# in further step we also going to print it 
l=[("S","NP","VP"),("NP","PP","AP"),("NN","VBP")]

printRules(l)

# so lets declare some grammer and for that we will go for the cky algo implementation


