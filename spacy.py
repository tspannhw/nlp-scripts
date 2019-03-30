import spacy

# pip3 install -U spacy
# python3 -m spacy download en
# major upgrade

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Cloudera is releasing new streaming technologies.   Apache NiFi 1.9.1 is one of them.")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
