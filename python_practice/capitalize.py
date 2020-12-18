def solve(s):
    total = ""
    s_list = s.split(" ")
    length = len(s_list)
    for i in range(length):
        if s_list[i].isdigit():
            total += s_list[i] + ' '
        else:
            total += s_list[i].capitalize() + ' '

    print(len(total)) 
    return total



s="1 2 2 3 4 5 6 7 8  9"
print(len(s))

print(solve(s))
