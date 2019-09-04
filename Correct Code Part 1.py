import os
from collections import defaultdict as dd
os.chdir(r'C:\Users\Gabriel\Desktop')
lines = open('.\Advent.txt').read().splitlines()
inst = []

lines = [(line.split(' ')[1], line.split(' ')[7]) for line in lines]

steps = set([s[0] for s in lines] + [s[1] for s in lines])


def next_step(steps, l):
    return [s for s in steps if all(b != s for (_, b) in l)]


order = ''
while steps:
cand = [s for s in steps if all(b != s for (_, b) in lines)]
cand.sort()
n = cand[0]
order += n
steps.remove(n)
lines = [(a, b) for (a, b) in lines if a != n]

print(order)