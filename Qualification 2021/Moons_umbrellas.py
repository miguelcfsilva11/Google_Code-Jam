def cost(mural, x, y):

    if "?" not in mural:
        price = 0
        for letter in range(1, len(mural)):
            if mural[letter-1: letter+1] == "CJ":
                price += x
            elif mural[letter-1: letter+1] == "JC":
                price += y
        return price

    threshold = 1*10**6

    for pick in generate_pick(mural):
        future_price = cost(pick, x, y)
        if future_price < threshold:
            threshold = future_price

    return threshold


def generate_pick(mural):
    possible_picks = []
    for letter in range(len(mural)):
        if mural[letter] == "?":
            temp = list(mural)
            temp[letter] = "C"
            possible_picks.append("".join(temp))
            temp[letter] = "J"
            possible_picks.append("".join(temp))
    return possible_picks


t = int(input())
case = 1
while t > 0:
    alist = list(input().split(" "))
    x, y, mural = int(alist[0]), int(alist[1]), alist[2]
    print(("Case #{0}: {1}").format(case, cost(mural, x, y)))
    case += 1
    t -= 1