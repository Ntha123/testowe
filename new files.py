from operator import itemgetter


def yatzi(dice):
    """
    Score the given roll in the 'Yatzi' category
    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0
