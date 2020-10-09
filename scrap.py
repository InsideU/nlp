import nltk
from nltk.tokenize import word_tokenize
from urllib import request

url = "http://www.gutenberg.org/files/2554/2554-0.txt"

response = request.urlopen(url)

raw = response.read().decode('utf8')

print(type(raw))

token = word_tokenize(raw)

print(type(token))

#Handling the tweet data
f= open('tweets1.txt','r')
text = f.read()
text1 = text.split()
text2 = nltk.Text(text1)

print(type(text1))
print(type(text2))
print(text2.concordance("good") #searching the specific word
