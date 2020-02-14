import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatize = WordNetLemmatizer()
word_data = " IT originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
#print(nltk_tokens)
sentence_data = "Sun rises in the east , sun sets in the west"
nltk_tokens = nltk.sent_tokenize(sentence_data)
print(nltk_tokens)
porter_stemmer = PorterStemmer()
nltk_tokens = nltk.word_tokenize(word_data)
# next find the roots of the word
for w in nltk_tokens :
    print('Actual : %s Stem: %s ' % (w,porter_stemmer.stem(w)))
for w in nltk_tokens:
    print('actual : %s Lemma: %s' %(w,wordnet_lemmatize.lemmatize(w)))
