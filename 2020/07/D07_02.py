import re

pattern = re.compile(r"[1-9]{1} \w+ \w+")

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


with open('input') as f:
     page = f.read().strip().splitlines()

# page = text2.strip().splitlines()
page = [line.split(' bags contain ') for line in page]

found_colors = set()
bags_to_check = ["1 shiny gold"]
suma = 0

while bags_to_check:
     bag_info = bags_to_check.pop().split(' ')
     num = int(bag_info[0])
     color = ' '.join([bag_info[1], bag_info[2]])

     for line in page:
          if color == line[0] and line[0] not in found_colors:
               contain_bags = re.findall(pattern, line[1])
               for bag in contain_bags:
                    bag = bag.split(' ')
                    total_num_bag = num * int(bag[0])
                    suma += total_num_bag
                    bag_to_check = ' '.join(
                         [str(total_num_bag), bag[1], bag[2]]
                         )
                    bags_to_check.append(bag_to_check)

     found_colors.add(color)

print(suma)
