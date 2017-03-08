def getAvailableLetters(lettersGuessed):
    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in lettersGuessed:
        if char in alf:
            alf.remove(char)
    output = ''
    for al in alf:
        output += al
    return output
