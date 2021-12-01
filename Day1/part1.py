with open("input.txt") as f:
    lines = f.readlines()

count = 0

for i in range(1, len(lines)):
    
    if int(lines[i]) > int(lines[i-1]):
        count += 1

print(count)