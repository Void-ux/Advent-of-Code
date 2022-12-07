def get_range(pair: str) -> range:
    lower_bound, upper_bound = pair.split('-')
    return range(int(lower_bound), int(upper_bound) + 1)


with open('2022/day_4.txt', 'r') as file:
    content = file.read()


c = 0
for ranges in content.split('\n'):
    pair_1, pair_2 = ranges.split(',')
    range_1, range_2 = get_range(pair_1), get_range(pair_2)
    if any(x.start <= y.start and x.stop >= y.stop for x, y in [(range_1, range_2), (range_2, range_1)]):
        c += 1

print(c)
