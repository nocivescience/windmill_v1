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
        next_pivot,angle=self.next_pivot_and_angle(line)
        #los self plays
        for mob in [dots,line,pivot_dot]:
            self.play(Create(mob))
        self.play(*[Rotate(
            line,-.99*angle,about_point=next_pivot,rate_func=linear
        )])
        self.rotate_to_next_pivot(line)
        self.get_let_windmill_run(line,1)
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
    def get_windmill(self,points,pivot=None,angle=TAU/8):
        line=Line(LEFT,RIGHT)
        line.set_angle(angle)
        line.set_length(2*config['frame_width'])
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
    def next_pivot_and_angle(self,windmill):
        curr_angle=windmill.get_angle()
        pivot=windmill.pivot
        non_pivots=list(filter(lambda t: not np.all(t==pivot), windmill.points_set))
        angles=np.array([
            -(angle_of_vector(point-pivot)-curr_angle)%PI for point in non_pivots
        ])
        index=np.argmin(angles)
        return non_pivots[index], angles[index]
    def rotate_to_next_pivot(self,windmill,max_time=None,added_anims=None):
        new_pivot,angle=self.next_pivot_and_angle(windmill=windmill)
        change_pivot_at_end=True
        if added_anims is None:
            added_anims=[]
        run_time=angle/windmill.rot_speed
        self.play(Rotate(windmill,about_point=new_pivot,angle=-angle,run_time=run_time))
        return run_time
    def get_let_windmill_run(self,windmill,time=0):
        while time<10:
            my_time=1
            last_run_time=self.rotate_to_next_pivot(windmill=windmill,max_time=my_time)
            time+=my_time