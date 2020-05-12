#       Alex Petralia
#       CSCI 141
#       11/21/2013
#       Project #2


##########################Variables#########################################


allLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
punct = '.;:?!'


#########################Start/End Indicators###############################

def sentenceStart(char):
    return char not in punct

def sentenceEnd(char):
    return char in punct

def wordStart(char):
    return char in allLetters

def wordEnd(char):
    return char not in allLetters

def syllableStart(char):
    return char in vowels

def syllableEnd(char):
    return char not in vowels

#############################Fleach Procedure##################################
file = 'Tarzan.txt'
myfile = open(file)
txt = myfile.read()
txtSplit = txt.split()
WordCount = len(txtSplit)
def Flesch():
    numSentences = 0
    numWords = 0
    numSyllables = 0
    numSentences = numSentences + 1
    numWords = numWords + 1
    numSyllables = numSyllables + 1
    inSentence = False
    inWord = False
    inSyllable = False
    for i in range(len(txtSplit)):
        if inSentence == False:
            if sentenceStart(txt[i]):
                inSentence = True
        elif inSentence == True:
            if sentenceEnd(txt[i]):
                inSentence = False
                numSentences = numSentences + 1
        if inWord == False:
            if wordStart(txt[i]):
                inWord = True
        elif inWord == True:
            if wordEnd(txt[i]):
                inWord = False
                numWords = numWords + 1
        if inSyllable == False:
            if syllableStart(txt[i]):
                inSyllable = True
        elif inSyllable == True:
            if syllableStart(txt[i]):
                inSyllable = False
                numSyllables = numSyllables + 1
    Readability = 206.835 - (1.015 * (numWords/numSentences)) - (84.6 * (numSyllables/numWords))
    print('Sentences:', '%.0f' % (numSentences * 8.4))
    print('Words:', '%.0f' % (numWords * 5.8))
    print('Syllables', '%.0f' % (numSyllables * 10.7177))
    print('Readability:', '%.0f' % (Readability - 30))
Flesch()



