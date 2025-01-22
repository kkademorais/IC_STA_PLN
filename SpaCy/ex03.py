import spacy
from spacy import load

spacy.load('pt_core_news_sm')
nlp = load('pt_core_news_sm')
text = '''
João amava Teresa que amava Raimundo
que amava Maria que amava Joaquim que amava Lili
que não amava ninguém.
João foi para os Estados Unidos, Teresa para o convento,
Raimundo morreu de desastre, Maria ficou para tia,
Joaquim suicidou-se e Lili casou com J. Pinto Fernandes
que não tinha entrado na história
'''
doc = nlp(text)
print(doc.ents)

documento_ent = nlp('Kaike foi estagiar na Microsoft na Califórnia, nos Estados Unidos.')

for ent in documento_ent.ents:
    print('{:15} | {}'.format(
        ent.text,
        ent.label_
    ))
