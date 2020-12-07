text = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
a = text.strip().split('\n\n')
a = [t.split('\n') for t in a]
print(a)
summary = 0
for groups in a:
    tmp_groups = []
    for grp in groups:
        tmp_groups.append(set(grp))
    print(tmp_groups[0].intersection(*tmp_groups[1:]))
    print(len(tmp_groups[0].intersection(*tmp_groups[1:])))
    summary += len(tmp_groups[0].intersection(*tmp_groups[1:]))

print(summary)
# ---------------------------------------------------------------
with open('input') as f:
    batch = f.read().strip().split('\n\n')

answers = [a.split('\n') for a in batch]

summary = 0
for groups in answers:
    tmp_groups = []
    for grp in groups:
        tmp_groups.append(set(grp))
    summary += len(tmp_groups[0].intersection(*tmp_groups[1:]))

print(summary)