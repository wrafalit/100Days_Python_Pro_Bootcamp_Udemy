import pandas

nato_file = pandas.read_csv("nato_phonetic_alphabet.csv")



nato_dic = {row.letter:row.code for (index, row) in nato_file.iterrows()}
# print(nato_dic)


def generat():
    word = input("Enter a word: ").upper()
    word_list = list(word)
    try:
        phonetic_list = [nato_dic[ch] for ch in word_list]

    # print(word_list)
    except:
        print("Sorry, only letters in the alphabet please.")
        generat()
    else:
        print(phonetic_list)

generat()

# for ch in word_list:
#     print_list.append(nato_dic[ch])
# print(print_list)




