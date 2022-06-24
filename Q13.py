# Q.13 - python lists

if __name__ == '__main__':
    N = int(input()) 
lst = []
for n in range(N):
    f = input() 
    l = f.split()
    if l[0] == 'insert':
        lst.insert(int(l[1]),int(l[2]))
        continue
    if l[0] == 'append':
        lst.append(int(l[1]))
        continue
    if l[0] == 'print':
        print(lst)
        continue
    if l[0] == 'remove':
        lst.remove(int(l[1]))
        continue
    if l[0] == 'sort':
        lst.sort()
        continue
    if l[0] == 'pop':
        lst.pop()
        continue
    if l[0] == 'reverse':
        lst.reverse()