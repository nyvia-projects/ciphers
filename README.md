# Caesar and Vigenere Cipher Decryptors

## Ceaser (Shift) Cipher

Implements brute force approach to shift cipher, where user gets to select the correct plaintext from the output.

To use it, make sure to have the following in the directory

- ciphertext in _ciphertext.txt_
- your alphabet in _input.txt_

After running the script select the correct plaintext, which will add it to _plaintext.txt_.

Run **_test_shift_cipher.py_** to make sure algorithm works for your inputs.

## Vigenere Cipher

Deciphers vigenere ciphertext to plaintext.

To use it,

- have your ciphertext in _ciphertext.txt_ within the directory of the script
- set **ALPHABET** and **KEY** values in **_vigenere_cipher.py_**

After running the script it will output plaintext to _plaintext.txt_.

Run **_test_vigenere_cipher.py_** to make sure algorithm works for your inputs.

### Comments and possible improvements

You could easily implement encryption for both ciphers by inversing decryption functions.

For Ceaser cipher you could use a library or AI to automatically select a the plaintext for you from the provided potential options.

You also can use other language letters as an alphabet for your ciphertext.
