import Algorithmia
import os
import json

client = Algorithmia.client('YOUR_API_KEY_HERE')
algo = client.algo('nlp/AutoTag/0.1.4')

rootdir = './clean_books/set_one/'
output_file = 'set_one_autotag_results.txt'
results = ''

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open(rootdir + filename, 'r') as content_file:
      input = content_file.read()
      print "Autotagging " + filename
      results += filename + "\n\n"
      results += json.dumps(algo.pipe(input))
      results += "\n\n"


with open(output_file, 'w') as f:
   f.write(results)

f.close()

print "Done!"
