from string import punctuation


def joining(s):
    text = ".".join(s)
    return text


# print(joining('hi every'))
# print(joining(['hi', 'every']))

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
        return answers[points_got]


a = FormatText('testujemy to')


# print(a.__str__())
# print(a.hash_format())
# print(a.reversed_string())
# print(a.delete_letter_from_string("t"))
# print(a.how_long())
# print(a.how_many_letters('t'))
# print(a.change_chosen_letter_to_uppercase('e'))
# print(a.is_this_good_password())

# -------------------------------------------------------------------

def score(dice):
    game_score = 0
    if 1 in dice:
        if dice.count(1) >= 3:
            game_score += 1000 + (dice.count(1) - 3) * 100
        else:
            game_score += dice.count(1) * 100
    if 5 in dice:
        if dice.count(5) >= 3:
            game_score += 500 + (dice.count(5) - 3) * 50
        else:
            game_score += dice.count(5) * 50
    triple_other_number = [number for number in dice if dice.count(number) >= 3 and number != 1 and number != 5]
    if triple_other_number != []:
        game_score += triple_other_number[0] * 100
    return game_score


print(score([4, 4, 3, 5, 1]))
