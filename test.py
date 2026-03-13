
def gambling():
    quarters = input("Amount of Martha's quarters""\n")
    one_played = input("Machine 1 Played""\n")
    two_played = input("Machine 2 Played""\n")
    three_played = input("Machine 3 Played""\n")
    times_played = 0
    while quarters > 0:
        one_over = False
        two_over = False
        three_over = False
        while one_over == False:
            one_played += 1
            times_played += 1
            if one_played == 35:
                one_played = 0
                quarters += 30
                one_over = True
        while two_over == False:
            two_played += 1
            times_played += 1
            if two_played == 100:
                two_played = 0
                quarters += 60
                two_over = True
        while three_over == False:
            three_played += 1
            times_played += 1
            if three_played == 10:
                three_played = 0
                quarters += 9
                three_over = True
    print("Martha went broke after", times_played, "times of playing")

gambling()