import random
import csv
import operator

learning_index = [0.33,	0.3, 0.15, 0.13, 0.19, 0.36, 0.49, 0.62, 0.56, 0.17,
                  0.13, 0.26, 0.35, 0.44, 0.13, 0.12, 0.42, 0.44, 0.73, 0.75]
health_cost = [0.10, 0.11, 0.29, 0.32, 0.19, 0.14, 0.17, 0.29, 0.53, 0.10,
               0.29, 0.21, 0.31, 0.28, 0.46, 0.32, 0.20, 0.21, 0.41, 0.33]

csv_data = []
for i in range(0, 20):
    a = str(bin(int(round(100000054432077770*random.random())))).split('0b')[1]
    if len(a) > 24:
        set_bits = []
        a = a[5:25]
        for t in range(0, len(a)):
            if a[t] == '1':
                set_bits.append(t+1)
        csv_data.append([a, a.count('1'), set_bits])

csv_data = sorted(csv_data, key=operator.itemgetter(1), reverse=True)

with open('population.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(csv_data)

for i in range(0, len(csv_data)):
    if csv_data[i][1] < 11:
        csv_data = csv_data[0:i]
        break

# generating second generation pairs
second_gen = []
for i in range(0, round(len(csv_data)/2)):
    p1 = 0
    p2 = 0

    while p1 == p2:
        p1 = round((100 * random.random())) % len(csv_data)
        p2 = round((100 * random.random())) % len(csv_data)
    second_gen.append([p1, p2])

print(second_gen)
