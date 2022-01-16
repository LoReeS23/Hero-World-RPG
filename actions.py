from characters import Hero, Monster
import random

all_monsters = []


def create_some_random_monsters():
    for enemy in range(random.randint(1, 3)):
        enemy = Monster('x', random.randint(1, 20), random.randint(1, 30), random.randint(1, 100),
                        random.randint(1, 100), random.randint(1, 100))
        all_monsters.append(enemy)
    return all_monsters


def find_monster():
    """
    :return: You ran away from a fight and maybe death.
    Function finds a nearby monsters. If monsters exists you can choose to fight them or not.
    """
    if len(all_monsters) > 0:
        fight_prompt = input("There are monsters nearby. Wanna fight one of them? y -> yes; n -> no")
        if fight_prompt == "y":
            fight()
        else:
            return "You ran away."

    return "No monsters."


def fight():
    pass


m = Monster('mmm', 10, 1, 3, 3, 5)
all_monsters.append(m)
print(all_monsters)
print(find_monster())
