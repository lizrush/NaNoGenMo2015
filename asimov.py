import Algorithmia

client = Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')

with open('./youth.txt', 'r') as content_file:
    input = content_file.read()

algo = client.algo('StanfordNLP/SentenceSplit/0.1.0')
sentences = algo.pipe(input)


input = [sentences, "xxBeGiN142xx", "xxEnD142xx", "data://.algo/ngram/GenerateTrigramFrequencies/temp/trigrams.txt"]
algo = client.algo('ngram/GenerateTrigramFrequencies/0.1.1')
trigrams_file = algo.pipe(input)


input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx"]
algo = client.algo('ngram/RandomTextFromTrigram/0.1.1')
print algo.pipe(input)