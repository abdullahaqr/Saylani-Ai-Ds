def space_count(text):
    '''This function accepts text/paragraph/string and returns number of spaces'''
    count = 0
    for letter in text:
        if letter == " ":
            count += 1
    return 'Number of Spaces : ' + str(count)

#######################################################################

def remove_double_space(text):
    '''This function accepts text/paragraph/string 
    and returns string with all double or multiple spaces removed '''

    return ( ' '.join(text.split()) )

#######################################################################

def punctuation_count(text):
    '''This function accepts text/paragraph/string 
    and returns number of punctuations '''
    count = 0
    for i in range (len(text)): 
        if text[i] in ('!', ",", "\'", ";", "/", ".", "-", "?", ":"):
            count += 1
    return "Number of punctuations : " + str(count)

#######################################################################

def remove_punctuation(text):
    '''This function accepts text/paragraph/string 
    and returns string with all punctuations removed '''
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punctuation = ""
    
    for char in text:
        if char not in punctuations:
            no_punctuation = no_punctuation + char

    return no_punctuation

#######################################################################