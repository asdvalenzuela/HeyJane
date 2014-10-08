#!/usr/bin/env python

from sys import argv
import random

script, filename = argv


def make_chains(corpus,n):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chain_dict = {}
    text = corpus.read()
    text = text.strip().split()

    #iterating through the file, if the key is already in the dictionary we
    #will add the new value into the key list, if the key is not in the
    #dictionary, we will add the key value pair

#this totally worked:

  # for i in range(len(text)-2):

  #       if (text[i], text[i+1],) in markov_chain_dict:
  #           markov_chain_dict[(text[i], text[i+1],)] += [text[i+2]]
  #       else:
  #           markov_chain_dict[(text[i],text[i+1],)] = [text[i+2]]

  #       #markov_chain_dict[(text[i], text[i+1],)] = markov_chain_dict.get((text[i], text[i+1],), []).append([text[i+2]])
  #   return markov_chain_dict

    
    for i in range(len(text)-n):
        key_list = []
        for j in range(n):
            key_list.append(text[i+j])
        key_tuple = tuple(key_list)

        if key_tuple in markov_chain_dict:
            markov_chain_dict[key_tuple] += [text[i+n]]
        else:
            markov_chain_dict[key_tuple] = [text[i+n]]
        
        #markov_chain_dict[(text[i], text[i+1],)] = markov_chain_dict.get((text[i], text[i+1],), []).append([text[i+2]])

    if len(key_tuple) < n:
        del markov_chain_dict[key_tuple]

    return markov_chain_dict

def make_text(markov_chain_dict, n):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
#this works, trying with ngram now
    # key_tuple = random.choice(markov_chain_dict.keys())
    # random_output_text = key_tuple[0] + ' ' + key_tuple[1]
    # end_punctuation = ['.','!','?']

    # #while key_tuple in markov_chain_dict:
    # while random_output_text[-1] not in end_punctuation:
    #     next_in_chain = random.choice(markov_chain_dict[key_tuple])
    #     random_output_text = random_output_text + " " + next_in_chain
    #     key_tuple = (key_tuple[1], next_in_chain,)


    random_output_text = ""
    key_tuple = random.choice(markov_chain_dict.keys())
    key_list = list(key_tuple)
    for index in range(len(key_list)):
        random_output_text = random_output_text + " " + key_list[index]
    end_punctuation = ['.','!','?']

    while key_tuple in markov_chain_dict:
    # while random_output_text[-1] not in end_punctuation:
        if len(key_tuple) == n:
             next_in_chain = random.choice(markov_chain_dict[key_tuple])
             random_output_text = random_output_text + " " + next_in_chain

             fake_tuple = list(key_tuple)
             fake_tuple = fake_tuple[1:]
             fake_tuple.append(next_in_chain)
             key_tuple = tuple(fake_tuple)

    if end_punctuation[0] in random_output_text or end_punctuation[1] in random_output_text or end_punctuation[2] in random_output_text:
        twitter_output = ''
        for achar in random_output_text:
            if len(twitter_output) > 140:
                break
            elif achar not in end_punctuation:
                twitter_output += achar
            else:
                twitter_output +=achar
                break
    if twitter_output:
        return twitter_output
    else:
        return random_output_text[0:139]

def main():

    n = 3

    input_text = open(filename)

    chain_dict = make_chains(input_text,n)

    random_text = make_text(chain_dict,n)
    print random_text

if __name__ == "__main__":
    main()
