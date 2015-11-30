import Algorithmia
import os
import re
from random import randint

client             	= Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
text_from_trigram  	= client.algo('/lizmrush/GenerateParagraphFromTrigram')
book_title 		 	= 'set_two_book.txt'

trigrams_file = "data://.algo/ngram/GenerateTrigramFrequencies/temp/set-two-trigrams.txt"

book = ''
word_count = len(re.findall(r'\w+', book))

print word_count

while len(re.findall(r'\w+', book)) < 500:
  print "Generating new paragraph"
  input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx", (randint(1,9))]
  new_paragraph = text_from_trigram.pipe(input)
  book += new_paragraph
  book += '\n'
  print "updated word_count:"
  print len(re.findall(r'\w+', book))

with open(book_title, 'w') as f:
    f.write(book)

f.close()

print "Done!"

