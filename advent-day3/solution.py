import os

BASE_DIR = os.getcwd() 

with open(BASE_DIR+ "\\advent-day3\\input.txt") as File :
    file = File.readlines()
file = [ l.strip() for l in file ]
depth = 0
horizontal = 0
aim = 0
for x in file :
    if "down" in x :
        aim += int(x.split(" ")[1])
    elif "up" in x :
        aim -= int(x.split(" ")[1])
    else :
        horizontal += int(x.split(" ")[1])
        depth += aim * (int(x.split(" ")[1]))
print("depth is :", depth, "horizontal is :", horizontal, "aim is :", aim)
print(depth*horizontal)