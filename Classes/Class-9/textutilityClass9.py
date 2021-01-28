def charCount(paragraph):
    '''This function accepts a text string and returns an integer count of number of charecters in it'''
    char_count = len(paragraph)
    return char_count

def word_count(paragraph):
    ''' This function accepts a text string and returns an integer 
    count of number of words in it '''
    word_count = len(paragraph.split(" "))
    return word_count