def parse(list):

    result = []

    for _ in list:
        if _ == "A":
            result.append(1)
        elif _ == "T" or _ == "J" or _ == "Q" or _ == "K":
            result.append(10)
        elif _ == "*":
            result.append(0)
        else:
            result.append(int(_))

    return result

def deparse(cards, card_values):

    result = []

    for i in range(n):
        if cards[i] == "*":

            if card_values[i] == 1:
                deparsed_card = "A"
            elif card_values[i] == 10:
                deparsed_card = "T"
            else:
                deparsed_card = card_values[i]
            
            result.append(str(deparsed_card))
        else:
            result.append(str(cards[i]))

    return result

n, m = [int(x) for x in input().split()]
cards = list(input())

card_values = parse(cards)
output = "NO"

if 1*cards.count("*") <= m-sum(card_values) <= 10*cards.count("*"):
    diff = m-sum(card_values)
    if cards.count("*") > 0:
        a = diff // cards.count("*")
        r = diff % cards.count("*")
    
        for i in range(n):
            if card_values[i] == 0:
                card_values[i] = a+1 if r > 0  else a
                if r > 0:
                    r -= 1
else:
    card_values.append(None)

if None in card_values or sum(card_values) != m:
    print(output)
else:
    output = "YES"
    print(output)
    print("".join(deparse(cards, card_values)))