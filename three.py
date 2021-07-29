def calculate_distance(point_i, point_j):
    return max(abs(point_i[0] - point_j[0]), abs(point_i[1] - point_j[1]))


number_of_point = int(input())

sequence_of_points = []

for _ in range(number_of_point):
    point = list(map(int, input().strip().split()))[:2]
    sequence_of_points.append(point)

sequence_of_distance = []

for i in range(number_of_point):
    for j in range(i + 1, number_of_point):
        sequence_of_distance.append(calculate_distance(sequence_of_points[i], sequence_of_points[j]))

sorted_sequence_of_distance = sorted(sequence_of_distance, reverse=True)

print(sorted_sequence_of_distance[1])
