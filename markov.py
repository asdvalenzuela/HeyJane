#!/usr/bin/env python

from sys import argv
import random
import os
import twitter 
api = twitter.Api()

script, filename, filename2 = argv


def make_chains(corpus,n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chain_dict = {}
    text = corpus.read()
    text = text.strip().split()

    
    for i in range(len(text)-n):
        key_list = []
        for j in range(n):
            key_list.append(text[i+j])
        key_tuple = tuple(key_list)
        if key_tuple in markov_chain_dict:
            markov_chain_dict[key_tuple] += [text[i+n]]
        else:
            markov_chain_dict[key_tuple] = [text[i+n]]
        
    if len(key_tuple) != n:
        del markov_chain_dict[key_tuple]
    return markov_chain_dict

def make_text(markov_chain_dict, n, random_text1 = None):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    if random_text1 == None:
        random_output_text = ""
        key_tuple = random.choice(markov_chain_dict.keys())
    else:
        random_output_text = random_text1
        last_word = random_text1.split()[-1]
        mc_keys = markov_chain_dict.keys()
        for a_key in mc_keys:
            if last_word == a_key[0]:
                key_tuple = a_key
            else:
                key_tuple = random.choice(markov_chain_dict.keys())

    key_list = list(key_tuple)    
    for index in range(len(key_list)):
        random_output_text = random_output_text + " " + key_list[index]

    # while key_tuple in markov_chain_dict:
    # while random_output_text[-1] not in end_punctuation:
    for times in range(100):
        if len(key_tuple) == n:
             next_in_chain = random.choice(markov_chain_dict[key_tuple])
    #         print("next_in_chain",next_in_chain)
             random_output_text = random_output_text + " " + next_in_chain

             fake_tuple = list(key_tuple)
             fake_tuple = fake_tuple[1:]
             fake_tuple.append(next_in_chain)
             key_tuple = tuple(fake_tuple)

    #end_punctuation = ['.','!','?']


    # if end_punctuation[0] in random_output_text or end_punctuation[1] in random_output_text or end_punctuation[2] in random_output_text:
    #     twitter_output = ''
    #     for achar in random_output_text:
    #         if len(twitter_output) > 140:
    #             break
    #         elif achar not in end_punctuation:
    #             twitter_output += achar
    #         else:
    #             twitter_output +=achar
    #             break
    # if twitter_output:
    #     return twitter_output


    # else:
    return random_output_text #[0:139]


def twitter_it(random_text1, random_text2):
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
    ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
    api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token_key=ACCESS_TOKEN_KEY, access_token_secret=ACCESS_TOKEN_SECRET)
    
    tweet = random_text2[len(random_text1)-70:len(random_text1)+70]


    for achar in tweet:
         if achar == " ":
             first_space = tweet.index(achar)
             break
    for index in range(len(tweet)):
         if tweet[-1*index] == " ":
             last_space = index

    real_tweet = tweet[first_space+1:last_space]
    print "tweet: "
    print tweet
    print "real tweet: first space, last_space"
    print real_tweet, first_space, last_space

    api.PostUpdate(real_tweet)

def main():

    n = 5
    #markov_chain_dict = {}

    input_text = open(filename)
    input_text2 = open(filename2)

    chain_dict1 = make_chains(input_text,n)
    chain_dict2 = make_chains(input_text2,n)


    random_text1 = make_text(chain_dict1,n)
    random_text2 = make_text(chain_dict2,n, random_text1)
    twitter_it(random_text1,random_text2)

if __name__ == "__main__":
    main()
