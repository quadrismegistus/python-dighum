filename='Burke.1790.Reflections on the Revolution of France.txt'

from textutils import *

text=get_text(filename)

words=tokenize(text)

wordcounts=count_words(words)

write_counts('countsBurke.txt', wordcounts)
