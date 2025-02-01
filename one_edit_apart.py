
def compute(s1, s2, max_len):
    #s1 has the offset
    not_equal_counter = 0
    j = 0
    for x in range(0, max_len):
        if (not_equal_counter > 1):
            return False
        if (s1[x] != s2[j]): # mismatch!
            if (x+1 < max_len):
                x = x + 1
            not_equal_counter += 1
            j = j -1
        
        if j < len(s2) - 1: 
            j = j + 1
    return True

def one_edit_apart(s1, s2):
    # if lengths are same, possible a replaced character
    not_equal_counter = 0
    if len(s1) == len(s2):
        for x in range(0, len(s2)):
            if (not_equal_counter > 1):
                return False
            if (s1[x] != s2[x]):
                not_equal_counter += 1

        return True
    else:
        max_len = max(len(s1), len(s2))

        # Inserting one character anywhere in the word (including at the beginning and end)

        if(len(s1) > len(s2)): 
            return compute(s1, s2, max_len)
        else:
            return compute(s2, s1, max_len)



s1 = "cat"
s2 = "cast"
print(one_edit_apart(s1, s2))