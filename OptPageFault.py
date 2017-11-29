import csv

with open('./test.csv') as f:
    _pages = csv.reader(f)
    for row in _pages:
        pages = row

print(pages, "/n")

output = []
index = 2
output = pages[:3]
pages = pages[3:]
for page in pages:
    if index == 2:
        index = 0
    print(page, index)
    if page in output:
        index += 1
        continue
    else:
        output[index] = page
        index += 1
    print(output)