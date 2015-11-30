import Algorithmia
import os

client		= Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
LDA_algo    = client.algo('mallet/LDA')


corpus 	= []
rootdir = './clean_books/'

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open('./clean_books/' + filename, 'r') as content_file:
      corpus.extend(content_file.read())

input = [corpus, 5]
LDA_result = LDA_algo.pipe(input)

print LDA_result
