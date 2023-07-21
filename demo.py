import spacy
from spacy.lang.en import English
nlp = English()
doc = nlp("Give it back! He pleaded.")
print(doc)
