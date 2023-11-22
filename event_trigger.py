import map as mp


def is_at_school(character, school_doors):
    player_position = (character['X'], character['Y'])
    for door_position in school_doors:
        if player_position == door_position:
            return True
    return False


def is_near_gym(character, school_doors):
    pass


def is_near_park(character, school_doors):
    pass
