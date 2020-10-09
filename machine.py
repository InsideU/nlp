import nltk 
from nltk.corpus import webtext     
from nltk.corpus import brown 
from nltk.probability import ConditionalFreqDist
from nltk.corpus import inaugural
#brown.categories()
#print(brown.words(categories='adventure')[:50])
#print(inaugural.fileids())
#print(inaugural.words(fileids = '2017-Trump.txt')[:50])

print(webtext.fileids())
text = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[1] Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving '
fd=nltk.FreqDist(text.split())
cfd= ConditionalFreqDist((len(word),word) for word in text.split())
#for i in fd:
#    print(i,fd[i])
for i in cfd[4]:
    print(i,cfd)

