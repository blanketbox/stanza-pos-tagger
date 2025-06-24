import stanza

# print("Downloading English model...")
# stanza.download('en', verbose=False)

print("Loading language model...")
en_nlp = stanza.Pipeline("en", processors="tokenize, lemma, pos", verbose=False)

print("Annotating...")

en_doc = en_nlp("this is the text.")

#print(type(en_doc))

for i, sent in enumerate(en_doc.sentences):

    for word in sent.words:
        print("{}\t{}\t{}\t{}\n".format(word.text, word.pos, word.xpos, word.lemma.lower()))
