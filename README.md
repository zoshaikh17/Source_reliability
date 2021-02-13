# Source_reliability

Taking sum of all ranks from various sources for each web page, and using the summation to generate the
combined rank. We have implemented Merge Sort, Quick Sort and Insertion Sort on the combined rank. As
a result, we have obtained the sorted list and the inversion count. We have also performed the quality on
the list and obtained the normalisation value by passing the weights to the sorted list. Furthermore, we have
performed iteration on the list to obtained the correct values for the ranking functions of different search engine
that is sorted list in order to obtain conclusion which is the most efficient algorithms among all of the three
one.

## Problem Statement
Modern web-based search engines use ranking functions to prioritize the order of documents shown to a user
after a search. One way to rank different search results is to compile a list of results from different search
engines, compare them, and compute results based on a weighted sum of rankings from each source. Of course,
in order to calculate a weighted sum, it is necessary to compute weights for each source using gathered data.
Once we have a set of rankings from each source of the same web pages, we need to develop a way to measure the
difference in quality between the sources. As there is no objective source for the best rankings, it is necessary
to judge each source against all other sources and iteratively calculate a quality score to be used as a weight
for the ranking function.
