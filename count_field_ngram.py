# This program will loop over a folder of text files
# and count the occurrence of each word in a given set of words
# store resulting counts for each word and total count in output file

from textutils import *
import codecs

# CONFIG: type in the words for the semantic field here

# This is called a flag
OPTION_MANUAL_ENTRY = True  
OPTION_LOAD_FIELD_FROM_FILE = False

if OPTION_MANUAL_ENTRY:
    field = raw_input("Enter your field here: ")

if OPTION_LOAD_FIELD_FROM_FILE:
    # load the field from a file using get_text
    filename = 'fieldwords.txt'
    field = get_text(filename)

field = tokenize(field,splitby=",")
    
print "I understood: ", field

# Loop over folder of text files and count words
folder = "test_corpus"
import os

# Create and open output file
output_file = codecs.open("fieldcounts.txt", mode='w', encoding="utf-8")

# Write header of file
# header='text\tword\tcount\ttf'
header = ['text', 'word', 'count', 'tf']
header_string = '\t'.join(header)
newline = '\n'

output_file.write(header_string + newline) # always want to write a newline char to each output line


# os.listdir gives us a list of all filenames in a director
for filename in os.listdir(folder):
    fullpath = os.path.join(folder, filename) # we need this in order to give python the exact address of the file we want
    # since we stored our text files in a separate folder, we need to direct python to that folder first
    fulltext= get_text(fullpath) # goes from filename to string
    words = tokenize(fulltext) # goes from string to list of cleaned words
    numwords = float(len(words))
    print fullpath

    total_field_counts = 0
    
    for ngram in field:
        count = count_substring(fulltext, ngram)
        tf = (count/numwords) * 1000
        line = [filename, ngram, str(count), str(tf)] # this defines what we want in each line as part of a list
        line = '\t'.join(line) # this makes the line list into a string, bc we can't print anything but a string
        output_file.write(line + newline) # this is all you need to do to write to a file!
        # now add the count to the total counts of all words in our field
        total_field_counts += count

    totaltf = total_field_counts/numwords * 1000
    line_list = [filename, "SemanticField", str(total_field_counts), str(totaltf)]
    line = '\t'.join(line_list)
    output_file.write(line + newline)
