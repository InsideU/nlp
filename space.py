import spacy 

spacy.prefer_gpu()

m = spacy.load("en_core_web_sm")

nlp = "it is considered as one of the big four technology companies,alongside"

doc= m(nlp)

for ent in doc.ents:
    print(ent.text,ent.label_)

doc1 = m("Apple is looking at buying U.K. startup for $1 billion")
for token in doc1:
    print(token.text, token.pos_, token.dep_)

locs = [('Omnicom','IN','New York'),('DDB Needham','IN','New York'),('kaplan Thaler Group','IN','New York')]

query =[e1 for(e1,re1,e2) in locs if e2 == 'New York']

print(query)
