

number_of_incidents = int(input())

description_of_incidents = list(map(int, input().strip().split()))[:number_of_incidents]

probability = 1 / number_of_incidents

expected_value_sequence = []

for i in range(number_of_incidents):
    sum_of_expected_value = 0
    for j in description_of_incidents:
        sum_of_expected_value += description_of_incidents[i]/2 + j - min(description_of_incidents[i], j)
    expected_value_sequence.append(sum_of_expected_value)

sorted_expected_value_sequence = sorted(expected_value_sequence)

print(sorted_expected_value_sequence[0] * probability)
