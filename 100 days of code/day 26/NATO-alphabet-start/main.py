import pandas

data = pandas.read_csv("100 days of code//day 26//NATO-alphabet-start//nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
is_on = True
while is_on:
    word = input("Enter a word: ").upper()

    try:
        nato_word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        is_on = False
        print(nato_word_list)
    
