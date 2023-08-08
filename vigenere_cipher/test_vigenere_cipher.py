from unittest import TestCase
import vigenere_cipher


class TestVigenereCipher(TestCase):

    def test_should_identify_symbols(self):
        self.assertEqual(int(vigenere_cipher.identify_symbol('A')), 0)
        self.assertEqual(int(vigenere_cipher.identify_symbol('a')), 0)
        self.assertEqual(vigenere_cipher.identify_symbol('8'), '8')
        self.assertEqual(vigenere_cipher.identify_symbol(' '), ' ')
        self.assertNotEqual(vigenere_cipher.identify_symbol('x'), 'x')
        self.assertNotEqual(int(vigenere_cipher.identify_symbol('z')), 24)

    def test_identify_symbol_should_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            vigenere_cipher.identify_symbol('<') and self.assertTrue('unknown character!' in context.exception)

    def test_should_pass_decrypt_vigenere(self):
        ciphertext = "Llgji mvcsxwiil lyv vns yhb gjrvtmxcjmukmvc."
        key = "SECRETKEY"
        plaintext = "THESE CREATURES HAD TWO ODD CHARACTERISTICS."
        self.assertEqual(vigenere_cipher.decrypt_with_vigenere(ciphertext, key), plaintext)

    def test_should_fail_decrypt_vigenere(self):
        ciphertext = "Llgji mvcsxwiil lyv vns yhb gjrvtmxcjmukmvc."
        key = "SECRET"
        plaintext = "THESE CREATURES HAD TWO ODD CHARACTERISTICS."
        self.assertNotEqual(vigenere_cipher.decrypt_with_vigenere(ciphertext, key), plaintext)

