#!/usr/bin/env python
"""
# date: 07/07/2017
# author: Ganesh Manal
# description: A Sample battleship Game
"""

import os
import sys
from battlespace import BattleField


def run():
    """
    Read battle details, Configure Battle and run battle.
    """
    battle_details = list()
    with open(os.getcwd() + os.path.sep + 'input.txt') as input_file:
        for line in input_file.readlines():
            battle_details.append(line.strip())

    # Configure And Start Battle
    bf_obj = BattleField()
    ret_val, msg = bf_obj.configure_battle(battle_details)
    if not ret_val:
        print("Error: %s", msg)
        sys.exit(1)

    # Run Battle
    ret_val = bf_obj.run_battle()

if __name__ == '__main__':
    run()
