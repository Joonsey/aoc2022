
class Input:
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max

    def __str__(self):
        return f"{self.min} - {self.max}"

array_of_tupes = [];

with open('file', 'r') as f:
    for line in f.readlines():
        line = line.replace("\n","")
        if line == "":
            continue
        left, right = tuple(line.split(','))
        left_values = left.split("-")
        left_input = Input(int(left_values[0]), int(left_values[1]))

        right_values = right.split("-")
        right_input = Input(int(right_values[0]), int(right_values[1]))

        array_of_tupes.append((left_input, right_input))

amount = 0
any_overlap = 0
for tupe in array_of_tupes:
    left, right = tupe
    range_of_right = [x for x in range(right.min, right.max+1)]
    range_of_left = [x for x in range(left.min, left.max+1)]

    if (left.min >= right.min and left.max <= right.max) or (right.min >= left.min and right.max <= left.max):
        amount += 1

    if left.min in range_of_right or left.max in range_of_right:
        any_overlap += 1
        print("\n",range_of_right)
        print("hitters: ", left.min, left.max)

    elif right.min in range_of_left or right.max in range_of_left:
        any_overlap += 1

        print("\n",range_of_left)
        print("hitters: ", right.min, right.max)

print("amount of covered shifts:", amount)
print("amount of overlap at all:",any_overlap)
