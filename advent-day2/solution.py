import os

BASE_DIR = os.getcwd() 

with open(BASE_DIR+ "\\advent-day2\\input.txt") as File :
    file = File.readlines()
file = [ l.strip() for l in file ]
depth = 0
horizontal = 0
for x in file :
    if "down" in x :
        depth += int(x.split(" ")[1])
    elif "up" in x :
        depth -= int(x.split(" ")[1])
    else :
        horizontal += int(x.split(" ")[1])
print("depth is :", depth, "horizontal is :", horizontal, '\n')
print(depth*horizontal)
