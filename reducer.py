from itertools import groupby
from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    min_length=0
    final_list=[]
    for current_word, group in groupby(data, itemgetter(0)):
        anagram_list = list(set(anagram for current_word, anagram in group))
        anagram_length=len(anagram_list)
        if anagram_length > 2 and anagram_length>min_length :
            final_list.append(anagram_list)
            min_length=anagram_length
    for item in final_list:
        print "%s\t%s" % (len(item), item)


if __name__ == "__main__":
    main()
