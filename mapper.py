#!/usr/bin/python

import sys
import re
def read_input(input_file):
    '''
    This function read input file line by line change it to lowercase and split words of this line and yield
    (return in each iteration) as list
    :param file: input file
    :type file : file object
    :return: yield in each iteration
    '''
    for line in input_file:
        line = re.split('[^a-z]+', line.lower())
        yield line
def main(separator='\t'):
    '''
    This function get input file from sys.stdin (argument passing in terminal) and pass this file to read_input function
    in each output of read_input function check list items if char number of each word larger than 0 (word validation)
    sort letter of word and print sorted word and first word with a separator(default value ="\t") to terminal
    :param separator: separator for sorted word and first word
    :type separator:str
    :return: None
    '''
    for words in read_input(sys.stdin):
        for word in words:
            if len(word) > 0:
                print '%s%s%s' % (''.join(sorted(word)), separator, word)
if __name__ == "__main__":
    main()
