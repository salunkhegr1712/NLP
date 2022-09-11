# nltk stands for the natural language toolkit 
# it is natural language procesing library 
import nltk

# downloading words corpus from the nltk words 
nltk.download("words")
from nltk.corpus import words
# importing the regex as we are going to need it in finding 
import re

mainWord=""
setOfWords=words.words()
# print(setOfWords)
# len(setOfWords)

# code to get jaccard similarity between two words
def jaccardDistance(l1,l2):
    l1=set(l1)
    l2=set(l2)
    j=l1.intersection(l2)
    jaccard=float(len(j)/(len(l1)+len(l2)-len(j)))
    return jaccard

# def WordWithSomeLength():
 
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
    global mainWord
    mainWord=word
    # matchingWords=list(filter(wordLength,setOfWords))
    matchingWords=list(filter(firstWordChecker,setOfWords))
    word=set(word)
    for i in word:
        bit=re.compile(i)
        matchingWords=list(filter(bit.findall,matchingWords))
    
    ll=[]
    for i in matchingWords:
        ll.append(editDistance(mainWord,i,len(word),len(i))) 
    return matchingWords[ll.index(min(ll))]
# print(matchingWords)

# print(findWords("azmaing"))


def main():
    
    l=['happpy', 'azmaing', 'intelliengt']
    for i in l:
        print(findWords(i))

main()