#!/usr/bin/python

from itertools import groupby
from operator import itemgetter
import sys

output=[]
def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def sort(input_list):
    temp_list=input_list
    length=len(input_list)
    output=[]
    for i in range(length):
        output.append(temp_list.pop(temp_list.index(max(temp_list))))

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    final_list=[]
    for current_word, group in groupby(data, itemgetter(0)):
        anagram_list = list(set(anagram for current_word, anagram in group))
        if anagram_length > 2:
            final_list.append(anagram_list)
    sort(final_list)
    for item in output:
        print "%s\t%s" % (len(item), item)


if __name__ == "__main__":
    main()
