from requests import get

with open('dataset_3378_3.txt') as inf:
    url = inf.readline().strip()

r = get(url)
line = r.text.strip()
while line[:2] != 'We':
    print(url)
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + line
    r = get(url)
    line = r.text.strip()

print(url)