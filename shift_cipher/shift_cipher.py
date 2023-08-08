# reads and returns alphabet file data as list
def read_alphabet(input_file):
    with open(input_file) as file:
        return [ch for ch in file.read() if ch != '\n']


# reads and returns ciphertext file data as list
def read_ciphertext(input_file):
    with open(input_file) as file:
        return [ch for ch in file.read()]


ALPHABET = read_alphabet('input.txt')
SIZE = len(ALPHABET)
CIPHERTEXT = read_ciphertext('ciphertext.txt')


# identifies symbol in ALPHABET or raises ValueError
# returns index
def identify_character(ch):
    if ch in ALPHABET:
        return ALPHABET.index(ch)
    else:
        raise ValueError("unknown character!")


# algorithm for decrypting shift
# returns potential plaintexts
def decrypt_with_shift(ciphertext, key):
    potential_plaintext = ""
    for ch in ciphertext:
        try:
            potential_plaintext += ALPHABET[(identify_character(ch) - key) % SIZE]
        except ValueError:
            print()
    return potential_plaintext


# automates calls to decrypt function
# returns dictionary of results with keys
def brute_force(func, ciphertext, keys):
    results = {}
    for key in keys:
        results[key] = func(ciphertext, key)
    return results


# handles key input
# returns chosen~correct key
def take_key_input():
    while True:
        try:
            key = int(input("cipher key: "))
            if -1 < key > SIZE:
                raise ValueError
            break
        except ValueError:
            print("invalid integer input!")
    return key


# shows brute-force results
# lets you select the correct message and returns
def show_results_and_return_message():
    results = brute_force(decrypt_with_shift, CIPHERTEXT, list(range(0, SIZE)))
    for key in results:
        print(f"key {key} : {results.get(key)}")
    found_key = take_key_input()
    found_message = results.get(found_key)
    print(f"message found:\n{found_message}")
    print("returning..")
    return {found_key: found_message}


# writes message to file
def write_plaintext(message):
    print("writing to 'plaintext.txt'..")
    with open('plaintext.txt', 'w') as output:
        output.write(f"key: message\n{str(message)}")


if __name__ == '__main__':
    write_plaintext(show_results_and_return_message())
