'''
A little bit of Twitter text analysis

Now that you have your DataFrame of tweets set up, you're going to do a bit of text 
analysis to count how many tweets contain the words 'clinton', 'trump', 'sanders' 
and 'cruz'. In the pre-exercise code, we have defined the following function 
word_in_text(), which will tell you whether the first argument (a word) occurs 
within the 2nd argument (a tweet).

import re

def word_in_text(word, text):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False
    
You're going to iterate over the rows of the DataFrame and calculate how many 
tweets contain each of our keywords! The list of objects for each candidate has 
been initialized to 0.

INSTRUCTIONS
100 XP
Within the for loop for index, row in df.iterrows():, the code currently increases 
the value of clinton by 1 each time a tweet mentioning 'Clinton' is encountered; 
complete the code so that the same happens for trump, sanders and cruz.
'''

