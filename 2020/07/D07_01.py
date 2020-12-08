text = """light red bags contain 1 bright white bag, 2 muted yellow bags.
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

page = [line.split(' bags contain ') for line in page]

found_colors = set()
colors_to_check = ["shiny gold"]

while colors_to_check:
     color = colors_to_check.pop()
     for line in page:
          if color in line[1]:
               # print(color, '---->', line[1])
               if line[0] not in found_colors:
                    found_colors.add(line[0])
                    colors_to_check.append(line[0])
               else:
                    continue

print(len(found_colors))
