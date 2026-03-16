def gambling(quarters, one, two, three):
    times_played = 0
    slot_one = one
    slot_two = two
    slot_three = three
    coins = quarters
    while coins > 0:
        if slot_one == 35:
            coins += 30
            slot_one = 0
        if slot_two == 100:
            coins += 60
            slot_two = 0
        if slot_three == 10:
            coins += 9
            slot_three = 0
        slot_one += 1
        times_played += 1
        coins -= 1
        slot_two += 1
        times_played += 1
        coins -= 1
        slot_three += 1
        times_played += 1
        coins -= 1
    return times_played







print(gambling(48, 3, 10, 4))