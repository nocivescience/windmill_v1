from manim import *
def get_random_point(n_points):
    return np.array([[
        np.random.uniform(-config['frame_width']/2-.5,config['frame_width']/2-.5),
        np.random.uniform(-config['frame_height']/2-.5,config['frame_height']/2-.5),
        0
    ] for _ in range(n_points) ])
def next_pivot_and_angle(points):
    pivot=points[np.random.randint(len(points))]
    non_pivot=list(filter(lambda t: not np.all(t==pivot),points))
    angles=np.array([
        -(angle_of_vector(point-pivot)%PI) for point in non_pivot
    ])
    return angles
points=get_random_point(20)
otro_dato=next_pivot_and_angle(points)
print(otro_dato)