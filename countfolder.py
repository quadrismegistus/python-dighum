# Set the name of the folder
folder='corpus'

# Make available operating system functions
import os,codecs

# Make available OUR text utility functions
from textutils import *

# Get the list of files in our folder
# -- it's a list of strings, one for each filename
files=os.listdir(folder)
print files

dd={}
for filename in files:
    # make a filename with the folder and a / in front
    filename_full=os.path.join(folder, filename)

    # Print the filename so we know what file we're working with
    print filename_full

    # From filename to big string of text
    text=get_text(filename_full)

    # From big string of text to list of words
    words=tokenize(text)

    # From list of words to a dictionary of word => count
    wordcounts=count_words(words)

    # Write a file of counts for this text
    count_filename="counts_"+filename
    write_counts(count_filename, wordcounts)

    # Set the entry for filename in the dd to be the wordcount dictionary
    dd[filename]=wordcounts


def save_count_dd(dd,ofn='counts_dd.txt'):
    # Assumes dd is of the structure
    # filename => { word: count, word: count }

    ## Get all unique words
    # Make an empty set called words
    words=set()
    for filename,wordcounts in dd.items():
        # Filename is "burke.txt" eg
        # wordcounts is Burke's wordcount dictionary: {'france':10...}

        # make a list of the words in Burke's dictionary
        filename_words = wordcounts.keys()

        # make this list a set
        filename_words_set = set(filename_words)

        # make words be the union of what was already in words,
        # and Burke's words
        words |= filename_words_set

    words=list(words)
    words.sort()

    ## Open file to write to
    ofile=codecs.open(ofn,'w',encoding='utf-8')

    ## Write header line
    ofile.write('filename')
    for word in words:
        ofile.write('\t'+word)
    ofile.write('\n')

    ## Write a line for each filename in the dd
    for filename,wordcounts in dd.items():
        ofile.write(filename)
        for word in words:
            count=wordcounts.get(word,0)
            ofile.write('\t'+str(count))
        ofile.write('\n')
    

    
        
    

save_count_dd(dd)
