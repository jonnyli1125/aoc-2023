import sys
from collections import defaultdict

lines = sys.stdin.readlines()

part_nums = {}
gear_conns = defaultdict(set)

def check_adj_symbols(i: int, j: int, n: int) -> None:
    for ai in [i-1, i, i+1]:
        if ai < 0 or ai >= len(lines):
            continue
        for aj in range(j-1, j+n+1):
            if aj < 0 or aj >= len(lines[ai]) - 1:
                continue
            if lines[ai][aj] == '*':
                gear_conns[(ai, aj)].add((i, j))

for i, line in enumerate(lines):
    num = ''
    for j, c in enumerate(line):
        if not c.isdigit():
            if not num:
                continue
            point = (i, j-len(num))
            part_nums[point] = int(num)
            check_adj_symbols(*point, len(num))
            num = ''
        else:
            num += c

def power(conns: set[tuple[int, int]]) -> int:
    val = 1
    for point in conns:
        val *= part_nums[point]
    return val

print(sum(power(conns) for conns in gear_conns.values() if len(conns) == 2))
