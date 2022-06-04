#10_2
list = []
with open("text.txt", "r") as f:
    for line in f:
        line = line.split()
        for i in line:
            list.append(int(i))
print(list)