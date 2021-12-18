def read_data(fname):
    template = ""
    mapping = {}
    with open(fname) as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            template = line
        for line in f:
            line = line.strip().split()
            mapping[line[0]] = line[2]
    return template, mapping


def add_pair(a_dict, pair):
    if pair not in a_dict.keys():
        a_dict[pair] = 0
    a_dict[pair] += 1
    return a_dict


def dp_grow(template, mapping, steps=1):
    pairs = {}
    for i in range(1, len(template)):
        pairs = add_pair(pairs, template[i-1:i+1])
    #print(pairs)
    for step in range(steps + 1):
        if step == steps:
            letters = {}
            for pair in pairs.keys():
                if pair[0] not in letters.keys():
                    letters[pair[0]] = 0
                #print(f'Letter: {pair[0]}, pairs[{pair}]={pairs[pair]}')
                letters[pair[0]] += pairs[pair]
            letters[template[-1]] += 1
            print(f'Pairs: {pairs}')
            print(f'Letters: {letters}')
            print(f'sum: {sum(letters.values())}')
            return max(letters.values()) - min(letters.values())
        # add new pairs:
        new_pairs = {}
        for pair in pairs.keys():
            if pair[0] + mapping[pair] not in new_pairs.keys():
                new_pairs[pair[0] + mapping[pair]] = 0
            new_pairs[pair[0] + mapping[pair]] += pairs[pair]
            if mapping[pair] + pair[1] not in new_pairs.keys():
                new_pairs[mapping[pair] + pair[1]] = 0
            new_pairs[mapping[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs
        #print(pairs)


def grow(template, mapping, steps=1):
    curr_template = template
    new_template = ""
    occs = {}
    for j in range(steps):
        if (curr_template[0] not in occs.keys()):
            occs[curr_template[0]] = 0
        occs[curr_template[0]] += 1
        new_template += curr_template[0]
        for i in range(1, len(curr_template)):
            key = curr_template[i-1:i+1]
            if (curr_template[i] not in occs.keys()):
                occs[curr_template[i]] = 0
            occs[curr_template[i]] += 1
            if (mapping[key] not in occs.keys()):
                occs[mapping[key]] = 0
            occs[mapping[key]] += 1
            new_template += mapping[key] + curr_template[i]
        #print(f'Template: {new_template}')
        #print("occurrences:")
        #for occ in occs.keys():
        #    print(f'\t{occ} -> {occs[occ]}')
        if j+1 == steps:
            break
        curr_template = new_template
        new_template = ""
        occs = {}
    return occs

def main():
    fname = 'input'
    template, mapping = read_data(fname)
    #print(f'Template: {template}')
    #print("Mapping:")
    #for key in mapping.keys():
    #    print(f'\t{key} -> {mapping[key]}')
    result = dp_grow(template, mapping, 10)
    print(result)
    result = dp_grow(template, mapping, 40)
    print(result)
if __name__ == "__main__":
    main()