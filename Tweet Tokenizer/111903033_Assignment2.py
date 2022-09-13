# installing / checking that is nltk is there in the system if not this will install it 
# pip install nltk
# after downloading the nltk we will import it in our system 
import nltk as nltk
from nltk.tokenize import TweetTokenizer
from curses.ascii import isalnum
from nltk import word_tokenize

def parsing(token):
    l=[]
    f=token.index("'")
    if token=="'":
        return ["'"]
    if(token[f+1]=="s" or token[f+1]=="S"):
        l.append(token[:f])
        l.append("is")
    elif(token[f+1]=="t" or token[f+1]=="T"):
        if(token[:f]=="can" or token[:f]=="Can" ):
            l.append("can")
            l.append("not")
        elif(token[:f]=="won" or token[:f]=="Wont" ):
            l.append("would")
            l.append("not")
        else:
            l.append(token[:f-1])
            l.append("not")
    elif(token[f+1]=="v" or token[f+1]=="V"):
        l.append(token[:f-1])
        l.append("have")
    elif(token[f+1]=="m" or token[f+1]=="M"):
        l.append(token[:f])
        l.append("am")
    elif(token[f+1]=="l" or token[f+1]=="L"):
        l.append(token[:f])
        l.append("will")
    elif(token[f+1]=="d" or token[f+1]=="D"):
        l.append(token[:f])
        l.append("had")
    else:
        l.append(token)

    return l

def split_dash(sm):
    a=sm.index("-")
    return [sm[:a],sm[a+1:]]  

# Python3 program Split camel case
# string to individual strings
def camel_case_split(str1):
    l=[]
    n=0
    if(len(str1)<2):
        return [str1]
    if (str1.isalpha()):
        s=str1[0]
        n=n+1
    else:
        l.append(str1[0])
        s=str1[1]
        n=2

    for i in range(n,len(str1)):
        if(str1[i].isupper()):
            l.append(s)
            s=""
        s=s+str1[i]
    l.append(s)
    return l

# camel_case_split("GhanshamRajaramSalunkhe")  

# now we will check for words having camel case or not 
def checkForCamelCase(s):
    return s != s.lower() and s != s.upper() and "_" not in s


# function to count capital letters inside the character
def countUpperCharacters(s,n):
    count=0
    for i in range(n,len(s)):
        if(s[i].isupper()):
            count=count+1
    return count

# code where we bring all things together and then we will return
def breakCamelCase(token):
    # if(token[0]=="@" or token[0]=="#") and checkForCamelCase(token) and countUpperCharacters(token,2) >0 and "/" not in token and "-" not in token :
    #     return camel_case_split(token)

    if checkForCamelCase(token) and countUpperCharacters(token,1) >0 and "/" not in token and "-" not in token:
        return camel_case_split(token)
    # print(fd)
# breakCamelCase("#GhanshamRajaramSalunkhe")

# def breakAndpercent(token):
#     if token=="@":
#         return ['@']
    
#     return [token[0],token[1:]]

def calculateCharacter(token):
    l=0
    for i in token:
        if isalnum(i):
            l+=1
    
    return len(token)-l

def punctuations(token):
    ll=[]
    for i in token:
        ll.append(i)
    return ll
    

# # getting data from the file to as a string and we will process it further 
# file1 = open("InputDataset.txt","r+") 
  
# print("Output of Read function is ")
# c=file1.read()
# # print(c)
# # printing the len of file and the type of after reading through the file 
# # print(len(c))
# # print(type(c))

# # it is showing error so we download the punkt to avoid this error 
# nltk.download('punkt')

# # so for your info tokenizer are present inside nltk.tokenize from nltk.tokenize you can get word_tokenize and other tokenizers 
# # on basis of spaces and on basis of spaces tokens are getting created
# # so as i need the words and the punchuations im using word tokenization

# tokens=word_tokenize(c) # tokenize with word tokenize 

# # print(len(tokens))
# # print(tokens)

# # now importing the tweetTokenizer and then we will process it further 

# tweetTokens=TweetTokenizer(tokens) # this will give a tokenizer object as the result 
# # now convert the tokens into the list or array 
# tweetTokens=tweetTokens.tokenize(c)

# print(tweetTokens)


# code which gives us the input in the form of oneline at a time 
with open('InputDataset.txt') as f:
    lines = f.readlines()

# print(lines[1])

# now importing the tweetTokenizer and then we will process it further 
from nltk.tokenize import TweetTokenizer
ttk=TweetTokenizer() # this will give a tokenizer object as the result 
# now convert the tokens into the list or array 
# ttk1=ttk.tokenize(lines[0])
# print(ttk)

# print(len(ttk1))
# print(ttk1)
ll=[]

def giveTokens(ttk1):
    for i in ttk1:
        if checkForCamelCase(i):
            for j in camel_case_split(i):
                ll.append(j)

        # elif i[0]=="@" or i[0]=="#":
        #     for j in camel_case_split(i):
        #         # print(j)
        #         ll.append(j)
        
        elif "-" in i and len(i)>3:
            for j in split_dash(i):
                # print(i)
                # print(j)
                ll.append(i)
                ll.append(j)
            
        elif ("'" in i and i !="'"):
            l=parsing(i)
            for j in l:
                ll.append(j)
                
        elif i.count('.')>2 or i.count(',')>2 or i.count('?')>2 or i.count('!')>2:
            for j in punctuations(i):
                ll.append(j)

        else:
            ll.append(i)

    ll.append(".")
    return ll

print(lines[1])
ttk1=ttk.tokenize(lines[99])
ll=giveTokens(ttk1)
print(ll)


# with open("output.txt","a")as f:
#     for j in lines:
#         ttk1=ttk.tokenize(j)
#         ll=giveTokens(ttk1)
#         for i in ll:
#             f.write(i+"\n")

print(camel_case_split("ImGhanshamSalunkhe"))