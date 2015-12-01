We've just wrapped up November, which means apiring writers all over the world are frantically typing away in an attempt to finish an entire novel in one month as part of National Novel Writing Month, also known as NaNoWriMo. Each Novemember, participants aim to write 50,000 words on a 30 day deadline--a difficult feat for any writer! NaNoWriMo has been around for quite a long time, but for the last couple of years programmers and digital artists have been participating in a cheeky alternative: [NaNoGenMo](https://github.com/dariusk/NaNoGenMo-2015), or National Novel Generation Month.

Internet artist Darius Kazemi started NaNoGenMo after tweeting the idea in 2013:

[embed the tweet here https://twitter.com/tinysubversions/status/396305662000775168]

This November is the third organized installment of NaNoGenMo and the community keeps growing every year as more and more programmers & artists become interested in the strange intersection of code, language processing, and literature. And because the event is primarily driven by developers, submissions are posted on a Github repo as Issues so that participants can comment on one another's ideas and help each other create some of the most unique and sometimes nonsensical novels written in November.

In the NaNoGenMo world, "novel" is pretty loosely defined. According to the rules,

> "The “novel” is defined however you want. It could be 50,000 repetitions of the word “meow”. It could literally grab a random novel from Project Gutenberg. It doesn’t matter, as long as it’s 50k+ words."

(And of course, someone *did* make that [50,000 word "meow" book](https://github.com/dariusk/NaNoGenMo-2014/issues/50) in 2014!)

Novel generation can be much more complicated than it appears from the outside. [Some books](https://github.com/dariusk/NaNoGenMo-2014/issues/51) integrate with social media by pulling text from twitter to generate dialogue, [others](https://github.com/samcoppini/Definition-book) go down a recursive rabbithole, and some even generate [graphic novels](http://gregborenstein.com/comics/generated_detective/1/).

Algorithmia is home to a wide variety of algorithms that are a perfect fit for NaNoGenMo. Because I don't have any background in natural language processing or computational linguistics, I found it was easy to combine algorithms that not only helped me generate my novel, but gave me insights on the texts I used as a basis.

I chose the texts I wanted to work with based on two things: availability in the public domain and to have an interesting author demographic. While there are tons of NaNoGenMo books out there that are based on other texts, I wanted to find a really unique set of texts to base my novel on. I also developed an interest in 19th century American literature after reading Uncle Tom's Cabin when I was 12. Luckily for me, Project Gutenberg is home to many novels and autobiographies that fit this intersection of interests!

First step: compile a corpus of texts. I chose to go with two sets of 7 books to compare. The first set was composed of primarily slave and emanicpation narratives from Black female authors. While digging around in these texts, I realized that books as seemingly disparate as Little Women were published at the same time. Somehow I have never really thought about how such drastically different worlds were becoming exposed in what we now think of as classic American literature, so I decided it would be interested to compare. The second set of texts are all from white female authors and published around the mid-19th century.

Set one:
* 1861 - Incidents in the Life of a Slave Girl by Harriet Jacobs
* 1868 to 1888 (published in serial form) - Trial and Triumph by Frances Ellen Watkins Harper
* 1868 to 1888 (published in serial form) - Sowing and Reaping: A Temperance Story by Frances Ellen Watkins Harper
* 1868 to 1888 (published in serial form) - Minnie's Sacrifice by Frances Ellen Watkins Harper
* 1868 - Behind the Scenes by Elizabeth Keckley
* 1891 - From the Darkness Cometh the Light, or, Struggles for Freedom by Lucy Delaney
* 1892 - Iola Leroy, or Shadows Uplifted by Frances Ellen Watkins Harper

Set two:
* 1845 - Woman in the Nineteenth Century by Margaret Fuller
* 1852 - Uncle Tom's Cabin by Harriet Beecher Stowe
* 1854 - The Lamplighter by Maria S. Cummins
* 1854 - Ruth Hall: A Domestic Tale of the Present Time by Fanny Fern (pen name of Sara Payson Willis)
* 1860 - Rutledge by Miriam Coles Harris
* 1868 - Little Women by Louisa May Alcott
* 1869 to 1870 (published in serial form) - An Old Fashioned Girl by Louisa May Alcott
* 1872 - What Katy Did by Susan Coolidge

Before I started generating my own novel based on these texts, I rolled up my sleeves and got to work on analyzing them. The Algorithmia platform is already full of many text analysis algorithms, so instead of getting lost in learning natural language processing from scratch, it was as simple as choosing an algorithm, passing in my texts, and comparing the results.

Haven't read any of the books? Don't worry! The first algorithm I ran on the texts was [Summarizer](https://algorithmia.com/algorithms/nlp/Summarizer). This algorithm is pretty straightforward--input text, get back key sentences based on frequency of topics and terms. Read the summaries of [Set One](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/set_one_summarizer_results.txt) and [Set Two](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/set_two_summarizer_results.txt) if you need a literary refresher!

Using the [AutoTag algorithm](https://algorithmia.com/algorithms/nlp/AutoTag), I set out to discover if there would be a difference in the topics we'd find between the two author demographics. The Autotag algorithm uses a variant of Latent Dirichlet allocation and returns a set of keywords that reprensent the topics in the text. I then took each of the topics returned by the algorithm and classified them into various categories or themes to see if we could find some common threads.

[insert autotag graph img here]

I had suspected that the second set of books would have more domestic related themes, but I was mostly unsurprised that there were no autotagged keywords about race or slavery in that set. Interestingly, specific names as keywords were fairly frequent in both sets, averaging 4.8 out of 8 topics for set one and 5.7 of the topics in set two.

While this algorithm gives us some interesting insights into our texts, it can't tell us everything and sometimes it can even trick you. For example, I grew suspicious of Sowing & Reaping when the AutoTag algorithm returned that one of the topics was "romaine". I suspected that this book did not in fact focus on a type of lettuce as a main topic. Since I hadn't read this specific book, I looked it up--turned out to be the last name of a main character!

After running the AutoTag algorithm on my data sets, I decided it check out [Sentiment Analysis](https://algorithmia.com/algorithms/nlp/SentimentAnalysis). This algorithm uses text analysis, natural language processing, and computational linguistics to identify subjective information in text. It's also known as opinion mining. The algorithm I used returns a rating of Very Negative, Negative, Neutral, Positive or Very Positive.

Here's the breakdown of sentiment by book:

| Set One Books | Sentiment | Set Two Books | Sentiment |
|---|---|---|---|
|Incidents in the Life of a Slave Girl | Negative|Woman in the Nineteenth Century|Negative|
|Trial and Triumph|Negative|Uncle Tom's Cabin|Negative|
|From the Darkness Cometh the Light|Negative|The Lamplighter|Negative|
|Sowing and Reaping|Negative|Ruth Hall|Neutral|
|Minnie's Sacrifice|Negative|Rutledge|Very Negative|
|Behind the Scenes|Positive|Little Women|Negative|
|Iola Leroy|Negative| What Katy Did|Negative|

Unsurprisingly, 12 out of 14 of the books I analyzed were Negative or Very Negative. Rough times in the 19th century!

Next, I decided it might be interesting to see what popped up with [Profanity Detection](https://algorithmia.com/algorithms/nlp/ProfanityDetection). While getting the data into the algorithm and writing the results back to a file was easy, it turns out that profanity detection requires a lot of double checking by hand. I knew that some words that came up were not really profane back then; words like "queer", "pussy", and "muff" were innocent in the context of these 19th century texts.

Interestingly, the frequency of racial profanity of the two data sets ended up being relatively similar:

[insert profanity graphic here]

Of course running the algorithm doesnt give you the full picture since in our second set of data about 95% of the racial profanity came from one book: Uncle Tom's Cabin. This is unsurprising since it's the only work in our second set of books that was written by an aboloitionist. However, we still don't quite get the full picture about profanity in these books: many of the words used were not considered slurs back then, and additionally, within the use of dialogue this kind of language takes on a different dimension. The thing we can learn from an algorithm such as Profanity Detection is that there is a very stark different in who these books focused on as main characters and what kind of world they lived in. Four of the seven books written by white authors had zero instances of these words.

---

Now, you've read though all this and you've seen the results from all these different algorithms, you might be thinking to yourself that you don't know how to do natural language processing so maybe this will be something you put on a project list and try out later. The most amazing part of this project that I haven't told you yet is this: every single one of the scripts that I wrote to do NLP and text analysis was **under 30 lines of code.**

Check out the script I wrote for running the AutoTag algorithm:

```
import Algorithmia
import os
import json

client = Algorithmia.client('my_api_key')
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
```

After analyzing all my books, it was time to generate my novel to complete NaNoGenMo. This was so easy compared to the text analysis! Once again, with just simple API calls, I generated trigram models based on each set of books. I then made book previews based on each trigram model just to see if you could hear a difference in the books generated on these different demographics.

The [book preivew from Set One](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/generated%20texts/set_one_book_preview.txt):
> Dem young uns vil kill you dead than to see you. Well, you would be less unhappy marriages if labor were more women in the midst of her nice pudding, as there are no enemies to good old aunt, and confirm themselves in woods and gloomy clouds hung like graceful draperies. Talk about the streets of the ballot in his land, that those who have fitted their children?
> ...
> Belle, and I live in such dingy, humble quarters. said Mrs. Underhill, from my own sorrow-darkened home, I did, that he had asked them. Do you remember the incident so well were given to Frederick Douglass contributed $200, besides lecturing for us. The President added: Man is a fair specimen of her negro blood in his friendship, but they may be an old woman entered her home with me? If the vessel had been. Reader, I felt humiliated enough.

The [book preivew from Set Two](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/generated%20texts/set_two_book_preview.txt):

> aw! Yes, said Miss Skinlin she hasn't the first heir to the female figure. The waves dance bright and happy when I forgot to learn, before which she told me to read and study. My Uncle, with a commanding, What are you better than Kintuck.

> It was useless to ask one last word I ran down a corridor as dark and narrow streets or the other.

> No Oh, Earth! And no one interfered, and it was. but then strangers came so by letting out all fear and distress and doubts of the damned, as well as bodies. What word Can we not get. I don't resent the sarcasm, and unsettled most of my observing her to rise. Fortunately the gate swinging in the recesses, chrysanthemums and Christmas roses bloomed as freshly as in her voice, what everybody finds in the streets so, for the best thing was insufferably disgusting and loathsome to me. I said a thing as leisure there.

The most interesting difference I found in the text generated from these different data sets was that the text from Set Two sounded much more formal. The first set of books, the ones written by Black authors, tended to have much more dialogue written in such a way as to let the reader hear the accents and dialects of the time. These words became part of the model to generate text, so as you can see in the first sentence of the Set One preview, the algorithm generated text that still makes a lot of sense even with words that are intended to showcase an accent.

In the end, I decided to create a trigram model based on both sets of text and use that to generate my full length novel. I didn't have to do any fancy code, I merely made another API call to the [Generate Trigram Frequencies](https://algorithmia.com/algorithms/ngram/GenerateTrigramFrequencies) algorithm, this time passing in the entirety of my data set. Then, to generate my novel, I wrote a quick script that calls into another algorithm: [Generate Paragraph From Trigram](https://algorithmia.com/algorithms/lizmrush/GenerateParagraphFromTrigram). This algorithm uses the trained trigram model to generate paragraphs of text. Since NaNoGenMo requires the book to be at least 50,000 words, I simply wrote a loop that calls the Generate Paragraph algorithm until the total word count of the book reaches the goal:

```
import Algorithmia
import os
import re
from random import randint

client              = Algorithmia.client('my_api_key')
text_from_trigram = client.algo('/lizmrush/GenerateParagraphFromTrigram')
trigrams_file     = "data://.algo/ngram/GenerateTrigramFrequencies/temp/all-trigrams.txt"

book_title      = 'full_book.txt'
book        = ''
book_word_length  = 50000

while len(re.findall(r'\w+', book)) < book_word_length:
  print "Generating new paragraph..."
  input = [trigrams_file, "xxBeGiN142xx", "xxEnD142xx", (randint(1,9))]
  new_paragraph = text_from_trigram.pipe(input)
  book += new_paragraph
  book += '\n\n'
  print "Updated word count:"
  print len(re.findall(r'\w+', book))

with open(book_title, 'w') as f:
    f.write(book.encode('utf8'))

f.close()

print "Done!"
print "You book is now complete. Give " + book_title + " a read now!"
```

Even with extra new lines for readability, the code I needed to generate an entire novel with Algorithmia was still under 30 lines! And I ended up generating a really unique, interesting novel without getting lost in the highly technical parts of natural language generation. Now, the text isn't perfect: sometimes the sentences don't quite sound right and there isn't really any sort of story arch, but for such simple code I think it's pretty good! My favorite part about using 19th century texts as the data set was that sometimes you can't tell if the generated text is hard to read because it's generated and doesn't make much sense or because it sounds so old-timey. My book includes the following gems that just might pass as human-written text:

>I have said of human life when I saw the Ohio river, that you shall work.

>Still, falsehood may be hearing you. She only 'spects something. Them curls may make a noise you shall not.

You can read the book, or rather, attempt to read the book, [online](http://lizrush.github.io/NaNoGenMo2015) or you can download it [from the repo](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/generated%20texts/full_book.txt).

It's mindblowingly fast and simple to get the power of these algorithms into your hands once they are behind a simple API call. You can see all the other scripts I wrote in the [GitHub repo](https://github.com/lizrush/NaNoGenMo2015) for this project. If you browse around, you'll see that each script is nearly identical. The only real changes I had to make were replacing the algorithm I was calling and what I named the files to write results to! The Algorithmia platform is an incredibly powerful tool. Instead of spending days, weeks, months learning how to code my own natural language processing and text analysis algorithms, I could just pop my data into a variety of algorithms with simple API calls. No sweat, just results.
