import nltk 
from nltk.corpus import stopwords


texts = 'I’m never sure if I dislike pseudo-science more than crypto-religious movements.  In practice they both tend to end up as cults in order to maintain a false belief system. The exemplar of the former, although it is now on the wane, is Neuro-linguistic programming (NLP) with its various promises of personal mastery and manipulation. Check out the Wikipedia entry (in which I am an active editor) if you want to see the evidence for its lack of scientific authenticity. I’ve never understood why the University of Surrey allows a group of NLP consultants a home'

sentences = nltk.sent_tokenize(texts)

stop_words = set(stopwords.words("english"))
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    #print(words)
    #print()
    wsw=[word for word in words if not word in stop_words] 

    print(wsw)

