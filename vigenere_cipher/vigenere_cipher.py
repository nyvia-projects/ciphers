KEY = 'SECRETKEY'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SIZE = len(ALPHABET)


def read_ciphertext(input_file):
    with open(input_file) as file:
        return [ch for ch in file.read()]


CIPHERTEXT = read_ciphertext('ciphertext.txt')


def identify_symbol(ch):
    common = [' ', ',', '.']
    if ch in common or ch.isnumeric():
        return str(ch)
    elif ch.isalpha():
        return str(ALPHABET.index(ch.upper()))
    else:
        raise ValueError('unknown character!')


def identify_key_numeric_value(key):
    values = []
    for ch in key:
        values.append(int(identify_symbol(ch)))
    return values


def decrypt_with_vigenere(ciphertext, key):
    potential_plaintext = ""
    key_numeric = identify_key_numeric_value(key)
    for i in range(len(ciphertext)):
        try:
            current_symbol = identify_symbol(ciphertext[i])
            if current_symbol.isnumeric():
                potential_plaintext += ALPHABET[
                    (int(current_symbol) - key_numeric[i % len(key)]) % SIZE]
            else:
                potential_plaintext += current_symbol
        except ValueError as context:
            print(context)
            return -1
    return potential_plaintext


def write_plaintext(message):
    print("writing to 'plaintext.txt'..")
    with open('plaintext.txt', 'w') as output:
        output.write(message)


if __name__ == '__main__':
    write_plaintext(decrypt_with_vigenere(CIPHERTEXT, KEY))
