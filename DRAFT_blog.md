We'vejust wrapped up November, which means apiring writers all over the world are frantically typing away in an attempt to write an entire novel in one month as part of National Novel Writing Month, also known as NaNoWriMo. Each Novemember, participants aim to write 50,000 words on a 30 day deadline--a difficult feat for any writer! NaNoWriMo has been around for quite a long time, but for the last couple of years programmers and digital artists have been participating in a cheeky alternative: [NaNoGenMo](https://github.com/dariusk/NaNoGenMo-2015), or National Novel Generation Month.

Internet artist Darius Kazemi started NaNoGenMo after tweeting the idea in 2013:

[embed the tweet here https://twitter.com/tinysubversions/status/396305662000775168]

This November is the third organized installment of NaNoGenMo and the community keeps growing every year as more and more programmers & artists become interested in the strange intersection of code, language processing, and literature. And because the event is primarily driven by developers, submissions are posted on a Github repo as Issues so that participants can comment on one another's ideas and help each other create some of the most unique and sometimes nonsensical novels written in November.

In the NaNoGenMo world, "novel" is pretty loosely defined. According to the rules,

> "The “novel” is defined however you want. It could be 50,000 repetitions of the word “meow”. It could literally grab a random novel from Project Gutenberg. It doesn’t matter, as long as it’s 50k+ words."

(And of course, someone *did* make that [50,000 word "meow" book](https://github.com/dariusk/NaNoGenMo-2014/issues/50) in 2014!)

Novel generation can be much more complicated than it appears from the outside. [Some books](https://github.com/dariusk/NaNoGenMo-2014/issues/51) integrate with social media by pulling text from twitter to generate dialogue, [others](https://github.com/samcoppini/Definition-book) go down a recursive rabbithole, and some even generate [graphic novels](http://gregborenstein.com/comics/generated_detective/1/).

Algorithmia is home to a wide variety of algorithms that are a perfect fit for NaNoGenMo. Because I don't have any background in natural language processing or computational linguistics, I found it was easy to combine algorithms that not only helped me generate my novel, but gave me insights on the texts I used as a basis and the result.

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

Before I started work on generating my own novel based on these texts, I rolled up my sleeves and got to work on analyzing them. The algorithmia platform is already full of many text analysis algorithms, so instead of getting lost in learning natural language processing from scratch, it was as simple as choosing an algorithm, passing in my texts, and comparing the results.

Haven't read any of the books? Don't worry! The first algorithm I ran on the texts was [Summarizer](https://algorithmia.com/algorithms/nlp/Summarizer). This algorithm is pretty straightforward--input text, get back key sentences based on frequency of topics and terms. Read the summaries of [Set One](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/set_one_summarizer_results.txt) and [Set Two](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/set_two_summarizer_results.txt) if you need a literary refresher!

Using the [AutoTag algorithm](https://algorithmia.com/algorithms/nlp/AutoTag), I set out to discover if there would be a difference in the topics we'd find between the two author demographics. The Autotag algorithm uses a variant of Latent Dirichlet allocation and returns a set of keywords that reprensent the topics in the text. I then took each of the topics returned by the algorithm and classified them into various categories or themes to see if we could find some common threads.

[insert graph img here]

I had suspected that the second set of books would have more domestic related themes, but I was mostly unsurprised that there were no autotagged keywords about race or slavery in that set. Interestingly, specific names as keywords were fairly frequent in both sets, averaging 4.8 out of 8 topics for set one and 5.7 of the topics in set two.

While this algorithm gives us some interesting insights into our texts, it can't tell us everything and sometimes it can even trick you. For example, I grew suspicious of Sowing & Reaping when the AutoTag algorithm returned that one of the topics was "romaine". I suspected that this book did not in fact focus on a type of lettuce as a main topic. Since I hadn't read this specific book, I looked it up--turned out to be the last name of a main character!

After running the AutoTag algorithm on my data sets, I decided it check out [Sentiment Analysis](https://algorithmia.com/algorithms/nlp/SentimentAnalysis). This algorithm uses text analysis, natural language processing, and computational linguistics to identify subjective information in text. It's also known as opinion mining. The algorithm I used returns a rating of Very Negative, Negative, Neutral, Positive or Very Positive.

Here's the breakdown of sentiment by book:
Set One:
* Incidents in the Life of a Slave Girl: Negative
* Trial and Triumph: Negative
* From the Darkness Cometh the Light, or, Struggles for Freedom: Negative
* Sowing and Reaping: Negative
* Minnie's Sacrifice: Negative
* Behind the Scenes: Positive
* Iola Leroy, or Shadows Uplifted: Negative

Set Two:
* Woman in the Nineteenth Century: Negative
* Uncle Tom's Cabin: Negative
* The Lamplighter: Negative
* Ruth Hall: A Domestic Tale of the Present Time: Neutral
* Rutledge: Very Negative
* Little Women: Negative
* What Katy Did: Negative

Unsurprisingly, 12 out of 14 of the books I analyzed were Negative or Very Negative. Rough times in the 19th century!

Next, I decided it might be interesting to see what popped up with Profanity Detection. [finsih talking baotu this here]

Now, you've read though all this and you've seen my results, you might be thinking to yourself that you don't know how to do natural language processing so maybe this will be something you put on a project list and try out later. The most amazing part of this project that I haven't told you yet is this secret: every single one of these scripts that I wrote to do NLP and text analysis was **under 30 lines of code.**

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

It's almost mindblowingly fast and simple to get the power of these algorithms into your hands once they are behind a simple API call.




Want to try NLP youself? Check out the [NLTK book](http://www.nltk.org/book/) to get up and running in python.

