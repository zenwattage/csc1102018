# working_with_strings_solution.py
# ## Here are some possible solutions for the "Working with Strings"
# # lab exercise.  Multiple versions are provided for some parts,
# # and the optional parts are included too.
# ## CSC 110
# # W'18
def main():
    # Part 0: Get the phrase from the user
    phrase = input('Enter a phrase: ')
    # Part 1: Print the phrase one character per line
    for ch in phrase:
        print(ch)
    print()# insert a blank line
    # Part 1b: Print the phrase one character per line
    #          Alternate version: using an indexed loop
    for i in range(len(phrase)):
        print(phrase[i])
        print()  # insert a blank line
        # Part 2: Print the phrase in reverse order, all on one line
        # #         using a slice.
        print(phrase[::-1])  # default start, default end, -1 step
        # Part 3: Print the phrase in reverse order, all on one line
        # #         Version 1 -- printing each character separately.
        reverse_phrase = '' # initialize to the empty string
        for i in range(len(phrase)-1, -1, -1):
            print(phrase[i], end='') # notice the use of the 'end' parameterprint()  
            # go to the next line
            # # Part 3: Print the phrase in reverse order, all on one line
            # #         Version 2 -- reverse iteration using a 'while' loop
            # #         and a string accumulator
            reverse_phrase = '' # initialize accumulator to the empty string
            i = len(phrase) - 1 # initialize index
            while i >= 0:reverse_phrase += phrase[i] # add character at the end
            i -= 1 # update loop 
            counterprint(reverse_phrase)
            # Part 3: Print the phrase in reverse order, all on one line
            # #         Version 3 -- using a string accumulator.
            reverse_phrase = '' # initialize to the empty string
            for ch in phrase:reverse_phrase = ch + reverse_phrase # add ch in FRONT
            print(reverse_phrase)
            # Part 4: Print one word per line
            print()   # insert a blank line
            word = '' # initialize to the empty string
            for ch in phrase:
                if ch == ' ':   # when you see a space, print the word and reset
                    print(word)
                    word = ''
            else:           # otherwise add the character to the word
                word += ch
                if word != '':      # print the last word
                    print(word)# Optional Part 5: Print each word in a file, one per line, no vowels
            #                  Version 1 -- reading the file one line at a time
            file_name = input('\nEnter the name of a text file: ')
            infile = open(file_name, 'r')  # open the file
            line = infile.readline()       # read one line from the file
            while line != '':
                for ch in line:
                    if ch not in 'AEIOUaeiou ':  # don't print vowels or spaces
                        print(ch, end='')
                    if ch == ' ':   # go to a new line for each space
                        print()
                    line = infile.readline()   # UPDATE read -- get the next line
                    infile.close()                 # close file
                    print()  # go to the next line
                    # Optional Part 5: Print each word in a file, one per line, no vowels
                    # #                  Version 2 -- reading all file contents into one string
                    # #                  Notice the use of the 'isspace' function from Ch 9
                    file_name = input('\nEnter the name of a text file: ')
                    infile = open(file_name, 'r')  # open the file
                    data = infile.read()           # read all data from the file
                    infile.close()                 # close file
                    for ch in data:
                        if ch not in 'AEIOUaeiou \t\n':  # don't print vowels or whitespace
                            print(ch, end='')
                    if ch.isspace():   # go to a new line for each whitespace character
                        print()
                        print()  # go to the next line
                    # Optional Part 6: Replace 'b' words with 'bee'
                        print()  # insert a blank line
                        word = '' # initialize to the empty string
                        phrase += ' ' # add a space at the end of the phrase
                    # to ensure the last word gets flushed out
                    for ch in phrase:
                        if ch == ' ':   # when you see a space, print the word and reset
                            if len(word) > 0:
                                if word[0] == 'b' or word[0] == 'B':
                                    print('bee', end=' ')
            else:
                print(word, end=' ') # notice -- spaces between words
                word = ''
        else:           # otherwise add the character to the word
            word += ch
            print()

main()
