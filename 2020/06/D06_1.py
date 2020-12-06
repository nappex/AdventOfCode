with open('input') as f:
    batch = f.read().strip().split('\n\n')


answers = [a.replace('\n', '') for a in batch]
count_answ = [len(set(a)) for a in answers]
print(sum(count_answ))