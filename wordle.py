w = open('fives.txt', 'r')

words = []
for number in range(5802):
    words.append(w.readline().strip('\n'))

while len(words) > 1:
    inputs = input('COMMANDS:\nGray(type "gray" followed by the letters)\nYellow(type "yellow" followed by the letter and where the letter is)\nGreen(type "green" followed by the letter and where the letter is)\nWords(prints the remaining words)\n')
    if inputs.lower()[0:4] == "gray":
        every_letter_gray = inputs.lower().replace(",", " ").split(" ")
        for value in every_letter_gray[1:]:
            if value == '':
                every_letter_gray.remove(value)
            elif len(value) > 1:
                print('Please separate each letter with either a comma, space, or both.')
        if len(every_letter_gray) == 1:
            print('Choose a letter.')
        else:
            gray_list = []
            for word in words:
                if all(letter not in word for letter in every_letter_gray[1:]):
                    gray_list.append(word)
            words = gray_list
            string_of_letters = ""
            for letter in every_letter_gray[1:]:
                if len(every_letter_gray[1:]) == 1:
                    string_of_letters = ' ' + letter
                else:
                    string_of_letters = string_of_letters + ' ' + letter
            print('Words with letter(s){a} have been removed.'.format(a=string_of_letters))
    elif inputs.lower() == "words":
        print(words)
        print("Words left to choose from: {a}".format(a=len(words)))
    elif inputs.lower() == "yellow":
        pass
    elif inputs.lower() == "green":
        pass
    else:
        print('{a} is not a command. Choose a command:'.format(a=inputs))

