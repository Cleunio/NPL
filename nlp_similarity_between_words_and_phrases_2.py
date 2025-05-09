# -*- coding: utf-8 -*-
"""NLP-Similarity Between Words and Phrases_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CHFTeFv7rAoJHNP7bPjhAW1j6cAC7ZrD
"""

!pip install spacy--upgrade
#pip install spacy==version
!python -m spacy download pt
!python install nltk --upgrade

import spacy
from nltk.stem import PorterStemmer
from spacy import displacy
from spacy.lang.pt.examples import sentences
from spacy.lang.en.stop_words import STOP_WORDS
spacy.__version__, nltk.__version__

nlp = spacy.load('pt')
document = nlp('I\'m learning English... in Brazil')

for token in document:
  print(token.text, token.pos_)

for token in document:
  print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape, token.is_alpha, token.is_stop)

for token in document:
   if token.pos == 'PROPN':
    print(token.text)

for token in document:
   if token.pos == 'PROPN':
    print(token.text, token.lemma_)

doc = nlp('am  is are be was were')
[token.lemma_ for token in doc]

stemmer = PorterStemmer()
stemmer.stem('am')

for token in document:
   if token.pos == 'PROPN':
    print(token.text, token.lemma_, stemmer.stem(token.text))

text = "IBM... Recife..."

doc = nlp(text)

for entity in doc:
   print(entity.text, entity.label_)

displacy.render(doc, style = 'ent', jupyter = True)

text2 = "Luiz Gonzaga... Exu... Baião"

doc = nlp(text2)

for entity in doc:
   print(entity.text, entity.label_)

displacy.render(doc, style = 'ent', jupyter = True)

for entity in doc.ents:
   if entity.label == 'PER'
    print(entity.text)

print(STOP_WORDS)

len(STOP_WORDS)

nlp.vocab['go'].is_stop

nlp.vocab['walk'].is_stop

doc = nlp('I\'m walking')

for token in doc:
  if not nlp.vocab[token.text].is_stop:
    print(token.text)

doc = nlp("Book a ticket from Recife to Miami")
origin = doc[5]
dest = doc[7]
origin, dest

list(origin.ancestors)

list(dest.ancestors)

doc[0].is_ancestor(doc[2])

#example 2
doc = nlp('Book a table at the restaurant and a taxi to the hotel')
tasks = doc[2], doc[8]
places = doc[5], doc[11]

for place in places:
  for obj in place.ancestors:
    print(obj)

for place in places:
  for obj in place.ancestors:
    if obj in tasks:
      print('Book {} is to the {}'.format(obj,place))

list(doc[5].children)

#example 3
doc = nlp('Book a table at the restaurant and a taxi to the hotel')
displacy.render(doc, style='dep', jupyter=True, options={'distance':90})
#display.serve(doc, style='dep')

list(doc[2].ancestors)

list(doc[2].children)

#example 4
doc = nlp('Which places can we visit in Recife and stay in Olinda?')
places = doc[6], doc[10]
action = doc[4], doc[8]
places, action

for local in places:
  for act in local.ancestors:
    if act in action:
      print("{} to {}".format(local,act))
      break

displacy.render(doc, style='dep', jupiter=True, options={'distance': 90})

p1 = nlp("Hello")
p2 = nlp("Hi")
p3 = nlp("High")

p1.similarity(p2)
p2.similarity(p3)
p1.similarity(p3)

texto1 = nlp("When will the new movie be released?")
texto2 = nlp("The new movie will be released next month")
texto3 = nlp("Which color is the car?")

texto1.similarity(texto2)
texto1.similarity(texto3)
texto2.similarity(texto3)

#Example 2

text4 = npl("cat dog horse person")

for text_ in text4;
  for text_2 in text4
    similarity = int(text_.similarity(text_2)*100)
    print("{} is {} similar to {}".format(text_,similiarity, text_2))