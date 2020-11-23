def snowman_edit (a):
    a = a.replace(',' , '')
    a = a.replace('.' , '')
    a = a.replace('-' , '')
    a = a.replace('\n' , '')
    a = a.replace('\'' , '')
    a = a.replace('\"' , '')
    a = a.lower()
    a = a.split( )
    snowman = a
    return snowman

def word_counter(w6_snow_white) :
    f = open(w6_snow_white,'r')
    snowman = f.read()
    f.close()
    
    snowman = snowman_edit(snowman)
    
    for word in snowman :
        if word in wordcount.keys():
            wordcount[word] += 1 
        else:
            wordcount[word] = 1

    return print(wordcount)
wordcount = {}
word_counter('w6_snow_white.txt')

#result = list(wordcount.items())
'''for tuple in result :
    result = tuple
    print(result)'''
