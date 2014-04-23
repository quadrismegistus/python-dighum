### countfield.py
### This script will loop over a folder of text files
### and count the occurrence of each word in a given
### set of words, called a semantic field.
### The resulting coutns and the total count will be saved.
from textutils import *

## CONFIG: Please type in the words for the semantic world.
OPTION_MANUAL_ENTRY = True
OPTION_LOAD_FIELD_FROM_FILE = False


if OPTION_MANUAL_ENTRY:
    field = raw_input('Please type in the words for the semantic field: ')
    print "You typed:",field
    field = tokenize(field)
    print "I understood:",field

if OPTION_LOAD_FIELD_FROM_FILE:
    filename='fieldwords.txt'
    # load field from a file
    filetext = get_text(filename)
    field = tokenize(filetext)
    print "I understand:",field
#######


### Part 1:  Loop over a folder of text files and count words
folder='corpus'
import os,codecs

# Open output file
output_file = codecs.open('fieldcounts.txt',mode='w',encoding='utf-8')

# Write header of file
header = ['text', 'word', 'count', 'tf']
header_str = '\t'.join(header)
newline = '\n'

output_file.write(header_str + newline)

for filename in os.listdir(folder):
    fullpath = os.path.join(folder, filename)
    fulltext = get_text(fullpath) # filename to string
    words = tokenize(fulltext) # string to list
    counts = count_words(words) # list to dictionary

    numwords = float(len(words))
    totalcount = 0

    print fullpath
    for word in field:
        count=counts.get(word, 0)
        totalcount += count
        
        tf = count / numwords

        line_list = [filename, word, str(count), str(tf)]
        
        line_str = '\t'.join(line_list)
        output_file.write(line_str + newline)

    totaltf = totalcount / numwords
    line_list = [filename, 'SemanticField', str(totalcount), str(totaltf)]

    line_str = '\t'.join(line_list)

    output_file.write(line_str + newline)
    
