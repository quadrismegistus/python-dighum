######### PART 1: Opening a file and pasting its contents into a variable 'text' #########

# make available the operating system functions
import os

# print a list of files in this directory
print os.listdir('.')

# assign one filename of a text to a variable 'filename'
filename='Burke.1790.Reflections on the Revolution of France.txt'

# [optionally] make sure file exists
print "Does the file exist?", os.path.exists(filename)

# make available functions to open unicode texts
import codecs

# create a variable 'file' which is a pointer to the real file
file=codecs.open(filename, encoding='utf-8')

# copy/paste the text of file into variable 'text'
text=file.read()



######### PART 2: "Tokenizing" the text into a list of words ################


# define an abstract function that tokenizes a big string of text into a list of words
def tokenize(x):
    # x is the big string coming into this function
    # First, let's .split() x into a list of all the smaller strings in between whitespace (like words)
    tokens=x.split()

    # But 'tokens' will have words like "REFLECTIONS" and "France," -- we want "reflections" and "france"
    # Let's make a new list where each word is the *refined* version of the word in original list
    refined_tokens=[refine_word(y) for y in tokens]

    # Return refined_tokens back out of this function (all functions generally need a return statement)
    return refined_tokens

# the above function 'tokenize' refers to a process 'refine_word', but we haven't defined that yet
# let's define that here:
def refine_word(x):
    # x is a word-like string, like "REFLECTIONS,"
    # First, let's make x lowercase
    x=x.lower()

    # Then, let's remove all non-alphanumeric characters from the end of x (like commas and periods)
    # While there are still letters in x ("while x", because if x has no letters, "while x" will stop looping)...
    # ... and while the last letter of x ("x[-1]") is not alphanumeric ...
    while x and not x[-1].isalnum():
        # make x equal to all the letters in x except the last one ("x[0:-1]")
        x=x[0:-1]

    # Now let's return x back out of this function
    return x

# APPLY the tokenize function to the string in text
# (before we do this, no tokenization has actually happened)
words=tokenize(text)




######### PART 3: Count the words in the list of words that we've created #########

# let's make a function that does this, and then later APPLY that function
# define a function 'count' that expects an incoming list 'l'
def count(l):
    # make an empty dictionary 'd'
    d={}

    # for each word (or 'token') in the list 'l'...
    for token in l:
        # if 'token' is not already in the dictionary 'd'...
        if not token in d:
            # then let's assign, under the entry 'token' in dictionary 'd', an initial value of 0
            d[token]=0

        # no matter what [we are no longer within the above 'if' clause], add 1 to the entry 'token' in dictionary 'd'
        d[token]+=1

    # return the dictionary which now has all the words as "entries", and the count for each word as that entry's "definition"
    return d


# now let's APPLY our count function to our list of words
wordcounts=count(words)




######### PART 4: Let's write out to a file the wordcount dictionary we just made #########

# first, let's open a new unicode (utf-8) file for writing ('w') with a filename 'wordcounts.txt'
ofile=codecs.open('wordcounts.txt', 'w', encoding='utf-8')

# one way to loop over a dictionary is to call .items() on that dictionary
# .items() will give back a list, each item of which is a tiny list with two things: (the word, and its count)
# so .items() might give back [ ('reflections',100), ('france',50), ... ]

# so we can loop over that list of (word,count)s like this:
# read: for every word and its count in the dictionary wordcounts's items
for word,count in wordcounts.items():
    # make a string which will be a line in our output file
    # the string will be:
    #   the word +
    #   a tab character (u'\t') +
    #   the count, but made into a string first, because we can't add a pure number to a string
    #   then a new-line character (u'\n' for Mac) (u'\r\n' for Windows)
    line=word + u'\t' + str(count) + u'\n'

    # write this line to the file
    ofile.write(line)


## DONE! Check out your file 'wordcounts.txt' to see the results!