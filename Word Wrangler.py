"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) == 0:
        return list1
    if len(list1) == 1:
        return [list1[0]]
    elif list1[len(list1)/2 -1] == list1[len(list1)/2]:
        return remove_duplicates(list1[:len(list1)/2]) + remove_duplicates(list1[len(list1)/2 + 1:])
    else:
        return remove_duplicates(list1[:len(list1)/2]) + remove_duplicates(list1[len(list1)/2:])

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if len(list1) == 0 or len(list2) == 0:
        return []
    index1 = 0
    index2 = 0
    intersect_list = []
    while index1 < len(list1) and index2 < len(list2):  
        if list1[index1] == list2[index2]:  
            intersect_list.append(list1[index1])  
            index1 += 1;  
            index2 += 1;  
        elif list1[index1]<list2[index2]:  
            index1 += 1  
        else:  
            index2 += 1  
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    merged_list = list2
    index_add = 0
    for (index1, item1) in enumerate(list1):        
        for index2 in range(index_add, len(list2)):
            if index2 == len(list2) - 1 and item1 >= list2[index2]:
                merged_list = merged_list + [item1]
            if item1 < list2[index2]:
                merged_list = merged_list[:(index2+index1)] + [item1] + merged_list[(index2+index1):]
                index_add = index2
                break
    return merged_list

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) < 2:
        return list1
    if len(list1) == 2:
        return merge([list1[0]], [list1[1]])
    else:
        return merge(merge_sort(list1[:len(list1)/2]), merge_sort(list1[len(list1)/2:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    if len(word) == 1:
        return ["", word]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        new_strings = []
        for string in rest_strings:
            for index_s in range(len(string) + 1):
                new_strings.append(str(string[:index_s]) + first + str(string[index_s:])) 
    return new_strings + rest_strings

# Function to load words from a file

def load_words(filename):  
    """ 
    Load word list from the file named filename. 
 
    Returns a list of strings. 
    """  
    res = []  
    url = codeskulptor.file2url(filename)  
    netfile = urllib2.urlopen(url)  
    for line in netfile.readlines():  
        res.append(line[:-1])  
    return res  


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()