text = "I wonder what language that is"
count_t = text.count('t')
count_T = text.count('T')
count_s = text.count('s')
count_S = text.count('S')

if count_t + count_T > count_s + count_S:
    print('Your text is in English')
else:
    print('Your text is in French')