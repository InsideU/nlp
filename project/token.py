import nltk
from nltk.tokenize import TweetTokenizer


text = 'Tom Scully (born 15 May 1991) is a professional Australian rules footballer playing for the Hawthorn Football Club. He previously played for the Melbourne Football Club and Greater Western Sydney Giants. A star midfielder at junior level, Scully was originally selected by Melbourne with the first overall draft pick of the 2009 AFL draft. However at the conclusion of his initial two-year contract with Melbourne, he accepted the opportunity to join the newly established GWS Giants in 2012 on a six-year deal.[1] In October 2018, Scully was traded to Hawthorn for the 2019 season.He attended school first at Berwick College and then Haileybury College'


print(nltk.sent_tokenize(text))
