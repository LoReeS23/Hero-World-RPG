from nickname_format import NicknameFormatting


class Hero(NicknameFormatting):
    def __init__(self, string):
        super().__init__(string)
        self.nickname = string
        self.points = 20
        self.strength = 10
        self.speed = 10
        self.health = 10

    def __str__(self):
        return f'''Nazywasz sie {self.nickname}.
        Punkty postaci: {self.points},
        Sila {self.strength},
        Szybkosc {self.speed}
        zdrowie {self.health}.
        '''


a = Hero('abc')
print(a.__str__())
print(a.how_long())
