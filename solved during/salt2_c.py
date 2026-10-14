checkpoint_money = [int(x) for x in input().split()]
proj_cost = [int(x) for x in input().split()]

purse_money = checkpoint_money[-1]
can_afford = False

for cost in proj_cost:
    if cost > 0:
        purse_money += cost
        can_afford = True

if not can_afford:
    max_purse = -1
    for cost in proj_cost:
        price = -cost
        if purse_money >= price:
            current = purse_money + cost
            if current > max_purse:
                max_purse = current
    purse_money = max_purse

print(purse_money)