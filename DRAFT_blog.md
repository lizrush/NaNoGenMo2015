We'vejust wrapped up November, which means apiring writers all over the world are frantically typing away in an attempt to write an entire novel in one month as part of National Novel Writing Month, also known as NaNoWriMo. Each Novemember, participants aim to write 50,000 words on a 30 day deadline--a difficult feat for any writer! NaNoWriMo has been around for quite a long time, but for the last couple of years programmers and digital artists have been participating in a cheeky alternative: [NaNoGenMo](https://github.com/dariusk/NaNoGenMo-2015), or National Novel Generation Month.

Internet artist Darius Kazemi started NaNoGenMo after tweeting the idea in 2013:

[embed the tweet here https://twitter.com/tinysubversions/status/396305662000775168]

This November is the third organized installment of NaNoGenMo and the community keeps growing every year as more and more programmers & artists become interested in the strange intersection of code, language processing, and literature. And because the event is primarily driven by developers, submissions are posted on a Github repo as Issues so that participants can comment on one another's ideas and help each other create some of the most unique and sometimes nonsensical novels written in November.

In the NaNoGenMo world, "novel" is pretty loosely defined. According to the rules,

> "The “novel” is defined however you want. It could be 50,000 repetitions of the word “meow”. It could literally grab a random novel from Project Gutenberg. It doesn’t matter, as long as it’s 50k+ words."

(And of course, someone *did* make that [50,000 word "meow" book](https://github.com/dariusk/NaNoGenMo-2014/issues/50) in 2014!)

Novel generation can be much more complicated than it appears from the outside. [Some books](https://github.com/dariusk/NaNoGenMo-2014/issues/51) integrate with social media by pulling text from twitter to generate dialogue, [others](https://github.com/samcoppini/Definition-book) go down a recursive rabbithole, and some even generate [graphic novels](http://gregborenstein.com/comics/generated_detective/1/).

Here at Algorithmia, we have a wide variety of algorithms that are a perfect fit for NaNoGenMo. Because I don't have any background in natural language processing or computational linguistics, I found it was easy to combine algorithms to not only help me generate my novel, but gain insights on the texts I used as a basis and the result.

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

Before I started work on generating my own novel based on these texts, I rolled up my sleeves and got to work on analyzing them. The algorithmia platform is already full of many text analysis algorithms, so instead of getting lost in learning natural language processing, it was as simple as choosing an algorithm, passing in my texts, and comparing the results.


Using the [AutoTag algorithm](https://algorithmia.com/algorithms/nlp/AutoTag), I set out to discover if there would be a difference in the topics we'd find between the two author demographics. The Autotag algorithm uses a variant of Latent Dirichlet allocation and returns a set of keywords that reprensent the topics in the text. I then took each of the topics returned  by the algorithm and classified them into various categories or themes to see if we could find some common threads. 

I found out that 

set one:
female person: 16
family person: 8
home-related noun: 5
slavery/race: 4
people/names: average of 4.5 out of 8

set two: 
female person: 28
family person: 4
home-related noun: 2
slavery/race: 0
people/names: average of 5.7 out of 8

While this algorithm gives us some interesting insights into our texts, it can't tell us everything and sometimes it can even trick you. For example, I grew suspicious of Sowing & Reaping when the AutoTag algorithm returned that one of the topics was "romaine". Since I hadn't read this specific book, I looked it up--turned out to be the last name of a main character! 

Sentiment analysis
behind_the_scenes.txt
3
from_the_darkness.txt
1
incidents.txt
1
iola_leroy_harper.txt
1
little_women.txt
1
minnies_sacrifice.txt
1
prophet_smoky_mountains.txt
3
ruth_hall.txt
2
rutledge.txt
0
sowing.txt
1
the_lamplighter.txt
1
trial_and_triumph.txt
1
uncle_toms_cabin.txt
1
what_katy_did.txt
1
woman_in_19th.txt
1



Want to try NLP youself? Check out the [NLTK book](http://www.nltk.org/book/) to get up and running in python.

