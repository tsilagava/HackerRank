def print_formatted(number):
    width = len(bin(number).replace("0b",""))
    for i in range(1,number+1):
        print(str(i).rjust(width), str(oct(i).replace("0o", "")).rjust(width), str(hex(i).replace("0x","") .upper()).rjust(width), str(bin(i).replace("0b","")).rjust(width) )
    



print_formatted(17)