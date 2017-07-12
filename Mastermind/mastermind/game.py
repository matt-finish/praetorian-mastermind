def Game_evaluate(guess, secret):
    correct_attack = 0
    for index in range(len(guess)):
        if guess[index] == secret[index]:
            correct_attack += 1
    correct_weapon = len(secret) - len(list(set(secret)-set(guess)))
    return [correct_weapon, correct_attack]