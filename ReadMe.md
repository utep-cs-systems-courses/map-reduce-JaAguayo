Jared Aguayo - Assignment 2 Parallel-Computing-MapReduce

A problem I encountered was using the string .split() instead of regex which led to my code not working properly so I fixed it by using a regex and a similar problem with .lower(). I also had a problem with initializing the dict outside of the parallel region as well as initializing it the wrong way so after fixing this it worked better.

The only problem left in the program is that it does not find the words that are names because the upper and lower cases do not match when checking for keys in the dict

It took me about 4-5 hours to complete but most time was spent debugging

To load files: 0.012sec
For 1 thread: 92.67sec
For 2 threads: 92.10sec
For 4 threads: 73.74sec
For 8 threads: 62.05sec

The program behaves this way since I am iterating a list of the files, when I give more threads it is able to work on more documents at a time to find words within, so when I give 8 threads it can search all the 8 files right away making the time the lowest.

cpuInfo.sh Program model name : AMD Ryzen 5 5600X 6-Core Processor 4 36 192

You run the program by having the files in the same directory that follow the "filename1.txt" format, the just run the program using "python3 parallelMapReduce.py"
