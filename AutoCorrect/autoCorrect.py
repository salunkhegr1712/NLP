# nltk stands for the natural language toolkit 
# it is natural language procesing library 
import nltk

# downloading words corpus from the nltk words 
# nltk.download("words")
from nltk.corpus import words
from nltk import word_tokenize
# importing the regex as we are going to need it in finding 
import re

mainWord=""
setOfWords=[]
with open("AutoCorrect/words_alpha.txt") as f:
    setOfWords=f.read().split()

# print(setOfWords)
len(setOfWords)

# code to get jaccard similarity between two words
def jaccardDistance(l1,l2):
    l1=set(l1)
    l2=set(l2)
    j=l1.intersection(l2)
    jaccard=float(len(j)/(len(l1)+len(l2)-len(j)))
    return jaccard

# def WordWithSomeLength():
 
def wordLength(word):
    return len(word)==len(mainWord) or len(word)==len(mainWord)+1 or len(word)==len(mainWord) +2 or len(word)==len(mainWord) -1 
# we just used dynamic programming here 
def editDistance(str1, str2, m, n):

    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    return 1 + min(editDistance(str1, str2, m, n-1),editDistance(str1, str2, m-1, n),editDistance(str1, str2, m-1, n-1))    # Replace)

def firstWordChecker(word):
    return word[0]==mainWord[0] 

# re is function which we can use to find words with some expression 
def findWords(word):
    if word in setOfWords:
        return word

    global mainWord
    mainWord=word
    matchingWords=list(filter(wordLength,setOfWords))
    matchingWords=list(filter(firstWordChecker,matchingWords))
    # print(matchingWords)
    word=set(word)
    for i in word:
        bit=re.compile(i)
        matchingWords=list(filter(bit.findall,matchingWords))
    
    ll=[]

    for i in matchingWords:
        # print(i)
        # print(editDistance(mainWord,i,len(word),len(i)))
        # ll.append(editDistance(mainWord,i,len(word),len(i))) 
        ll.append(jaccardDistance(mainWord,i)) 

    # return matchingWords[ll.index(min(ll))]
    return matchingWords[ll.index(max(ll))]
# print(matchingWords)

# print(findWords("azmaing"))


a=""
with open("AutoCorrect/misspelledText.txt") as f:

    a+=str(f.read())

# print(a)

text=word_tokenize("mainlly mdae uup offf hydreong and hleium gssa sruface isis konwn \
pohtospehre surroundde tinh laeyr knonw tehre wulod leif ")
# print(text)


def main(text):
    
    
    for i in text:
        print(i +" : "+findWords(i))



l=["hydreong","hldo","daiemetr","cna","millionism","surpe","planste","tinh","erath","hlel","cmomon","dfinitee","lightgnin","frie"]
main(l+text)