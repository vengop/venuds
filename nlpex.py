import nltk
from nltk.book import *
import matplotlib.pyplot as plt
print(text1)
print(text1.concordance('monstrous'))
print(text1.similar("monstrous"))
print(text2.similar('monstrous'))
print(text2.common_contexts(["monstrous", "very"]))
print(text4.dispersion_plot(['citizens','democracy','freedom','duties','America']))
#text3.generate(self)
print(len(text4))
#print(sorted(set(text6)))
def lexical_diversity(text) :
    return len(set(text)) / len(text)
def percentage(count,total):
    return 100 * count/total
lexical_diversity(text4)
percentage(4,5)
print(sent1)
print(['Monty', 'Python'] + ['and', 'the', 'Holy', 'Grail'])
sent1.append("Some")
print(sent1)
''.join(['monty','python'])
print('monty python'.split())
saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(tokens)
print(tokens[-2:])
fdist1 = FreqDist(text1)
print(fdist1)
print(fdist1.most_common(50))
fdist2 = FreqDist(text2)
print(fdist2)
print(fdist2.most_common(50))
fdist1.plot(50, cumulative=True)
plt.show()
#print(fdist1.hapaxes())
v = set(text1)
long_words = [w for w in v if len(w) > 15]
#print(sorted(long_words))
list(bigrams(['more','is','said','than','done']))
#print(text4.collocations())
print([w.upper() for w in text1])
print(sorted([w.upper() for w in text1]))
sent1 = ['call','me','Ishmael']
for xyzzy in sent1 :
    if xyzzy.endswith('l'):
        print(xyzzy)
tricky = sorted(w for w in set(text2) if 'cie' in w or 'cei' in w)
for word in tricky:
     print(word, end=' ')
sett = set(sent3) < set(text1)
print(sett)

