total_slimes = int(input())
size_slimes = [int(n) for n in input().split()]
cost = 0
max = 0

for i in size_slimes:
    max += i
    cost += i*i
    min_cost = (max**2 - cost) // 2
print(f"{max} {min_cost}")

