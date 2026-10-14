keyboard = ""
for i in range(3):
    keyboard += input()

q = int(input())
str = [list(input()) for i in range(q)]

alphabet = list("QWERTYUIOPASDFGHJKLZXCVBNM")
letters = list(keyboard)

used_letters = []

for i in range(26):
    if letters[i] == "*":
        used_letters.append(alphabet[i])

result = "POSSIBLE"

for i in range(q):
    current_s = str[i]
    current_bank = used_letters.copy()

    for _ in used_letters:
        if _ in current_s:
            while current_s.count(_) > 0:
                current_s.remove(_)
            current_bank.remove(_)

    if len(current_s) > 0 or len(current_bank) > 0:
        result = "IMPOSSIBLE"

    print(result)

    result = "POSSIBLE"
