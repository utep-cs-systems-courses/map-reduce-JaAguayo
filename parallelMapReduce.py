#!/usr/bin/env python3
import time
import pymp
import os
import re

#you can change the filename beginning to fit format, fileName1.txt
FILE = "shakespeare"

def readFiles():
    docs = []
    #counts all the files in the dir with .txt
    number_of_files = sum(f.endswith('.txt') for f in os.listdir("."))
    for i in range(number_of_files):
        #loads all the files from shakespeare1-8.txt into strings in a list docs
        file = (FILE + "%d" + ".txt") %(i+1)
        with open(file) as f:
            full_doc = f.read()
            docs.append(full_doc)
    return docs


def map(files):
    words = ['hate', 'love', 'death', 'night', 'sleep', 'time', 'henry', 'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart', 'honest']
    #gets the list of files in strings
    docs = files
    #shared dict
    words_dict = pymp.shared.dict()

    with pymp.Parallel() as p:
        doc_lock = p.lock
        #initialize the dict
        for word in words:
            words_dict[word] = 0
        #iterates over the list of docs
        for doc in p.iterate(docs):
            #regex to split the words in the string, sp_word = split word
            for spl_word in re.split(r"[-;,.\s]\s*", doc):
                if spl_word in words_dict:
                    count = words_dict[spl_word]
                    #aquire lock
                    doc_lock.acquire()
                    #add to the number in the dict at that key (word)
                    words_dict[spl_word] = count + 1
                    #release lock
                    doc_lock.release()

    return words_dict

def main():
    #gets time that it takes to load the files into strings
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    docs = readFiles()
    elasped_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-start_time
    format_time = '{:.10f}'.format(elasped_time)
    print("Loaded File Time:",format_time)

    #runs the parallel area and times how long to find the words
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    word_count = map(docs)
    elasped_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-start_time
    format_time = '{:.10f}'.format(elasped_time)
    print("Time to find the words in document:",format_time)


    print(word_count)

if __name__ == '__main__':
    main()
