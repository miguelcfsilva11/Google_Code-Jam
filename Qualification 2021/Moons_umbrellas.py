def cost(alist, x, y):
    price = 0
    mural = "".join(alist)
    for letter in range(1, len(mural)):
        if mural[letter-1: letter+1] == "CJ":
            price += x
        elif mural[letter-1: letter+1] == "JC":
            price += y
    return price

t = int(input())
case = 1
while t > 0:
    alist = list(input().split(" "))
    x, y = int(alist[0]), int(alist[1])
    mural = [letter for letter in list(alist[2]) if letter != "?"]
    print(("Case #{0}: {1}").format(case, cost(mural, x, y)))
    case += 1
    t -= 1