import unittest
import shift_cipher


class TestShiftCipher(unittest.TestCase):

    # def test_read_alphabet(self):
    #     under_test = shift_cipher.read_alphabet('input.txt')
    #     self.assertEqual(under_test, list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?,."))
    #
    # def test_read_ciphertext(self):
    #     under_test = shift_cipher.read_ciphertext('ciphertext.txt')
    #     self.assertEqual(under_test, list(
    #         "wslhzlCzlukC2zCz2wwsplzCx2pjrs6ChzCwvzzpislGCdlChylCsvjh1lkCpuC1olC4lz1CvmCwhjpmpjCvjlhuGCV2yClult6C4pssChyyp3lCpuC89C1vC8!Cov2yzG"))
    #
    # def test_fail_read_alphabet(self):
    #     under_test = shift_cipher.read_alphabet('input.txt')
    #     self.assertNotEqual(under_test, list("abcdefghijklmnopqrstuvwxyz1234567890"))
    #
    # def test_fail_read_ciphertext(self):
    #     under_test = shift_cipher.read_ciphertext('ciphertext.txt')
    #     self.assertNotEqual(under_test, list("wslhzlCzlukC2zCz2wwsplzCx2pjrs"))

    def test_should_identify_character_in_alphabet(self):
        under_test = shift_cipher.identify_character('A')
        self.assertIs(under_test, 0)
        under_test = shift_cipher.identify_character(' ')
        self.assertIs(under_test, 62)

    def test_should_fail_identifying_character(self):
        under_test = shift_cipher.identify_character('?')
        self.assertIsNot(under_test, 1)

    def test_should_fail_with_exception(self):
        with self.assertRaises(ValueError) as context:
            shift_cipher.identify_character('<')
            self.assertTrue('unknown character!' in context.exception)

    def test_should_decrypt_shift_cipher(self):
        plaintext = "please send us supplies"
        ciphertext = "wslhzlCzlukC2zCz2wwsplz"
        key = 7
        self.assertEqual(shift_cipher.decrypt_with_shift(ciphertext, key), plaintext)

    def test_should_fail_decrypting(self):
        plaintext = "please send us"
        ciphertext = "wslhzlCzluk"
        key = 2
        self.assertNotEqual(shift_cipher.decrypt_with_shift(ciphertext, key), plaintext)

    def test_fail_because_of_handled_exception(self):
        key = 11
        ciphertext = 'a<qwerty'
        plaintext = "something"
        self.assertIsNot(shift_cipher.decrypt_with_shift(ciphertext, key), plaintext)

    def test_should_pass_brute_force(self):
        def random_func(some_text, key=0):
            return some_text

        text = "random-text"
        keys = list(range(1, 4))
        expected_message = {keys[0]: text, keys[1]: text, keys[2]: text}

        self.assertEqual(shift_cipher.brute_force(random_func, text, keys), expected_message)


if __name__ == '__main__':
    unittest.main()
