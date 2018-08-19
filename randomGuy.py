import random
import csv
import operator

learning_index = [0.33,	0.3, 0.15, 0.13, 0.19, 0.36, 0.49, 0.62, 0.56, 0.17,
                  0.13, 0.26, 0.35, 0.44, 0.13, 0.12, 0.42, 0.44, 0.73, 0.75]
health_cost = [0.10, 0.11, 0.29, 0.32, 0.19, 0.14, 0.17, 0.29, 0.53, 0.10,
               0.29, 0.21, 0.31, 0.28, 0.46, 0.32, 0.20, 0.21, 0.41, 0.33]

complete_pop = [['chromosome', 'no_of_set_bits', 'learning_index', 'health_cost', 'li-hc', 'set_bits']]
index = 0


def cross_and_mute(p1, p2):

    new_child = ''
    for i in range(0, len(p1)):
        if round(random.random()*10)%2 == 0:
            new_child += str(p1[i])
        else:
            new_child += str(p2[i])

    mut_index = round(random.random()*900) % 20
    if new_child[mut_index] == '1':
        new_child = new_child[0:mut_index] + '0' + new_child[mut_index+1:20]
    else:
        new_child = new_child[0:mut_index] + '1' + new_child[mut_index+1:20]

    l_i = 0
    h_c = 0
    set_bits = []
    for t in range(0, len(a)):
        if new_child[t] == '1':
            l_i += learning_index[t]
            h_c += health_cost[t]
            set_bits.append(t + 1)

    return [new_child, new_child.count('1'), str(l_i)[0:4], str(h_c)[0:4], str(l_i - h_c)[0:4], set_bits]


# the first population
for i in range(0, 20):
    a = str(bin(int(round(100000054432077770*random.random())))).split('0b')[1]
    if len(a) > 24:
        l_i = 0
        h_c = 0
        set_bits = []
        a = a[5:25]
        for t in range(0, len(a)):
            if a[t] == '1':
                l_i += learning_index[t]
                h_c += health_cost[t]
                set_bits.append(t+1)

        complete_pop.append([a, a.count('1'), str(l_i)[0:4], str(h_c)[0:4], str(l_i - h_c)[0:4], set_bits, 'F'])

# those having no. of set bits > 10 (minimum 50% attendance)
first_gen = sorted(complete_pop[1:len(complete_pop)], key=operator.itemgetter(1), reverse=True)
for i in range(0, len(first_gen)):
    if first_gen[i][1] < 11:
        first_gen = first_gen[0:i]
        break


with open('first_gen.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(first_gen)

# generating next generation pairs
next_gen_probs = []
for i in range(0, round(len(first_gen))):
    p1 = 0
    p2 = 0

    while p1 == p2:
        p1 = round((100 * random.random())) % len(first_gen)
        p2 = round((100 * random.random())) % len(first_gen)
    next_gen_probs.append([p1, p2])

next_gen = []

for i in range(0, len(next_gen_probs)):
    new_guy = cross_and_mute(first_gen[next_gen_probs[i][0]][0], first_gen[next_gen_probs[i][1]][0])
    new_guy.append(str(next_gen_probs[i][0]) + ' ' + str(next_gen_probs[i][1]))
    next_gen.append(new_guy)
    complete_pop.append(new_guy)

next_gen = sorted(next_gen, key=operator.itemgetter(4), reverse=True)


with open('next_gen.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(next_gen)

with open('complete_population.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(complete_pop)

