def bin_to_dec(bin_str):
    bin_str = bin_str[::-1]
    result = 0
    for i in range(len(bin_str)):
        if bin_str[i] == '1':
            result += 2 ** i
    return result

def main():
    with open('test') as f:
        ## get first line data
        gamma = []
        isFirstPass = True
        for line in f:
            line = line.strip()
            if isFirstPass:
                gamma = [0]*len(line)
                isFirstPass = False
            for i in range(len(gamma)):
                if int(line[i]) == 1:
                    gamma[i] += 1
                else:
                    gamma[i] -= 1
        gamma_res = ""
        epsilon_res = ""
        for i in range(len(gamma)):
            if (gamma[i] > 0):
                gamma_res += '1'
                epsilon_res += '0'
            else:
                gamma_res += '0'
                epsilon_res += '1'
        print('gamma_res: ' + gamma_res)
        print('epsilon_res: ' + epsilon_res)
        print(f'Power Consumption: {bin_to_dec(gamma_res)*bin_to_dec(epsilon_res)}')
if __name__ == "__main__":
    main()