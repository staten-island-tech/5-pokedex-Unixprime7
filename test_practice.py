#text = "I wonder what language that is"
#count_t = text.count('t')
#count_T = text.count('T')
#count_s = text.count('s')
#count_S = text.count('S')

#if count_t + count_T > count_s + count_S:
    #print('Your text is in English')
#else:
#    print('Your text is in French')

text = "HHHHOOONNNIII"

honi_count = 0
which_letter = 0
while which_letter < len(text):
    h_found = False
    while not h_found:
        if text[int(which_letter)] == "H":
            which_letter = which_letter + 1
            h_found = True
        else:
            which_letter = which_letter + 1
    o_found = False
    while not o_found:
        if text[int(which_letter)] == "O":
                which_letter = which_letter + 1
                o_found = True
        else:
            which_letter = which_letter + 1
    n_found = False
    while not n_found:
        if text[int(which_letter)] == "N":
            which_letter = which_letter + 1
            n_found = True
        else:
            which_letter = which_letter + 1
    i_found = False
    while not i_found:
        if text[int(which_letter)] == "I":
            which_letter = which_letter + 1
            i_found = True
        else:
            which_letter = which_letter + 1
    if h_found and o_found and n_found and i_found:
        honi_count = honi_count + 1
print(honi_count)
        
    

