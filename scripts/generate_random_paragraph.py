import Algorithmia
import os
import re
from random import randint

client             	= Algorithmia.client('simG4c7kU+Seay4VpjAP3MSovuR1')
text_from_trigram  	= client.algo('/lizmrush/GenerateParagraphFromTrigram')
paragraph_length 	= (randint(1,9))

trigrams_file = "data://.algo/ngram/GenerateTrigramFrequencies/temp/set-two-trigrams.txt"

input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx", paragraph_length]

print text_from_trigram.pipe(input)
