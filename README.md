# tweep
Generating public tweets based on a specific region. 

We will achieve this by using the RESTful api of twitter. The api is handled using tweepy, 
which uses Python(3.6).

### Authentication 
First, sign in to Twitter at [Twitter apps](https://apps.twitter.com/) and create a new app
by filling up the application details. Then you should have your ```consumer_token``` and 
```consumer_secret```. 
Then run the code given in filtered_tweets.py and follow the instructions.

### Output
This saves the specified number of location filtered (geo-tagged tweets only) in a file called india_data.txt
in the same directory as the source file. 
