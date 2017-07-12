#!/usr/bin/python3
from mastermind import level
from mastermind import game
from itertools import chain
import random

class Player:
    def __init__(self, client):
        self.client = client

    def play(self, level=1):
        self.start_new_level(level)

    def start_new_level(self, level_num):
        level = self.client.start_level(level_num)
        level_details = level

        self.current_level = self.initialize_new_level(level_num, level_details)

        self.reset_remaining_possibilities()

        resp = None
        while resp == None:
            resp = self.solve_current_level()

        if resp != None:
            if 'message' in resp and 'hash' not in resp:
                self.start_new_level(level_num + 1)
            else:
                pass
                #print(resp)

    def initialize_new_level(self, level_num, level_details):
        level_details['levelNum'] = level_num
        return level.Level(level_details)

    def reset_remaining_possibilities(self):
        self.remaining_possibilities = self.current_level.all_possible_guesses()
        self.sizer = self.current_level.nPr()
        return self.remaining_possibilities

    def solve_current_level(self):
        if self.sizer > 10 ** 6:
            self.reduce_weapon_options()

        if (type(self.remaining_possibilities) == type([])) == False:
            self.remaining_possibilities = list(self.remaining_possibilities)

        guess = list(random.choice(self.remaining_possibilities))
        response = self.client.solve_level(self.current_level.levelNum, guess)

        if 'roundsLeft' in response:
            self.reset_remaining_possibilities()
            return None
        elif 'response' not in response:
            return response

        self.remaining_possibilities=[possibility for possibility in self.remaining_possibilities if game.Game_evaluate(guess, list(possibility)) == response['response']]
        self.sizer = len(self.remaining_possibilities)
        return None

    def reduce_weapon_options(self):
        weapon_combinations = list(self.current_level.weapon_combinations())
        self.sizer = len(weapon_combinations)
        guesses_with_answer = []

        while len(set([x for y in weapon_combinations for x in y])) > 10:
            weapon_guess = list(random.choice(weapon_combinations))

            resp = self.client.solve_level(self.current_level.levelNum, weapon_guess)
            weapon_combinations=[possibility for possibility in weapon_combinations if game.Game_evaluate(weapon_guess, list(possibility))[0] == resp['response'][0]]

            guesses_with_answer.append([weapon_guess, resp['response']])

        self.remaining_possibilities = list(self.current_level.possible_answers(set([x for y in weapon_combinations for x in y])))

        self.remaining_possibilities = [possibility for gwa in guesses_with_answer for possibility in self.remaining_possibilities if game.Game_evaluate(gwa[0], list(possibility)) == gwa[1]]
        return None