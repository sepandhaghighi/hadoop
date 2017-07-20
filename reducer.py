#!/usr/bin/python

from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    '''
    This function read mapper output
    :param file: input file
    :type file : sys.stdin
    :param separator: seperator string
    :type separator:str
    :return: yeild in each iteration
    '''
    for line in file:
        yield line.rstrip().split(separator, 1)

def sort(input_list):
    '''
    This function sort input list
    :param input_list: input list
    :type input_list:list
    :return: sorted list as list
    '''
    temp_list=input_list
    length=len(input_list)
    output=[]
    length_list=list(map(len,input_list))
    for i in range(length):
        max_item=max(length_list)
        max_index=length_list.index(max_item)
        length_list.remove(max_item)
        output.append(temp_list.pop(max_index))
    return output

def main(separator='\t'):
    '''
    This function first read mapper output from terminal output (sys.stdin) and pass it to read_mapper to pretify it
    after that append each word with same sorted face to a seperated list and append each seperated list to lager final list
    in final step call sort function to sort larg list and print each item of this list
    :param separator: seperator between sorted word and first word
    :type separator: str
    :return: None
    '''
    data = read_mapper_output(sys.stdin, separator=separator)
    final_list=[]
    for current_word, group in groupby(data, itemgetter(0)):
        anagram_list = list(set(anagram for current_word, anagram in group))
        anagram_length=len(anagram_list)
        if anagram_length>1:
            final_list.append(anagram_list)
    sorted_list=sort(final_list)
    for item in sorted_list:
        print "%s\t%s" % (len(item), item)


if __name__ == "__main__":
    main()
