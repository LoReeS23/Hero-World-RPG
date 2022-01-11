import codecs


class NicknameFormatting:
    def __init__(self, string):
        """

        :param string: Nickname given by user
        """
        self.string = string

    def how_long(self):
        return len(self.string)

    def hash_format(self):
        return '#' + self.string.title().replace(" ", "")

    def make_nickname_part(self):
        return self.string.title().replace(" ", "")

    def reversed_string(self):
        return self.string[::-1]

    def delete_letter_from_string(self, letter):
        return self.string.replace(letter, "")

    def how_many_letters(self, letter):
        return self.string.count(letter)

    def change_chosen_letter_to_uppercase(self, letter):
        return self.string.replace(letter, letter.upper())

    def is_this_good_nickname(self):
        answers = ('Terrible!', 'Bad', 'Good', 'Perfect!!')
        points_terms = (" " not in self.string, len(self.string) < 30, any(letter.isupper() for letter in self.string),
                        any(letter.isdigit() for letter in self.string))
        points_got = points_terms.count(True)
        return answers[points_got - 1]

    def encode_string_rot13(self):
        return codecs.encode(self.string, 'rot13')
