from manim import *
import numpy as np

class Sinusoidal(Scene):
    def construct(self):
        ax=Axes(x_range=[-10,10,1], y_range=[-2,2,1], 
                x_axis_config={"numbers_to_include": np.arange(-9,9,2)}, 
                y_axis_config={"numbers_to_include": [-1, 1]})
        ax_labels = ax.get_axis_labels()

        period_dot = Dot(ax.coords_to_point(np.pi, 0), fill_color=BLUE, stroke_width=2, stroke_color=WHITE)
        period_label = Tex("$T_0$").scale(0.75).next_to(ax.c2p(np.pi, .25, 0))

        sin_graph = []
        for period in np.linspace(2*np.pi, np.pi, 60):
            sin_graph.append(ax.plot(lambda x: np.sin(2*np.pi*x/period), color=BLUE))
        sin_label = ax.get_graph_label(sin_graph[0], label="\\sin(x)", 
                                    x_val=-9, direction=UP*6)
        
        ax_group=VGroup(ax, ax_labels)
        
        self.play(Create(ax_group), run_time=.1)
        self.wait()
        self.play(Write(sin_label))
        self.play(Create(sin_graph[0]), run_time=.1)
        self.wait()
        self.play(Create(period_dot), run_time=.1)
        self.wait()
        self.play(Write(period_label), run_time=.1)
        self.wait()
        for i in range(1, len(sin_graph)):
            self.play(
                ReplacementTransform(sin_graph[i-1], sin_graph[i]),
                run_time=.1
            )