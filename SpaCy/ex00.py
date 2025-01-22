import spacy
from spacy import blank
from spacy import load

##Básico
#nlp = blank('pt')
#doc = nlp('Kaike está estudando')
#span = doc[0:2]
#print(doc[2])
#print(span)

##Carregando modelo pré-treinado
spacy.load("pt_core_news_sm")
nlp = load("pt_core_news_sm")
doc = nlp('Kaike, estudante de computação. Ele está estudando')
doc.sents
for sent in doc.sents: {
    #print(sent)
}

##Tokenization
doc_token = nlp('Kaike fez café. Ele bebeu 3 xícaras.')
#print(list(doc_token))
print([str(x) for x in list(doc_token)])
for t in doc_token:
    print('{:10} | {} | {} | {} | {}'.format(t.text, t.pos_, t.lemma_, t.dep_, t.is_stop))