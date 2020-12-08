import re

text2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

text1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

def format_bag_rule(rule):
     bag_total, *bag_color = rule.split(' ')
     return int(bag_total), ' '.join(bag_color)


with open('input') as f:
     rules = f.read().strip().splitlines()


# rules = text2.strip().splitlines()
rules = [rule.split(' bags contain ') for rule in rules]


inner_bag_pattern = re.compile(r"[1-9]{1} \w+ \w+")
bags_to_check = ["1 shiny gold"]
suma = 0

while bags_to_check:
     bag_info = bags_to_check.pop()
     bag_total, bag_color = format_bag_rule(bag_info)

     for rule in rules:
          outer_bag, inner_bags = rule

          if bag_color == outer_bag:

               for bag in re.findall(inner_bag_pattern, inner_bags):
                    num, color = format_bag_rule(bag)
                    total_num_bag = bag_total * int(num)
                    suma += total_num_bag
                    bag_to_check = ' '.join([str(total_num_bag), color])
                    bags_to_check.append(bag_to_check)


print(suma)
