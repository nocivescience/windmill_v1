from manim import *
class WindmilldScene(Scene):
    CONFIG={
        'radius_dot':0.2
    }
    def construct(self):
        ##los mobs
        points=self.get_random_point(20)
        dots=self.get_dots(points)
        line=self.get_windmill(points)
        pivot_dot=self.get_pivot_dot(line)
        #los self plays
        for mob in [dots,line,pivot_dot]:
            self.play(Create(mob))
        self.wait()
    def get_random_point(self,n_points):
        return np.array([[
            np.random.uniform(-config['frame_width']/2-.5,config['frame_width']/2-.5),
            np.random.uniform(-config['frame_height']/2-.5,config['frame_height']/2-.5),
            0
        ] for _ in range(n_points) ])
    def get_dots(self,points):
        return VGroup(*[
            Dot().move_to(point) for point in points
        ])
    def get_windmill(self,points,pivot=None,angle=TAU/4):
        line=Line(LEFT,RIGHT)
        line.set_angle(angle)
        line.set_length=2*config['frame_width']
        line.points_set=points
        if pivot is not None:
            line.pivot=pivot
        else:
            line.pivot=points[0]
        line.rot_speed=2
        line.add_updater(lambda t: t.move_to(t.pivot))    
        return line
    def get_pivot_dot(self,windmill,color=ORANGE):
        pivot_dot=Dot(color=color,radius=0.08)
        pivot_dot.set_z_index(20)
        pivot_dot.add_updater(lambda t: t.move_to(windmill.pivot))
        return pivot_dot
    