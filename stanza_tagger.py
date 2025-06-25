import stanza
import sys
import re
from timeit import default_timer as timer

# print("Downloading English model...")
# stanza.download('en', verbose=False)

# start timing code execution
start = timer()

print("Loading language model...")
nlp = stanza.Pipeline("en", processors="tokenize, lemma, pos", verbose=False)


# Input file 
input_file = sys.argv[1]

# If the output file has not been specified the default name will be the name of the input file with the file ending vrt
if len(sys.argv) < 3:
    output_file = "{}.vrt".format(sys.argv[1][:4])
else: 
    output_file = sys.argv[2]



print("Annotating...")

# Read the input file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern to split XML tags and non-tags
# Group 1: XML tags; Group 2: non-tag text
parts = re.findall(r'(<[^>]+>)|([^<]+)', content)

# print(parts)

with open(output_file, "w", encoding="utf-8") as out:
    for tag, text in parts:
        if tag:
            # It's an XML tag — write it unchanged
            out.write(tag + "\n")
        elif text:
            # It's text content — lemmatize, clean and write
            doc = nlp(text)

            for sentence in doc.sentences: 
                for word in sentence.words:
                    out.write("{}\t{}\t{}\t{}\n".format(word.text, word.pos, word.xpos, word.lemma.lower()))

""" 
stanza will print each token, the corresponding Penn Treebank tag (xpos),
the Universal Dependencies tag (pos) and
the lemma (lemma) in all lowercase letters for everything that is not whitespace
on a new line 
"""

print(f"Lemmatized text written to '{output_file}'.")

# end timing code execution
end = timer()

# calculate execution time and convert to minutes
exec_time = (end - start)/60

print("Code executed in " + str(round(exec_time, 2)) + " minutes.")
