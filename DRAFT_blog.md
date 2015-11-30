We're coming up on the end of November, which means apiring writers all over the world are frantically typing away in an attempt to write an entire novel in one month as part of National Novel Writing Month, also known as NaNoWriMo. Each Novemember, participants aim to write 50,000 words on a 30 day deadline--a difficult feat for any writer! NaNoWriMo has been around for quite a long time, but for the last couple of years programmers and digital artists have been participating in a cheeky alternative: [NaNoGenMo](https://github.com/dariusk/NaNoGenMo-2015), or National Novel Generation Month.

Internet artist Darius Kazemi started NaNoGenMo after tweeting the idea in 2013:

[embed the tweet here https://twitter.com/tinysubversions/status/396305662000775168]

This November is the third organized installment of NaNoGenMo and the community keeps growing every year as mor and more programmers & artists become interested in the strange intersection of tech, language processing, and literature. And because the event is primarily driven by developers, submissions are posted on a Github repo as Issues so that participants can comment on one another's ideas and help each other create some of the most unique and sometimes nonsensical novels written in November.

In the NaNoGenMo world, "novel" is pretty loosely defined. According to the rules,

> "The “novel” is defined however you want. It could be 50,000 repetitions of the word “meow”. It could literally grab a random novel from Project Gutenberg. It doesn’t matter, as long as it’s 50k+ words."

(And of course, someone *did* make that [50,000 word "meow" book](https://github.com/dariusk/NaNoGenMo-2014/issues/50) in 2014!)

Novel generation can be much more complicated than it appears from the outside. [Some books](https://github.com/dariusk/NaNoGenMo-2014/issues/51) integrate with social media by pulling text from twitter to generate dialogue, [others](https://github.com/samcoppini/Definition-book) go down a recursive rabbithole, and some even generate [graphic novels](http://gregborenstein.com/comics/generated_detective/1/).

Here at Algorithmia, we have a wide variety of algorithms that are a perfect fit for NaNoGenMo. Because I don't have any background in natural language processing or computational linguistics, I found it was easy to combine algorithms to not only help me generate my novel, but gain insights on the texts I used as a basis and the result.


I chose the texts I wanted to work with based on two things: availability in the public domain and to have an interesting author demographic. While there are tons of NaNoGenMo books out there that are based on other texts, the unfortunate truth is that I see very few that are based on female or minority authors. I also developed an interest in 19th century American literature, slave and emancipation narratives in particular, after reading Uncle Tom's Cabin when I was 12. Luckily for me, Project Gutenberg is home to many novels and autobiographies that fit this intersection of interests!

First step: compile a corpus of texts. I chose to go with two sets of 8 books to compare. The first set was composed of

Set one:
* 1859 - Our Nig by Harriet E. Wilson
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
* 1885 - The Prophet of the Great Smoky Mountains by Charles Egbert Craddock (pen name of Mary Noailles Murfree)


Second, clean the texts (I used [guten-gutter](https://github.com/catseye/Guten-gutter)). Then I had to escape " marks so that I could run algos that take text inputs.


AUTOTAG:
black authors
['dsdb', 'bud']
['mrs', 'lincoln', 'president', 'day', 'house', 'mother', 'room', 'time']
['mother', 'mrs', 'time', 'judge', 'mitchell', 'freedom', 'free', 'girl']
['children', 'grandmother', 'told', 'master', 'slave', 'house', 'day', 'time']
['war', 'robert', 'iola', 'mother', 'dat', 'good', 'ter', 'ole']
['louis', 'minnie', 'child', 'colored', 'home', 'race', 'mother', 'people']
['belle', 'life', 'mother', 'home', 'romaine', 'jeanette', 'man', 'john']
['annette', 'mrs', 'life', 'young', 'men', 'people', 'man', 'thomas']
white authors
['meg', 'amy', 'laurie', 'good', 'beth', 'mother', 'time', 'made']
['ter', 'hev', 'war', 'air', 'man', 'fur', 'thar', 'eyes']
['ruth', 'doctor', 'katy', 'mrs', 'time', 'eyes', 'nettie', 'lady']
['rutledge', 'mrs', 'kitty', 'time', 'room', 'back', 'door', 'made']
['gertrude', 'emily', 'mrs', 'gerty', 'miss', 'willie', 'time', 'graham']
['tom', 'man', 'miss', 'clare', 'good', 'ophelia', 'george', 'child']
['katy', 'aunt', 'izzie', 'clover', 'cousin', 'children', 'helen', 'elsie']
['woman', 'man', 'life', 'men', 'women', 'love', 'thought', 'nature']


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

