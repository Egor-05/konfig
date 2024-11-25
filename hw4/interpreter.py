import sys
import json


def interpreter(filename, memory):
    with open(filename, 'rb') as f:
        binary_data = f.read()
        hex_values = [hex(i)[2:].upper().zfill(2) for i in binary_data]
    for i in range(0, len(hex_values), 12):
        bit_string = ''.join([bin(int(j, 16))[2:].rjust(8, '0') for j in hex_values[i:i+12]])

        if int(bit_string[:6][::-1], 2) == 7:
            bit_string = bit_string[:51]
            a = int(bit_string[:6][::-1], 2)
            b = int(bit_string[6:33][::-1], 2)
            c = int(bit_string[33:][::-1], 2)
            memory[b] = c

        elif int(bit_string[:6][::-1], 2) == 12:
            bit_string = bit_string[:59]
            a = int(bit_string[:6][::-1], 2)
            b = int(bit_string[6:33][::-1], 2)
            c = int(bit_string[33:][::-1], 2)
            memory[b] = memory[c]

        elif int(bit_string[:6][::-1], 2) == 53:
            bit_string = bit_string[:59]
            a = int(bit_string[:6][::-1], 2)
            b = int(bit_string[6:33][::-1], 2)
            c = int(bit_string[33:][::-1], 2)
            memory[b] = memory[memory[c]]

        else:
            bit_string = bit_string[:94]
            a = int(bit_string[:6][::-1], 2)
            b = int(bit_string[6:33][::-1], 2)
            c = int(bit_string[33:60][::-1], 2)
            d = int(bit_string[60:68][::-1], 2)
            e = int(bit_string[68:][::-1], 2)
            memory[b] = memory[c + d] - memory[e]

    return memory[0:13]


if __name__ == "__main__":
    binary_file = 'binary_test.bin'#sys.argv[1]
    result_file = 'result_test.json'#sys.argv[2]
    from_idx = 0#int(sys.argv[3])
    to_idx = 10#int(sys.argv[4])
    memory = [0] * 1000

    with open(result_file, 'w') as f:
        print(interpreter(binary_file, memory))
        json.dump(memory[from_idx:to_idx + 1], f)
