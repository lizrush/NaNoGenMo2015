import Algorithmia
import os

client            = Algorithmia.client('YOUR_API_KEY_HERE')
sentence_split    = client.algo('StanfordNLP/SentenceSplit/0.1.0')
generate_trigrams	= client.algo('ngram/GenerateTrigramFrequencies/0.1.1')
trigram_file_name	= "set-one-trigrams.txt"

corpus  = []
rootdir = './clean_books/set_one/'
book 		= ''

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open(rootdir + filename, 'r') as content_file:
      input = content_file.read()
      sentences = sentence_split.pipe(input)
      corpus.extend(sentences)

#  generate trigrams
input = [corpus,
        "xxBeGiN142xx",
        "xxEnD142xx",
        "data://.algo/ngram/GenerateTrigramFrequencies/temp/" + trigram_file_name]

trigrams_file = generate_trigrams.pipe(input)

print "Done!"
print "Your trigrams file is now available on Algorithmia."

