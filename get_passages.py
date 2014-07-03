"""
get_passages.py
-- This file will loop through text files in a corpus folder,
-- find passages including any of a set of given words,
-- output all passges in a text file,
	one text file per text per word [eg. Burke.liberty.txt, Burke.virtue.txt, ..]
"""

FOLDER='corpus'
OUTPUT_FOLDER='passages'
WINDOW = 20
RANDOMIZE = True

from textutils import *
import os,codecs,random


## STEP 1: What are the words we are looking for?
words = raw_input("For which words would you like to find passages?")
words = tokenize(words,splitby=",")
print ">> SEARCHING FOR:",words




for filename in os.listdir(FOLDER):
	fullpath = os.path.join(FOLDER,filename)
	
	fulltext = get_text(fullpath)

	for substring in words:
		passages = get_passages(fulltext, substring, WINDOW)

		if RANDOMIZE: random.shuffle(passages)

		joinby=os.linesep + os.linesep

		output_text = joinby.join(passages)

		#output_filename = os.path.join(OUTPUT_FOLDER, filename.replace('.txt', substring+'.txt'))
		output_filename = os.path.join(OUTPUT_FOLDER, substring + '.' + filename)

		output_file = codecs.open(output_filename,mode='w',encoding='utf-8')

		output_file.write(output_text)

		output_file.close()

		print ">> saved:",output_filename




















