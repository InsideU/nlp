import nltk

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "NP:{<DV>?<JJ>*<NN>}"


cp = nltk.RegexpParser(grammar)

result = cp.parse(sentence)

print(result)

print(result.draw())
