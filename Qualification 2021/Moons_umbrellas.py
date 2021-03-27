def cost(mural, x, y):
    price = 0
    for letter in range(1, len(mural)):
        if mural[letter-1: letter+1] == "CJ":
            price += x
        elif mural[letter-1: letter+1] == "JC":
            price += y
    return price


def generate_pick(mural, x, y):

    aux = set()
    altered = False
    
    for state in mural:
        for letter in range(len(state)):
            if state[letter] == "?":
                altered = True
                temp = list(state)
                temp[letter] = "C"
                aux.add("".join(temp))
                temp[letter] = "J"
                aux.add("".join(temp))

    if altered:
        return generate_pick(aux, x, y)  
    return min([cost(state,x,y) for state in mural])


t = int(input())
case = 1
while t > 0:
    alist = list(input().split(" "))
    mural = set()
    mural.add(alist[2])
    x, y = int(alist[0]), int(alist[1])
    print(("Case #{0}: {1}").format(case, generate_pick(mural, x, y)))
    case += 1
    t -= 1