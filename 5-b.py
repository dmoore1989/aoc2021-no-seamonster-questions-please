f = open("5in.txt", "r")
output = f.readlines()
points = set()
seen_points = set()
count = 0
for segments in output:
    segment_li = segments.split(' -> ')
    start = segment_li[0].split(',')
    start[0] = int(start[0])
    start[1] = int(start[1])
    end = segment_li[1].split(',')
    end[0] = int(end[0])
    end[1] = int(end[1])
    if start[0] == end[0]:
        iterator = 1 if end[1] > start[1] else -1
        for y_points in range(start[1], end[1] + iterator, iterator):
            coordinate_string = str(start[0]) + ',' + str(y_points)
            # print(coordinate_string)
            if coordinate_string in points and coordinate_string not in seen_points:
                count += 1
                seen_points.add(coordinate_string)
            else:
                points.add(coordinate_string)
    elif start[1] == end[1]:
        iterator = 1 if end[0] > start[0] else -1
        for x_points in range(start[0], end[0] + iterator, iterator):
            coordinate_string = str(x_points) + ',' + str(start[1])
            # print(coordinate_string)
            if coordinate_string in points and coordinate_string not in seen_points:
                count += 1
                seen_points.add(coordinate_string)
            else:
                points.add(coordinate_string)
    else:
        x_iterator = 1 if end[0] > start[0] else -1
        y_iterator = 1 if end[1] > start[1] else -1
        y_point = start[1]
        for x_points in range(start[0], end[0] + x_iterator, x_iterator):
            coordinate_string = str(x_points) + ',' + str(y_point)
            # print(coordinate_string)
            if coordinate_string in points and coordinate_string not in seen_points:
                count += 1
                seen_points.add(coordinate_string)
            else:
                points.add(coordinate_string)
            y_point += y_iterator
# print(points)
print(count)