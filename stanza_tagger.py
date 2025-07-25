import stanza
import sys
import re
import os
from timeit import default_timer as timer

# start timing code execution
start = timer()

print("Loading language model...")
nlp = stanza.Pipeline("en", processors="tokenize, lemma, pos", verbose=False)


# input file
input_file = sys.argv[1]

# if the output file has not been specified, the default name will be the name of the input file with the file ending vrt
if len(sys.argv) < 3:
    name, ext = os.path.splitext(input_file)
    output_file = name + ".vrt"
else:
    output_file = sys.argv[2]


print("Annotating...")

# Read the input file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()


def tag_tokens(output_file): 
    # pattern to split XML tags and non-tags
    # group 1: XML tags, group 2: non-tag text
    parts = re.findall(r'(<[^>]+>)|([^<]+)', content)


    with open(output_file, "w", encoding="utf-8") as out:
        for tag, text in parts:
            # print(tag, text)
            if tag:
                # it's an XML tag, so write it unchanged
                out.write(tag + "\n")
            elif text:
                # it's text content, so lemmatize, clean and write
                doc = nlp(text)

                for sentence in doc.sentences:
                    for word in sentence.words:
                        out.write(
                            f"{word.text}\t{word.xpos}\t{word.pos}\t{word.lemma.lower()}\n")

    """ 
    stanza will print each token, the Penn Treebank tag (xpos), 
    the corresponding Universal Dependencies tag (pos) and the lemma (lemma) 
    in all lowercase letters on a new line 
    """


tag_tokens(output_file=output_file)


print(f"Lemmatized text written to {output_file}.")

# end timing code execution
end = timer()

# calculate execution time and convert to minutes
exec_time = (end - start)/60

print(f"Code executed in {str(round(exec_time, 2))} minutes.")
