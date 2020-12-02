from itertools import combinations
from functools import reduce
from operator import mul


with open('input') as file:
    ex_report = [int(line) for line in file]


doubles = combinations(ex_report, 2)
triples = combinations(ex_report, 3)


def get_mul_entries(iterable):
    for nums in iterable:
        if sum(nums) == 2020:
            return reduce(mul, nums)


print(get_mul_entries(doubles))
print(get_mul_entries(triples))
