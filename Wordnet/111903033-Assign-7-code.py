# basic code for the printing the info with the help of the nltk and wordnet
import nltk 
from nltk.corpus import wordnet;
from nltk.corpus import brown
from nltk import word_tokenize

# function to gice lowest common hypernym 
# lcs is basic function with wordnet
# calculation of information content of the two words 
# with nltk brown corpus 
# brownIc=wordnet.ic(brown,False,0.0)

brownIc=""
def lcs(a,b):
    aa=wordnet.synsets(a)[0]
    bb=wordnet.synsets(b)[0]
    # print(b,c)
    return aa.lowest_common_hypernyms(bb)

# print(lcs("bench","wall"))

# function to return the resnikSimilarity value 
# formula :IC(c)=−log p(lcs(c,c2))

def resnikSimilarity(a):

    aa=wordnet.synsets(a)[0]
    return aa.res_similarity(aa,brownIc)

# print(resnikSimilarity("cat"))

# there are different ways are there to find the lin similarity 
# as we know that inorder to find the similarity between the words with the help
# of lin similarity then we are going to use ic that is Information Content 
# i will use both here 

# formula for lin_similarity is 
    # lin_similarity = 2*IC(c1,c2)/(IC(c1)+IC(c2))
    
def lin_similarity(a,b):
    # taking top most meaning as the synset and do further proceding on it 
    aa=wordnet.synsets(a)[0]
    bb=wordnet.synsets(b)[0]

    # the value which we get with resmik_similarity with itself is ic itself
    # lets calculate and then return the value for the lin_similarity
    linsim=2*(aa.res_similarity(bb,brownIc))/(resnikSimilarity(a)+resnikSimilarity(b))
    
    return linsim#,aa.lin_similarity(bb,brownIc)
    # print(aa,bb)

# this is function which is calling the lin similarity
# print(lin_similarity("plant","tree"))

# Jiang-Conrath distance 
def jcDistance(a,b):
    # jcDistance(c1,c2)=IC(c1)+IC(c2)-2*IC(lcs(c1,c2))
    aa=wordnet.synsets(a)[0]
    bb=wordnet.synsets(b)[0]
    # d=resnikSimilarity(a)+resnikSimilarity(b)-2*(z.res_similarity(z,brownIc))
    return 1/aa.jcn_similarity(bb,brownIc)

# print(jcDistance("cat","dog"))

# Leacock-Chodorow similarity
def leacockChodorowSimilarity(a,b):
    aa=wordnet.synsets(a)[0]
    bb=wordnet.synsets(b)[0]
    return aa.lch_similarity(bb,brownIc)


# print(leacockChodorowSimilarity("car","brush"))


def leskAlgo(s):
    # create tokens with the help of the string 
    # so now we created tokens successfulley 
    a= word_tokenize(s)

    return a

print(leskAlgo("dog and cat"))

