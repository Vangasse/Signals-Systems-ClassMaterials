from manim import *
import numpy as np

class TimeShift(Scene):
    def construct(self):

        ax=Axes(x_range=[-3,3,1], y_range=[-2,2,1], 
                x_axis_config={"numbers_to_include": np.arange(-3,3,1)}, 
                y_axis_config={"numbers_to_include": [-1, 1]})
        ax_labels = ax.get_axis_labels()

        w = 2*np.pi
        phase = 0
        sin_graph = ax.plot(lambda x: np.sin(w*x + phase), color=BLUE)
        sin_label = ax.get_graph_label(sin_graph[0], label="\\sin(\omega x + \phi)", 
                                       x_val=-3, direction=UP*7)
        
        delayed_sin_graph = []
        delayed_sin_label = []
        for phase in np.linspace(0, np.pi/2, 30):
            delayed_sin_graph.append(ax.plot(lambda x: np.sin(w*x + phase), color=RED))
            delayed_sin_label.append(ax.get_graph_label(delayed_sin_graph[0], 
                                                        label="\\sin(\omega x + {:.2f}".format(phase) + ")", 
                                                        x_val=3, direction=DOWN*13))
        
        ax_group=VGroup(ax, ax_labels)
        
        self.play(Create(ax_group), run_time=.5)
        self.wait()
        self.play(Write(sin_label))
        self.play(Create(sin_graph), run_time=1)
        self.wait()
        self.play(Write(delayed_sin_label[0]))
        self.play(Create(delayed_sin_graph[0]), run_time=1)
        for i in range(1, len(delayed_sin_graph)):
            self.play(
                ReplacementTransform(delayed_sin_graph[i-1], delayed_sin_graph[i]),
                FadeTransform(delayed_sin_label[i-1], delayed_sin_label[i]),
                run_time=.1
            )