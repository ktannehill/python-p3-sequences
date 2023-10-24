#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        seq = [0, 1]

        while len(seq) < length:
            seq.append(seq[-1] + seq[-2])
        print(seq)
    pass

print_fibonacci(9)