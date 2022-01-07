from string import punctuation
from tkinter import font


class FormatText:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'Twoj tekst to: {self.string}'

    def how_long(self):
        return len(self.string)

    def hash_format(self):
        return '#' + self.string.title().replace(" ", "")

    def reversed_string(self):
        return self.string[::-1]

    def delete_letter_from_string(self, letter):
        return self.string.replace(letter, "")

    def how_many_letters(self, letter):
        return self.string.count(letter)

    def change_chosen_letter_to_uppercase(self, letter):
        return self.string.replace(letter, letter.upper())

    def is_this_good_password(self):
        answers = ('Terrible!', 'Bad', 'It can be', 'Good', 'Perfect!!')
        points_terms = (len(self.string) > 10, self.string.istitle(), any(letter.isdigit() for letter in self.string),
                        any(sign in punctuation for sign in self.string))
        points_got = points_terms.count(True)
        return answers[points_got - 1]

    def is_this_good_nickname(self):
        answers = ('Terrible!', 'Bad', 'Good', 'Perfect!!')
        points_terms = (" " not in self.string, len(self.string) < 30, any(letter.isupper() for letter in self.string),
                        any(letter.isdigit() for letter in self.string))
        points_got = points_terms.count(True)
        return answers[points_got - 1]


a = FormatText('testujemy to')
# print(a.__str__())
# print(a.hash_format())
# print(a.reversed_string())
# print(a.delete_letter_from_string("t"))
# print(a.how_long())
# print(a.how_many_letters('t'))
# print(a.change_chosen_letter_to_uppercase('e'))
# print(a.is_this_good_password())
# print(a.is_this_good_nickname())
