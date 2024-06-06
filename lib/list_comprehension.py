#!/usr/bin/env python3

def return_evens(num_list):
    for n in num_list:
      if n % 2 == 0:
          print (n)
      else :
          print('null')

def make_exclamation(sentence_list):
    for words in sentence_list:
        print (f"{words}!")
    