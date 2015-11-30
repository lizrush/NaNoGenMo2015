import Algorithmia
import os
import re

client             = Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
sentence_split     = client.algo('StanfordNLP/SentenceSplit/0.1.0')
generate_trigrams  = client.algo('ngram/GenerateTrigramFrequencies/0.1.1')
text_from_trigram  = client.algo('/lizmrush/GenerateParagraphFromTrigram')

corpus  = []
rootdir = './clean_books/'
book = ''

# for subdir, dirs, files in os.walk(rootdir):
#   for filename in files:
#     with open('./clean_books/' + filename, 'r') as content_file:
#       input = content_file.read()
#       sentences = sentence_split.pipe(input)
#       corpus.extend(sentences)

# #  generate trigrams
# input = [corpus,
#         "xxBeGiN142xx",
#         "xxEnD142xx",
#         "data://.algo/ngram/GenerateTrigramFrequencies/temp/trigrams-for-generation.txt"]

# trigrams_file = generate_trigrams.pipe(input)
trigrams_file = "data://.algo/ngram/GenerateTrigramFrequencies/temp/trigrams-for-generation.txt"

word_count = len(re.findall(r'\w+', book))

print word_count

while len(re.findall(r'\w+', book)) < 500:
# generate paragraph
  input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx", 7]
  print "generating new paragraph"
  new_paragraph = text_from_trigram.pipe(input)
  book += new_paragraph
  book += '\n'
  print "updated word_count:"
  print len(re.findall(r'\w+', book))

with open('new_book.txt', 'w') as f:
    f.write(book)

f.close()

print "done!"

