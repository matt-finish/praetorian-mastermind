import itertools as it
from math import factorial

class Level:
    def __init__(self, level_details={}, roundsLeft=None):
        self.roundsLeft = roundsLeft
        self.numGladiators = level_details['numGladiators']
        self.numGuesses = level_details['numGuesses']
        self.numRounds = level_details['numRounds']
        self.numWeapons = level_details['numWeapons']
        self.levelNum = level_details['levelNum']
    
    def all_possible_responses(self):
        responses = []
        for correctWeapon in range(0, self.numGladiators+1):
            for correctAttack in range(0, correctWeapon+1):
                if correctWeapon == self.numGladiators and correctAttack + 1 == self.numGladiators:
                    continue
                responses.append([correctWeapon, correctAttack])
        
        return responses
    
    def nPr(self):
        return int(factorial(self.numWeapons)/factorial(self.numWeapons-self.numGladiators))
    
    def all_possible_guesses(self):
        return it.permutations(range(0, self.numWeapons), self.numGladiators)
    
    def possible_answers(self, weapons):
        return it.permutations(weapons, self.numGladiators)
    
    def weapon_combinations(self):
        return it.combinations(range(0, self.numWeapons), self.numGladiators)