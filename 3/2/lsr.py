class BinSeqTree:
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None
    
    def add_bin_seq(self, bin_seq):
        curr_node = self
        curr_node.val += 1
        for char in bin_seq:
            if (curr_node.left == None):
                curr_node.left = BinSeqTree()
            if (curr_node.right == None):
                curr_node.right = BinSeqTree()
            if char == '0':
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            curr_node.val += 1
    
    def calculate_ogr(self):
        result = ""
        curr_node = self
        while True:
            if (curr_node.left == None or curr_node.right == None):
                break
            if curr_node.right.val >= curr_node.left.val:
                result += '1'
                curr_node = curr_node.right
            else:
                result += '0'
                curr_node = curr_node.left
        return result
    
    def calculate_co2s(self):
        result = ""
        curr_node = self
        while True:
            if (curr_node.left == None or curr_node.right == None):
                break
            if curr_node.left.val <= curr_node.right.val:
                if curr_node.left.val == 0:
                    result += '1'
                    curr_node = curr_node.right
                else:
                    result += '0'
                    curr_node = curr_node.left
            else:
                if curr_node.right.val == 0:
                    result += '0'
                    curr_node = curr_node.left
                else:
                    result += '1'
                    curr_node = curr_node.right
        return result


def calculate_lsr(binseqtree, ogr_res):
    curr_node = binseqtree
    for char in ogr_res:
        if char == '0':
            if (curr_node.left == None):
                pass
            curr_node = curr_node.left
        else:
            if (curr_node.right == None):
                pass
            curr_node = curr_node.right


def bin_to_dec(bin_str):
    bin_str = bin_str[::-1]
    result = 0
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            result += 2 ** i
    return result

def main():
    binseqtree = BinSeqTree()
    with open('input') as f:
        # iterate over data and build binseqtree
        for line in f:
            line = line.strip()
            binseqtree.add_bin_seq(line)
    ogr_res = binseqtree.calculate_ogr()
    co2s_res = binseqtree.calculate_co2s()
    print(f'OGR: {ogr_res}')
    print(f'CO2S: {co2s_res}')
    print(f'LSR: {bin_to_dec(ogr_res) * bin_to_dec(co2s_res)}')
        
    
    with open('input') as f:
        pass
if __name__ == "__main__":
    main()