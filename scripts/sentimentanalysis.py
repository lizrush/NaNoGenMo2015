import Algorithmia
import os
import json

algo 	= client.algo('nlp/sentimentanalysis')

rootdir 	= './clean_books/set_one/'
output_file = 'set_one_sentiment_results.txt'
results 	= ''

for subdir, dirs, files in os.walk(rootdir):
  for filename in files:
    with open(rootdir + filename, 'r') as content_file:
      input = content_file.read()
      print "Running Sentiment Analysis on " + filename
      results += filename + "\n\n"
      results += json.dumps(algo.pipe(input))
      results += "\n\n"


with open(output_file, 'w') as f:
   f.write(results)

f.close()

print "Done!"

