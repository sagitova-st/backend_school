string_T = input()
string_S = input()

min_delta = len(string_S)

for i in range(len(string_T) - len(string_S) + 1):
    delta = 0
    for j in range(len(string_S)):
        delta += int(string_T[i + j] != string_S[j])
    min_delta = min(delta, min_delta)

print(min_delta)
