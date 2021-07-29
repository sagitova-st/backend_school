def func_polyndrom(initial_sequence, half_of_elements):
    counter = 0
    bad_subsequence = []
    for i in range(half_of_elements):
        if initial_sequence[i] == initial_sequence[len(initial_sequence) - i - 1]:
            counter += 1
        else:
            bad_subsequence.append(initial_sequence[i])
            bad_subsequence.append(initial_sequence[len(initial_sequence) - i - 1])

    if counter == half_of_elements:
        return 0
    else:
        unique_bad_subsequence = set(bad_subsequence)
        return int(len(unique_bad_subsequence) / 2 + 0.5)


number_of_elements = int(input())
sequence = list(map(int, input().strip().split()))[:number_of_elements]

print(func_polyndrom(sequence, int(number_of_elements/2)))
