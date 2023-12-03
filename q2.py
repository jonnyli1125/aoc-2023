import sys

def min_cubeset_power(line: str) -> int:
    _, draws = line.split(':', 1)
    draws = draws.strip().split(';')
    rgb_min = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for draw_details in draw.split(','):
            num, color = draw_details.strip().split()
            rgb_min[color] = max(rgb_min[color], int(num))
    return rgb_min['red'] * rgb_min['green'] * rgb_min['blue']

print(sum(min_cubeset_power(line) for line in sys.stdin))
