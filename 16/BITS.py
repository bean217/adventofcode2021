BINARY = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
    }

STRARY = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
    }

def read_bits(fname):
    with open(fname) as f:
        r = f.read()
    return r.strip().split('\n')[0]


def translate(data):
    binary = ""
    for char in data:
        binary += BINARY[char]
    return binary


def bin(binary):
    num = 0
    binlen = len(binary)
    i = binlen - 1
    while i >= 0:
        num += int(binary[i]) * (2 ** (binlen - 1 - i))
        i -= 1
    return num


def stringify(binary):
    string = ""
    for i in range(len(binary)//4):
        string += STRARY[binary[i*4:i*4+4]]
    return string


class Operator:
    def __init__(self, version, type, typeID, length, subpackets):
        self.version = version
        self.type = type
        self.typeID = typeID
        self.length = length
        self.subpackets = subpackets

    def value(self):
        if self.type == 0:
            result = 0
            for packet in self.subpackets:
                result += packet.value()
            return result
        elif self.type == 1:
            result = 1
            for packet in self.subpackets:
                result *= packet.value()
            return result
        elif self.type == 2:
            minimum = float('inf')
            for packet in self.subpackets:
                res = packet.value()
                if res < minimum:
                    minimum = res
            return minimum
        elif self.type == 3:
            maximum = 0
            for packet in self.subpackets:
                res = packet.value()
                if res > maximum:
                    maximum = res
            return maximum
        elif self.type == 5:
            res1 = self.subpackets[0].value()
            res2 = self.subpackets[1].value()
            if res1 > res2:
                return 1
            else:
                return 0
        elif self.type == 6:
            res1 = self.subpackets[0].value()
            res2 = self.subpackets[1].value()
            if res1 < res2:
                return 1
            else:
                return 0
        elif self.type == 7:
            res1 = self.subpackets[0].value()
            res2 = self.subpackets[1].value()
            if res1 == res2:
                return 1
            else:
                return 0

    def __repr__(self):
        string = f'Operator: [Version: {self.version}, Type: {self.type}, '
        if self.typeID == 1:
            string += '#SubPacks: '
        else:
            string += 'LenSubPacks: '
        string += f'{self.length}, \n\t[Subpackets: {[sub for sub in self.subpackets]}]' 
        return string

class Literal:
    def __init__(self, version, type, value):
        self.version = version
        self.type = type
        self.val = value

    def value(self):
        return self.val

    def __repr__(self):
        string = f'Literal: [Version: {self.version}, Type: {self.type}, Value: {self.value}]'
        return string

def get_subpackets_by_length(data, i, length):
    sub_packets = []
    length_used = 0
    while length_used < length:
        sub_packet, new_i = decode(data, i)
        sub_packets += [sub_packet]
        length_used += new_i - i
        i = new_i
    return sub_packets, i

def get_subpackets_by_number(data, i, number):
    sub_packets = []
    number_used = 0
    while number_used < number:
        sub_packet, i = decode(data, i)
        sub_packets += [sub_packet]
        number_used += 1
    return sub_packets, i

def get_literal_value(data, i):
    value = ""
    while True:
        is_last_value = data[i] == '0'
        value += data[i+1:i+5]
        i += 5
        if is_last_value:
            break
    return value, i 

def decode(data, i=0):
    print(f'I = {i}--> {data[i:]}')
    # packet version
    version = bin(data[i:i+3])
    # packet type
    ptype = bin(data[i+3:i+6])
    i += 6
    packet = None
    if ptype == 4:
        value, i = get_literal_value(data, i)
        packet = Literal(version, ptype, bin(value))
    else:
        typeID = int(data[i])
        i += 1
        if typeID == 1:
            # L is # of packets, L=11
            length = bin(data[i:i+11])
            i += 11
            subpackets, i = get_subpackets_by_number(data, i, length)
        else:
            # L is length of remaining packets, L=15
            length = bin(data[i:i+15])
            i += 15
            subpackets, i = get_subpackets_by_length(data, i, length)
        packet = Operator(version, ptype, typeID, length, subpackets)
    return packet, i

def decode_all(data, i=0):
    lendata = len(data)
    packets = []
    while i < lendata:
        packet, i = decode(data, i)
        packets += [packet]
        i += 8 - (i%8)
    return packets

def version_sums(packets, sum=0):
    for packet in packets:
        sum += packet.version
        if type(packet) == Operator:
            sum += version_sums(packet.subpackets)
    return sum

def main():
    fname = 'input'
    data = read_bits(fname)
    print(data)
    print()
    data = translate(data)
    print(data)
    packets = decode_all(data)
    sums = version_sums(packets)
    print(f"Version Sums: {sums}")
    print(f'Outter-Most Value: {packets[0].value()}')
if __name__ == "__main__":
    main()