# with open("Sample.txt") as file :
#     file = file.readlines()
# File = file[0].split(",")
# for i in range(0, len(File)):
#     File[i] = int(File[i])


# Ans = 0
# i = 1
# while i <= 80 :
#     for j in range(0, len(File)+1) :
#         if File[j] == 0 :
#             File.append(8)
#             File[j] = 6
#         else :
#             File[j] -= 1
#     i += 1
# print(File)
# for i in File :
#     Ans += i
# print(Ans)
#1,0,2,5
#0,6,1,4,8
#6,5,0,3,7,8
#5,4,6,2,6,7,8
line = ""
with open('input.txt') as f:
    line = f.readline()
nums = line.split(",")

#print (nums)

fishes = [0,0,0,0,0,0,0,0,0]

for fish in nums:
  fishes[int(fish)] = fishes[int(fish)]+1

print (f"Start:{fishes}")

def newday(day):
  newfishborn = False
  newfishCount = 0
  if (fishes[0]>0):
    newfishborn = True
    newfishCount = fishes[0]
  fishes.append(fishes.pop(0))
  if newfishborn == True:
    fishes[6] = fishes[6] + newfishCount
  print (f"day {x+1}:{fishes}")

for x in range(256):
  newday(x)


total = 0
for fish in fishes:
  total = total + fish
print()
print(f"Total Fish Population is:{total}")