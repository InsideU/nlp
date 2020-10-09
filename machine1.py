import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet as  wn 
from nltk.stem import PorterStemmer 
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
#print(wn.synsets('motorcar'))

#print(wn.synset('car.n.01').lemma_names())
#print(stopwords.words('english'))
stemmer = PorterStemmer()
print()
#print(stemmer.stem("happiness"))
stemLan=LancasterStemmer()
#print(stemLan.stem('happiness'))
# Cmu Wordlist 

#entries = nltk.corpus.cmudict.entries()

#SnowballStemmer.languages
#S=SnowballStemmer('french')
#print(S.stem('manges'))
example = 'I am the only one of my kind'
example = [stemmer.stem(token) for token in example.split(" ")]
#print(" ".join(example))
l=WordNetLemmatizer()
print(lemmatizer.lemmatize("knives"))
