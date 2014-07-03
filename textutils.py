def get_text(filename):
    # This takes a filename
    # and returns a large string with the contents of the text

    import os,codecs
    
    if not os.path.exists(filename):
        print "!! File not found!",filename
    else:
        try:
            file=codecs.open(filename,encoding='utf-8')
            text=file.read()
        except UnicodeDecodeError:
            file=open(filename)
            text=file.read()

        return text
        
def refine_token(token):
    # token is a word-like string that may include punctuation, 
    # and may have weird capitalization
    # we want to return a lower-case, no-punctuation version.
    
    # Lowercase
    token=token.lower()
    
    # Remove non-alphanumeric characters from end
    while token and not token[-1].isalnum():
        token=token[0:-1]
    
    # Remove non alpha-numeric characters from beginning
    while token and not token[0].isalnum():
        token=token[1:]
    
    return token
                
def tokenize(text, splitby=None):
    # This takes a big string, text
    # and returns a list of words
    #splitby is an optional argument; now default set to white space
    #if you want to change how text is being split, change splitby in function
    
    tokens=text.split(splitby) # 'giant,'
    words=[]
    for token in tokens: 
        word=refine_token(token)
        if not word: continue
        words.append(word)
        
    return words


def get_passages(text, substring, window=50):
    horizon = int(window / 2)

    textl = text.lower()
    subl = substring.lower()

    index = textl.find(subl)

    passages = []

    while index > -1:
        pre=text[:index]
        post=text[index + len(substring):]

        left_letter = pre[-1]
        right_letter = post[0]

        if not left_letter.isalpha() and not right_letter.isalpha():
            pre_words = pre.split()
            post_words = post.split()

            pre_window = pre_words[-horizon:]
            post_window = post_words[:horizon]

            pre_window_str = ' '.join(pre_window)
            post_window_str = ' '.join(post_window)

            passage = pre_window_str + ' >>>' + substring + '<<< ' + post_window_str

            passages.append(passage)

        index = textl.find(subl,index+1)

    return passages


    
def count_substring(text, substring):
    textl = text.lower()
    index = text.find(substring)
    count = 0
    while index > -1:
        instance=text[index : index + len(substring)]
        left_letter = text[index-1] if index>0 else ""
        right_letter = text[index + len(substring)]
        right_letter = text[right_letter_index] if right_letter_index < len (text) else "" 
        
        if not left_letter.isalnum() and not right_letter.isalnum():
            count += 1
            
        index = textl.find(substring, index + 1)
        
    return count
        
    
def count_words(words):
    # This function takes in a list of words
    # and gives back a dictionary,
    # with each word as its key
    # and that word's count as its value
    
    d={}
    
    for word in words: 
        if not word in d:
            d[word]=1
        else: 
            d[word]+=1
            
    return d
    
def write_counts(filename,counts):
    import codecs
    file=codecs.open(filename,'w',encoding='utf-8') 
    
    for word,count in sorted(counts.items(), key=lambda tinylist: -tinylist[1]):
        print word, count
        
        line=word + u'\t' + str(count) + u'\n'
        file.write(line)
        
    file.close()
    print ">> saved:",filename
