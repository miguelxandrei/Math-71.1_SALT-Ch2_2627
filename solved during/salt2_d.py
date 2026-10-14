T = int(input())

final_optimist = []
final_pessimist = []

for i in range(T):
    n = int(input())
    takaw = [int(x) for x in input().split()]

    takaw.sort()
    min_pairings = []

    for i in range(n):
        min_pairings.append(takaw[i] + takaw[2*n-i-1])

    final_optimist.append(max(min_pairings))
    final_pessimist.append(max(takaw)+max(takaw[:-1]))

for i in range(len(final_optimist)):
    print(final_optimist[i], final_pessimist[i])