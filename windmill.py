from manim import *
class WillmildScene(Scene):
    CONFIG={
        'radius_dot':0.2
    }
    def construct(self):
        points=self.get_random_point(20)
        dots=self.get_dots(points)
        self.play(Create(dots))
        self.wait()
    def get_random_point(self,n_points):
        return np.array([[
            np.random.uniform(-config['frame_width'],config['frame_width']),
            np.random.uniform(-config['frame_height'],config['frame_height']),
            0
        ] for _ in range(n_points) ])
    def get_dots(self,points):
        return VGroup(*[
            Dot().move_to(point) for point in points
        ])