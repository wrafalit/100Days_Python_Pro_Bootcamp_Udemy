import CeasarCipher_art

def caesar(text_plain,shift_amount,direction_way):
    caesar = ''
    if direction_way == 'decode':
        shift_amount *= -1
    for ch in text_plain:
        if ch.isalpha():
            ind = alphabet.index(ch)
            caesar += alphabet[ind + shift_amount]
        else:
            caesar += ch
    print(f'The encoded text is: {caesar}')

print(CeasarCipher_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game_of = False
while not game_of:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25
    caesar(text, shift, direction)

    while True:
        game = input("Type 'yes' if you want to go again, otherwise type 'no'.\n")
        if game == 'yes':
            game_of = False
            break
        elif game == 'no':
            game_of = True
            break
        else:
            print('Type yes or no')

