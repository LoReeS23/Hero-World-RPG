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