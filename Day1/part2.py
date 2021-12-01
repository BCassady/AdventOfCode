
with open("input.txt") as f:
    lines = f.readlines()

count = 0
new_lines = []
for line in lines:
    line = line.strip()
    new_lines.append(int(line))

prev = sum(new_lines[0:3])
for i in range(1, len(new_lines)):
    num = sum(new_lines[i:i+3])
    if num > prev:
        count += 1

    prev = num
print(count)