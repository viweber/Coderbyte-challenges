def LongestWord(sen):  
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    words = ""

    for index in sen:
        if index in letters:
            words = words+index
        else:
            words = words+' '


    wordsArr = words.strip().split(" ")

    for index in wordsArr:
        if index == '':
            wordsArr.remove(index)

    bigWordSize = 0
    bigWordLocate = ''
    for index in wordsArr:
        if len(index) > bigWordSize:
            bigWordSize = len(index)
            bigWordLocate = index

    print("A maior palavra é:", bigWordLocate)

LongestWord(input())
 