# 0: 6
# 1: 2
# 2: 5
# 3: 5
# 4: 4
# 5: 5
# 6: 6
# 7: 3
# 8: 7
# 9: 6

# 2: 1
# 3: 7
# 4: 4
# 5: 2, 3, 5
# 6: 0, 6, 9
# 7: 8

# part 1 code
def count_easy_digits(fname):
    count = 0
    with open(fname) as f:
        for line in f:
            line = line.strip()
            line = line.split('|')[1].split()
            #print(line)
            for seq in line:
                if len(seq) in (2, 3, 4, 7):
                    count += 1
    return count

def display_binary(dec):
    bin_str = ""
    curr = dec
    for i in range(7):
        if dec & 1 == 1:
            bin_str = '1' + bin_str
        else:
            bin_str = '0' + bin_str
        dec = dec >> 1
    return bin_str
def build_binary_from_seq(seq):
    mapping = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64}
    binary = 0
    for char in seq:
        binary |= mapping[char]
    return binary

def build_mappings(unique_seqs):
    mapping = {}
    rev_mapping = {}
    easy = {2: 1, 3: 7, 4: 4, 7: 8}
    # get mappings for 1, 4, 7, 8
    for seq in unique_seqs:
        seqlen = len(seq)
        binary = build_binary_from_seq(seq)
        if seqlen in easy.keys():
            mapping[binary] = easy[seqlen]
            rev_mapping[easy[seqlen]] = binary
    # get mapping for 3
    for seq in unique_seqs:
        seqlen = len(seq)
        binary = build_binary_from_seq(seq)
        if seqlen == 5 and binary & rev_mapping[1] == rev_mapping[1]:
            mapping[binary] = 3
            rev_mapping[3] = binary
    # get mapping for 9
    mapping[rev_mapping[3] | rev_mapping[4] | rev_mapping[7]] = 9
    rev_mapping[9] = rev_mapping[3] | rev_mapping[4] | rev_mapping[7]
    # get mappings for 0 and 6
    for seq in unique_seqs:
        seqlen = len(seq)
        binary = build_binary_from_seq(seq)
        if seqlen != 6 or rev_mapping[9] == binary:
            continue
        # seqlen is 6 and seq does not map to 9
        if binary & rev_mapping[1] == rev_mapping[1]:
            # shares bits/segments with 1, so is 0
            mapping[binary] = 0
            rev_mapping[0] = binary
        else:
            # does not share bits/segments with 1, so is 6
            mapping[binary] = 6
            rev_mapping[6] = binary
    # get mappings for 2 and 5
    for seq in unique_seqs:
        seqlen = len(seq)
        binary = build_binary_from_seq(seq)
        if seqlen != 5 or rev_mapping[3] == binary:
            continue
        # seqlen in 5 and seq does not map to 3
        if binary | rev_mapping[6] == rev_mapping[6]:
            # shares bits/segments with 6, so is 5
            mapping[binary] = 5
            rev_mapping[5] = binary
        else:
            # does not share bits/segments with 6, so is 2
            mapping[binary] = 2
            rev_mapping[2] = binary
    
    #print(f'Mapping: {mapping}')
    #print(f'Reverse Mapping: {rev_mapping}')
    #for key in mapping.keys():
    #    print(display_binary(key))
    return mapping

# part 2 code
def count_all_digits(fname):
    count = 0
    with open(fname) as f:
        for line in f:
            line = line.strip()
            line = line.split('|')
            line = [seg.split() for seg in line]
            #print(line)
            mapping = build_mappings(line[0])
            #print(f'Mapping: {mapping}')
            temp = 0
            for seq in line[1]:
                binary = build_binary_from_seq(seq)
                #print(f"binary: {binary}")
                #print(f'mapping: {mapping[binary]}')
                temp = temp * 10 + mapping[binary]
            #print(temp)
            count += temp
    return count

def main():
    fname = 'input'
    num_digits = count_all_digits(fname)
    print(f'Number of Digits: {num_digits}')

if __name__ == "__main__":
    main()