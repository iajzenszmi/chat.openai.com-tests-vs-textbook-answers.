import math

def distance_3d(p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    z_diff = p2[2] - p1[2]
    distance = math.sqrt(x_diff**2 + y_diff**2 + z_diff**2)
    return distance

p1 = (2, 3, 4)
p2 = (6, 9, 12)

distance = distance_3d(p1, p2)
print(f"The distance between the two points is approximately {distance:.5f} units.")


