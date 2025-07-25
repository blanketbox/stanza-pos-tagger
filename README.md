## Using stanza_tagger.py

Use this script on the command line: 

```python3 stanza_tagger.py input_file destination_file``` 

The script will automatically create a new file with the name given in place of "destination_file".

If no destination file is specified, the name of the destination file will be the name of the input file with the file extension ".vrt".

The script creates a VRT-file to be used with the IMS Open Corpus Workbench. XML-tags will be written to the destination file unchanged. Find out more about VRT-files here: https://fedora.clarin-d.uni-saarland.de/teaching/Comparing_Corpora_Tutorials/Tutorial_VRT.html

Instead of using ```stanza_tagger.py```, though, you can use the notebook for Google Colab called ```stanza-pos-tagger.ipynb``` with the added advantage of running the code with a hardware accelerator (GPU). With large text files, the difference in speed can be significant. 

The file ```requirements.txt``` only lists the dependencies for ```stanza_tagger.py```. 