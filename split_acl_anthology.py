import os

# url = 'https://aclanthology.org/anthology.bib.gz'
# os.system(f'rm anthology.bib; rm anthology.bib.gz; wget {url}; gunzip anthology.bib.gz')


with open('anthology.bib') as f:
    text = f.read()

text = text[text.find('@'):]
text = text.replace('\n\n', '\n')
text = text.replace('\n\n', '\n')
text = text.replace('\n\n', '\n')
text = text.replace('\n\n', '\n')

text = text.replace('}\n@', '}@@@###===@')
items = text.split('@@@###===')

import collections

final_split = collections.defaultdict(list)
years = [str(x) for x in range(2030, 1950, -1)]
for item in items:
    lines = item.split('\n')
    matched = False
    for line in lines:
        if not matched and line.startswith('@'):
            for year in years:
                if not matched and year in line:
                    final_split[year].append(item)
                    matched = True
    if not matched:
        print('Cant find')
        print(item)
        print('-' * 120)

year_groups = [
    (1950, 2000),
    (2000, 2005),
    (2005, 2010),
    (2010, 2012),
    (2012, 2014),
    (2014, 2016),
    (2016, 2018),
    (2018, 2020),
    (2020, 2022),
    (2022, 2024),
    (2024, 2026),
]

for start, end in year_groups:
    group_bibs = []
    for year in range(start, end):
        d = final_split[str(year)]
        group_bibs += d
    print(start, end, len(group_bibs))

    with open(f'bibs/anthology.{start}.{end}.bib', 'w') as f:
        f.write('\n'.join(group_bibs))

if __name__ == '__main__':
    pass
