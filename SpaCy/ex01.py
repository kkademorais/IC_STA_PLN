#Display das relações de dependência
from spacy import load, displacy

nlp = load('pt_core_news_sm')
doc = nlp('Kaike está estudando PLN. Ele está focado.')

#displacy.serve(doc)