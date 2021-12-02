with open("input2.txt") as f:
    lines = f.readlines()

x = 0
y = 0
aim = 0

for line in lines:
    split_line = line.strip().split(" ")
    direction = split_line[0]
    num = int(split_line[1])
    if direction == "forward":
        x += num
        y += num*aim
    elif direction == "up":
        aim -= num
    elif direction == "down":
        aim += num

print(x * y)