##Análise morfológica
import spacy
from spacy import load
spacy.load("pt_core_news_sm")
nlp = load("pt_core_news_sm")
doc = nlp('Kaike foi dormir tarde. Ele estava estudando.')
for t in doc:
    print("{:10} | {:10} | {}".format(
        t.text,
        t.pos_,
        t.morph
    ))