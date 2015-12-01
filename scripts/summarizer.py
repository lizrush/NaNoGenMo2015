import Algorithmia
import os
import json

client = Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
algo = client.algo('nlp/Summarizer')

rootdir = './clean_books/set_two/'
output_file = 'set_two_summarizer_results.txt'
results = ''

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open(rootdir + filename, 'r') as content_file:
      input = content_file.read()
      print "Summarizing " + filename 
      results += filename + "\n\n"
      results += json.dumps(algo.pipe(input))
      results += "\n\n"


with open(output_file, 'w') as f:
   f.write(results)

f.close()	

print "Done!"

