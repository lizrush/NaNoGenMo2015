import Algorithmia
import os

client = Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
sentence_split		= client.algo('StanfordNLP/SentenceSplit/0.1.0')
generate_trigrams 	= client.algo('ngram/GenerateTrigramFrequencies/0.1.1')
text_from_trigram	= client.algo('ngram/RandomTextFromTrigram/0.1.1')

corpus 	= []
rootdir = './books/WF authors'

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open('./books/WF authors/' + filename, 'r') as content_file:
      input = content_file.read()
      sentences = sentence_split.pipe(input)
      corpus.extend(sentences)


#  generate trigrams
input = [corpus, "xxBeGiN142xx", "xxEnD142xx", "data://.algo/ngram/GenerateTrigramFrequencies/temp/trigrams-WF.txt"]
trigrams_file = generate_trigrams.pipe(input)

# generate sentence
input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx"]

print text_from_trigram.pipe(input)