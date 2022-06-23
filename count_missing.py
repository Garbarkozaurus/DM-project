source = open("data/water_potability.arff",'r')

for i in range(14):
    line = source.readline()

counts = [0 for i in range(9)]

while True:
    line = source.readline()
    if not line:
        break
    counts[line.count('?')]+=1

print(counts)
print(sum(counts))