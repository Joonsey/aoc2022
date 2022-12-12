#[T]             [P]     [J]        
#[F]     [S]     [T]     [R]     [B]
#[V]     [M] [H] [S]     [F]     [R]
#[Z]     [P] [Q] [B]     [S] [W] [P]
#[C]     [Q] [R] [D] [Z] [N] [H] [Q]
#[W] [B] [T] [F] [L] [T] [M] [F] [T]
#[S] [R] [Z] [V] [G] [R] [Q] [N] [Z]
#[Q] [Q] [B] [D] [J] [W] [H] [R] [J]
# 1   2   3   4   5   6   7   8   9 

import re

crates = {}
crates[1] = ["Q", "S", "W", "C", "Z", "V", "F", "T"]
crates[2] = ["Q", "R", "B"]
crates[3] = ["B", "Z", "T", "Q", "P", "N", "S"]
crates[4] = ["D", "V", "F", "R", "Q", "H"]
crates[5] = ["J", "G", "L", "D", "B", "S", "T", "P"]
crates[6] = ["W", "R", "T", "Z"]
crates[7] = ["H", "Q", "M", "N", "S", "F", "R", "J"]
crates[8] = ["R", "N", "F", "H", "W"]
crates[9] = ["J", "Z", "T", "Q", "P", "R", "B"]

def parse_instructions(line: str) -> list[str]:
    return re.findall(r'[0-9]+', line)

def first_one():
    with open("file", "r") as f:
        for line in f.readlines():
            match = parse_instructions(line)
            item_amount = int(match[0])
            for items in range(item_amount):
                to_get = crates[int(match[1])].pop()
                crates[int(match[2])].append(to_get)
                print(f"moved {to_get}, from {crates[int(match[1])]}, to {crates[int(match[2])]}")

    for crate in crates.keys():
        print(crates[crate][-1])


def second_one():
    with open("file", "r") as f:
        for line in f.readlines():
            match = parse_instructions(line)
            item_amount = int(match[0])

            all_crates_to_move = crates[int(match[1])][-item_amount:]
            for i in range(item_amount):
                crates[int(match[1])].pop()

            #print("crates to move", all_crates_to_move)
            #print("keys: ",match)
            #for crate in crates.keys():
                #print(crates[crate])
            crates[int(match[2])].extend(all_crates_to_move)

    for crate in crates.keys():
        print(crates[crate][-1])

#first_one()
second_one()

