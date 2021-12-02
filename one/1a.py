import os
os.chdir("D:\~Studio Stuffz~\Coding\Python coding\Advent of code\1")
f = open("1.txt", "r")
tally = 0;
prev_line = 0;
arr = f.readlines()
fixed_arr = []
best_arr = []
tally = 0
for elem in arr:
    fixed_arr.append(elem.strip())
for elem in arr:
    best_arr.append(int(elem.strip()))
for elem in best_arr:
    if prev_line == 0:
        prev_line = elem
    else:
        if elem > prev_line:
            tally += 1
        prev_line = elem
print("tally: ", tally)
