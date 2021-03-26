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


t = int(input())
case = 1
while t > 0:
    n = int(input())
    alist = list(map(int, input().split(" ")))
    print(("Case #{0}: {1}").format(case, reversort(alist)))
    case += 1
    t -= 1
