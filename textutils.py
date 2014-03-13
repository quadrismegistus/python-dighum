def get_text(filename):
    # This takes a filename as a string,
    # and returns a large string with the contents of the text

    import os,codecs

    if not os.path.exists(filename):
        print "!! File not found!",filename
    else:
        file=codecs.open(filename,encoding='utf-8')
        text=file.read()
        return text

def refine_token(token):
    # token is a word-like string that may include punctuation,
    # and may have weird capitalizations.
    # we want to return a lower-cased, no-punctuation version.

    # Lowercase
    token=token.lower()

    # Remove non-alphanumeric characters from end
    while token and not token[-1].isalnum():
        token=token[0:-1]

    # Remove non alpha-numeric cahracters from beginning
    while token and not token[0].isalnum():
        token=token[1:]

    return token
    

def tokenize(text):
    # This takes a big string, text,
    # and returns a list of words

    tokens=text.split() # 'giant,'
    words=[]
    for token in tokens:
        word=refine_token(token)
        if not word: continue
        words.append(word)

    return words


def count_words(words):
    # This function takes in a list of words
    # and gives back a dictionary,
    # with each word as its key
    # and that word's count as its value

    d={} # 'reflections' => 10

    for word in words:
        if not word in d:
            d[word]=1
        else:
            d[word]+=1

    return d


def write_counts(filename, counts):
    import codecs
    ofile=codecs.open(filename,'w',encoding='utf-8')

    for word,count in sorted(counts.items(), key=lambda tinylist: -tinylist[1]):
        line=word + u'\t' + str(count) + u'\n'
        ofile.write(line)

    ofile.close()
    print ">> saved:",filename
