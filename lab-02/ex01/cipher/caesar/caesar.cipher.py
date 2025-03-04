from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

        def encrypy_text(self, text: str, key: int) -> str:
            alphabet_len = len(self.alphabet)
            text = text.upper()
            encrypy_text = []
            for letter in text:
                letter_index = self
