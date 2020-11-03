n = int(input())
s = input()
print(len(s))
l = []
count_j = 0
count_a = 0
count_v = 0
count_p = 0
count_i = 0
for i in s:
    l.append(i)
if 'j' in s:
    for i in l:
        if i == 'j':
            count_j += 1
        elif i == 'a':
            count_a += 1
        elif i == 'v':
            count_v += 1
        elif i == 'p':
            count_p += 1
        elif i == 'i':
            count_i += 1
    count_a = count_a/2
    a = min(count_a,count_i,count_j,count_v,count_p)
    print(a)