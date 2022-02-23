
#verified
def bin_to_dec(bin):
    if len(bin) == 1:
        return int(bin)
    init = bin[:-1]
    last = bin[-1]
    return bin_to_dec(init) * 2 + int(last)


print(bin_to_dec('101'))
print(bin_to_dec('0'))
print(bin_to_dec('1'))
print(bin_to_dec('101101'))