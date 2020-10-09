import jieba
seg = jieba.cut("把句子中所有的可以成词的词语都扫描出来 ",cut_all=True)
print(" ".join(seg))
ss = "把句子中所有的可以成词的词语都扫描出来"

print("Using loop")
print()
for i in ss:
    print(i,end= " ")
