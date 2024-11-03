from numpy import random
random.seed(1234)

def n_dice_dupes(num_dice, sims, only_one_pair = False):
    die, probabilities = [1,2,3,4,5,6], [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    pairs = 0
    for i in range(sims):
        dice_roll = random.choice(die, size=num_dice, p=probabilities)
        for n in range(num_dice):
            if only_one_pair:
                only_once = False
                if dice_roll[n] == dice_roll[n-1]:
                    pairs += 1
                    only_once = True

                if only_once:
                    break
            else:
                if dice_roll[n] == dice_roll[n-1]:
                    pairs += 1
    return sims, pairs

