w = open('fives.txt', 'r')

words = []
for number in range(5802):
    words.append(w.readline().strip('\n'))

while len(words) > 0:
    inputs = input('COMMANDS:\n------------------------\nGray(type "gray" followed by the letters)\nYellow(type "yellow" followed by the letter and where the letter is)\nGreen(type "green" followed by the letter and where the letter is)\nWords(prints the remaining words)\nQuit to quit the finder\n------------------------\n')
    first_input = inputs.lower().split()[0]
    if first_input == "gray":
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
    elif first_input == "words":
        print(words)
        print("Words left to choose from: {a}".format(a=len(words)))
    elif first_input == "yellow": # yellow f 5, g 3
        letter_and_value = inputs.lower().split(',')
        checker = inputs.lower().split(' ')
        print(letter_and_value)
        if len(checker) == 1:
            print('Please input a letter followed by where the yellow letter is. If there are multiple, please use a comma.')
        else:
            letter_and_value = inputs.lower()[6:].split(',')
            temp = []
            for pair in letter_and_value:
                pair = pair.strip()
                temp.append(pair)
            letter_and_value = temp
            print(letter_and_value)
        for pair in letter_and_value:
            if not pair[0].isnumeric(): # if the first value in every pair is not a number:
                pass
            else:
                print('Improper use of command.')
    elif first_input == "green":
        pass
    elif first_input == "quit":
        print('\nProgram ended.')
        break
    elif first_input == "skibidi":
        print('\n\nskibidi fortnite\n-Isabella Alban\n')
    else:
        print('{a} is not a command. Choose a command:'.format(a=inputs))

