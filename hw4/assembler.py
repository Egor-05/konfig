import sys
import json

def encode_const(string):
    bit_string = '111000'
    log = {'A': 7, 'B': int(string[1]), 'C': int(string[2])}
    bit_string += bin(int(string[1]))[2:].rjust(27, '0')[::-1]
    bit_string += bin(int(string[2]))[2:].rjust(18, '0')[::-1]
    bit_string = bit_string.ljust(96, '0')
    array = [int(bit_string[8 * i: 8 * i + 8], 2) for i in range(12)]
    return array, log


def encode_read(string):
    bit_string = '001100'
    log = {'A': 12, 'B': int(string[1]), 'C': int(string[2])}
    bit_string += bin(int(string[1]))[2:].rjust(27, '0')[::-1]
    bit_string += bin(int(string[2]))[2:].rjust(27, '0')[::-1]
    bit_string = bit_string.ljust(96, '0')
    array = [int(bit_string[8 * i: 8 * i + 8], 2) for i in range(12)]
    return array, log

def encode_write(string):
    bit_string = '101011'
    log = {'A': 52, 'B': int(string[1]), 'C': int(string[2])}
    bit_string += bin(int(string[1]))[2:].rjust(27, '0')[::-1]
    bit_string += bin(int(string[2]))[2:].rjust(27, '0')[::-1]
    bit_string = bit_string.ljust(96, '0')
    array = [int(bit_string[8 * i: 8 * i + 8], 2) for i in range(12)]
    return array, log

def encode_sub(string):
    bit_string = '011001'
    log = {'A': 38, 'B': int(string[1]), 'C': int(string[2]), 'D': int(string[3]), 'E': int(string[4])}
    bit_string += bin(int(string[1]))[2:].rjust(27, '0')[::-1]
    bit_string += bin(int(string[2]))[2:].rjust(27, '0')[::-1]
    bit_string += bin(int(string[3]))[2:].rjust(8, '0')[::-1]
    bit_string += bin(int(string[4]))[2:].rjust(27, '0')[::-1]
    bit_string = bit_string.ljust(96, '0')
    array = [int(bit_string[8 * i: 8 * i + 8], 2) for i in range(12)]
    return array, log


COMMANDS = {
    'CONST': encode_const,
    'READ': encode_read,
    'WRITE': encode_write,
    'SUB': encode_sub
}


def encoder(text, binary):
    lines = []
    logs = []
    with open(text) as f:
        for i in f.readlines():
            a = i.strip().split()
            array, log = COMMANDS[a[0]](a)
            lines.append(array)
            logs.append(log)
    with open(binary, 'wb') as f:
        for line in lines:
            for i in line:
                data = i.to_bytes(1, byteorder='big')
                f.write(data)
    return logs


if __name__ == "__main__":
    text_file = sys.argv[1]
    binary_file = sys.argv[2]
    try:
        log_file = sys.argv[3]
    except IndexError:
        log_file = None
    logs = encoder(text_file, binary_file)

    if log_file:
        with open(log_file, 'w') as f:
            json.dump(logs, f)

