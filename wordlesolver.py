w = open('fives.txt', 'r')

def removewords(word):
    words = w.readlines()
    while len(words) > 1:
        input('COMMANDS:\nGray(type "gray" followed by the letters)\nYellow(type "yellow" followed by the letter and where the letter is)\nGreen(type "green" followed by the letter and where the letter is)\n')
        
removewords(1)