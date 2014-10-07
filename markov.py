#!/usr/bin/env python

from sys import argv
import random

script, filename = argv


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chain_dict = {}
    text = corpus.read()
    text = text.strip().split()

    #iterating through the file, if the key is already in the dictionary we
    #will add the new value into the key list, if the key is not in the
    #dictionary, we will add the key value pair
    for i in range(len(text)-2):

        if (text[i], text[i+1],) in markov_chain_dict:
            markov_chain_dict[(text[i], text[i+1],)] += [text[i+2]]
        else:
            markov_chain_dict[(text[i],text[i+1],)] = [text[i+2]]

        #markov_chain_dict[(text[i], text[i+1],)] = markov_chain_dict.get((text[i], text[i+1],), []).append([text[i+2]])
    return markov_chain_dict

def make_text(markov_chain_dict):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    key_tuple = random.choice(markov_chain_dict.keys())
    random_output_text = key_tuple[0] + ' ' + key_tuple[1]

    while key_tuple in markov_chain_dict:

        next_in_chain = random.choice(markov_chain_dict[key_tuple])
        random_output_text = random_output_text + " " + next_in_chain
        key_tuple = (key_tuple[1], next_in_chain,)

    return random_output_text

def main():

    input_text = open(filename)

    chain_dict = make_chains(input_text)

    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
