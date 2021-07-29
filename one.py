def check_progression(a_1, a_2, a_3):
    if a_1 - a_2 == a_2 - a_3:
        return "Yes"
    else:
        return "No"


number_of_sequence = int(input())

elements_in_seq = 3

result = []

for _ in range(number_of_sequence):
    sequence = []
    for index_of_element in range(elements_in_seq):
        sequence.append(int(input()))
    sorted_sequence = sorted(sequence)
    result.append(check_progression(sorted_sequence[0], sorted_sequence[1], sorted_sequence[2]))

for i in range(number_of_sequence):
    print(result[i])

