#!/usr/bin/env python3
import time
import pymp
import os
"""
-need to use a lock for global dict
-use a dict to count how many times the words appear
-hate, love, death, night, sleep, time, henry, hamlet,
you, my, blood, poison, macbeth, king, heart, honest 

words_dict = {"hate":0,"love":0,"death":0,"night":0,"sleep":0,"time":0,
"henry":0,"hamlet":0,"you":0,"my":0,"blood":0,"poison":0,"macbeth":0,
"king":0,"heart":0,"honest":0}
"""

def readFiles():
    docs = []
    number_of_files = sum(f.endswith('.txt') for f in os.listdir("."))
    for i in range(number_of_files):
        file = ("shakespeare" + "%d" + ".txt") %(i+1)
        with open(file) as f:
            full_doc = f.read()
            docs.append(full_doc)
    return docs


def map():
    docs = readFiles()

    words_dict = pymp.shared.dict()
    words_dict = {"hate":0,"love":0,"death":0,"night":0,"sleep":0,"time":0,
    "henry":0,"hamlet":0,"you":0,"my":0,"blood":0,"poison":0,"macbeth":0,
    "king":0,"heart":0,"honest":0}

    with pymp.Parallel() as p:
        words = []
        doc_lock = p.lock

        for doc in p.iterate(docs):
            for word in doc.split():
                #print(word)
                #for word in line.split():
                if str(word).lower() in words_dict:
                    count = words_dict[word]
                    doc_lock.acquire()
                    words_dict[word] = count + 1
                    print(word)
                    doc_lock.release()
                    
    return words_dict

def main():
    word_count = map()
    print(word_count)

if __name__ == '__main__':
    main()
