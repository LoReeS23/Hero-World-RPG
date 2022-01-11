from nickname_format import NicknameFormatting


class Hero(NicknameFormatting):
    def __init__(self, string):
        """
        :param string: nickname of hero given by user

        Function initializes new hero and sets attributes like speed or strength.
        """
        super().__init__(string)
        self.nickname = string
        self.points = 20
        self.strength = 10
        self.speed = 10
        self.hp = 10
        self.xp = 0
        self.lvl = 1

    def __str__(self):
        return f'''Nazywasz sie {self.nickname}.
        Punkty postaci: {self.points},
        Sila: {self.strength},
        Szybkosc: {self.speed}
        zdrowie: {self.hp}.'''

    def get_lvl(self):
        return self.lvl

    def get_xp(self):
        return self.xp

    def set_lvl_up(self):
        self.lvl += 1
        self.xp = 0

    def set_strength(self):
        self.strength += 1
        self.points -= 1

    def set_speed(self):
        self.speed += 1
        self.points -= 1

    def set_hp(self):
        self.hp += 1
        self.points -= 1


a = Hero('abc')


# print(a.get_lvl())
# a.set_lvl_up()
# a.set_strength()
# print(a.get_lvl())
# print(a.__str__())


class Monster:
    def __init__(self, name, hp, lvl, speed, strength, xp_if_win):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self.speed = speed
        self.strength = strength
        self.xp_if_win = xp_if_win

    def __str__(self):
        return f'''
        {self.name}
        LVL: {self.lvl}
        HP: {self.hp}
        speed: {self.speed}
        strength: {self.strength}
        '''


m = Monster('mmm', 10, 1, 3, 3, 5)
print(m.__str__())
