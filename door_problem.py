## simulating the monty all problem just for fun

import numpy as np

num_games = 100000
options = np.arange(1, 4, 1)

stick_result = 0
switch_result = 0

for i in range(1, num_games + 1):
    winning_door = np.random.randint(1, 4)
    first_choice = np.random.randint(1, 4)

    if winning_door == first_choice:
        stick_result += 1

    # remove a door that isn't the winning_door or the first_choice
    door_to_remove = np.random.choice(options[~np.isin(options, [winning_door, first_choice])])
    options_with_one_door_removed = options[~np.isin(options, door_to_remove)]

    # switch door to remaining option that isn't the first choice
    second_choice_after_switch = options_with_one_door_removed[~np.isin(options_with_one_door_removed, first_choice)]

    if winning_door == second_choice_after_switch:
        switch_result += 1

