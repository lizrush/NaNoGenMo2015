import Algorithmia
import os

client = Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
algo = client.algo('diego/WordFrequencyCounter')
corpus 	= []
rootdir = './clean_books/'

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open('./clean_books/' + filename, 'r') as content_file:
      input = content_file.read()
      print filename 
      print algo.pipe(input)
