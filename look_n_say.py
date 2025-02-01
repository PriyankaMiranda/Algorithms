
def look_n_say(val, loc, length):
    final_ans = ""
    buffer = []
    prev_val = val[0]
    buffer.append(val[0])

    loc = 1
    while loc < length:
        if (prev_val != val[loc]):
            if(len(buffer)):
                final_ans = final_ans + str(len(buffer))+ str(prev_val)
            else:
                final_ans = final_ans + "1" + prev_val
            buffer = []
            buffer.append(val[loc])
        else:
            buffer.append(val[loc])
        prev_val = val[loc]
        loc += 1
    if len(buffer):
        return int(final_ans + str(len(buffer))+str(buffer[0]))    
    
    return int(final_ans + val)

start = 1 
max_length = 6
current_list = [0 for x in range(0, max_length)]
print(f"list: {current_list}")

current_list[0] = start
i = 1
while i < max_length: 
    current_list[i] = look_n_say(
        str(current_list[i-1]), 
        0, 
        len(str(current_list[i-1]))
    )
    i += 1

print(f"list: {current_list}")
