import itertools


def reversort(list):
    counter = 0
    altered = False
    for i in range(0, len(list)-1):
        threshold = list[i]
        for pos in range(i, len(list)):
            if list[pos] < threshold:
                altered = True
                j = pos
                threshold = list[pos]
        if altered:
            list[i:j+1] = list[i:j+1][::-1]
            counter += j-i + 1
        else:
            counter += 1
        altered = False
    return counter


def reversort_engineer(n, c):
    alist = []
    for element in range(0, n):
        alist.append(element+1)
    perms = list(itertools.permutations(alist, n))
    for choice in perms:
        if reversort(list(choice)) == c:
            return list(choice)
        
    return "IMPOSSIBLE"

t = int(input())
case = 1
while t > 0:
    n, c = map(int, input().split(" "))
    a = reversort_engineer(n, c)
    if a == "IMPOSSIBLE":
        print(("Case #{0}: {1}").format(case, reversort_engineer(n, c)))
    else:
        print(("Case #{0}: {1}").format(case, " ".join(map(str, (reversort_engineer(n, c))))))
    case += 1
    t -= 1