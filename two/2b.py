import os
import re
os.chdir("D:\~Studio Stuffz~\Coding\Python coding\Advent of code\\two")
f = open("2.txt", "r")

foward = 0
depth = 0
aim = 0

text_arr = [e.rstrip() for e in f.readlines()]
int_arr = [int(re.sub("\D", "", e)) for e in text_arr]

for i in range(len(text_arr)):
    if text_arr[i][0] == "f":
        foward += int_arr[i]
        depth += aim*int_arr[i]
    elif text_arr[i][0] == "u":
        aim -= int_arr[i]
    elif text_arr[i][0] == "d":
        aim += int_arr[i]

print(depth, foward)
print("Answer: ", depth*foward)
