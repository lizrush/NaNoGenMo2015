This repo is home to the NaNoGenMo book "Not-So-Little-Women", which can be found as [a .txt file](https://github.com/lizrush/NaNoGenMo2015/blob/master/results/generated%20texts/full_book.txt) or you can read [the full text online](http://lizrush.github.io/NaNoGenMo2015).

This book was generated based on a trigram model that was trained using two sets of data. Each set contains 7 books written by female authors in the 19th century United States.

Set one:
1861 - Incidents in the Life of a Slave Girl by Harriet Jacobs
1868 to 1888 (published in serial form) - Trial and Triumph by Frances Ellen Watkins Harper
1868 to 1888 (published in serial form) - Sowing and Reaping: A Temperance Story by Frances Ellen Watkins Harper
1868 to 1888 (published in serial form) - Minnie's Sacrifice by Frances Ellen Watkins Harper
1868 - Behind the Scenes by Elizabeth Keckley
1891 - From the Darkness Cometh the Light, or, Struggles for Freedom by Lucy Delaney
1892 - Iola Leroy, or Shadows Uplifted by Frances Ellen Watkins Harper

Set two:
1845 - Woman in the Nineteenth Century by Margaret Fuller
1852 - Uncle Tom's Cabin by Harriet Beecher Stowe
1854 - The Lamplighter by Maria S. Cummins
1854 - Ruth Hall: A Domestic Tale of the Present Time by Fanny Fern (pen name of Sara Payson Willis)
1860 - Rutledge by Miriam Coles Harris
1868 - Little Women by Louisa May Alcott
1872 - What Katy Did by Susan Coolidge


These books were analyzed using algorithms such as [AutoTaggin](https://algorithmia.com/algorithms/nlp/AutoTag), [Profanity Detection](https://algorithmia.com/algorithms/nlp/ProfanityDetection), [Summarizer](https://algorithmia.com/algorithms/nlp/Summarizer), and [Sentiment Analysis](https://algorithmia.com/algorithms/nlp/SentimentAnalysis). The scripts can be found in the `scripts` directory. Just simply stick in your API code and you're good to go! Run them from the root directory with `python scripts/autotag.py` and it will generate an output file for you. Feel free to tweak the scripts or replace the source data to run on your own texts!

Read more about NaNoGenMo 2015 [here](https://github.com/dariusk/NaNoGenMo-2015).
