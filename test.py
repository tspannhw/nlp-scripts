import spacy
# major upgrade

nlp = spacy.load("en_core_web_sm")
doc = nlp(u"Cloudera is releasing new streaming technologies. Apache NiFi 1.9.1 is one of them.   For my $100,000 Princeton has the best engineers.")

# Named entity recognition
# https://spacy.io/usage/linguistic-features#named-entities

print("--- Named Entities ---")

for ent in doc.ents:
   print(ent.text, ent.start_char, ent.end_char, ent.label_)

print("--- Sentences ---")

for sent in doc.sents:
    print(sent.text)
