'''
API requests

Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) 
using their API. The movie you'll query the API about is The Social Network. Recall 
that, in the video, to query the API about the movie Hackers, Hugo's query string 
was 
    'http://www.omdbapi.com/?t=hackers' 
and had a single argument 
    t=hackers.

Note: recently, OMDB has changed their API: you now also have to specify an API key. 
This means you'll have to add another argument to the URL: 
    apikey=ff21610b.

INSTRUCTIONS
100 XP
Import the requests package.
Assign to the variable url the URL of interest in order to query 
'http://www.omdbapi.com' for the data corresponding to the movie 
The Social Network. The query string should have two arguments: apikey=ff21610b and
t=social+network. You can combine them as follows: apikey=ff21610b&t=social+network.
Print the text of the reponse object r by using its text attribute and passing the 
result to the print() function.
'''

