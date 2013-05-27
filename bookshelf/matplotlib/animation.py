"""Animation with matplolib.
"""

import random

import matplotlib                                          #1
matplotlib.use('TkAgg')                                    #2
import matplotlib.pyplot as plt


class Residual(object):                                    #3
    """Generator for residual values.

    This somehow mimics the residual a solver for
    a system of equations would produce.
    """

    def __init__(self, start, limit):                      #4
        self.value = start
        self.limit = limit
        self.counter = 0
        self.done = False

    def __call__(self):                                    #5
        if self.done:
            return None                                    #6
        diff = random.random() * self.value                #7
        if self.counter == 2:                              #8
            self.value += diff
            self.counter = 0
        else:                                              #9
            self.value -= diff
            self.counter += 1
        if self.value <= self.limit:                       #10
            self.done = True
        return self.value


class ResidualGraph(object):                               #11
    """Semilog plot with matplotlib.

    This plot is updated for every calculation time step.
    Therefore it grows dynamically.
    """

    def __init__(self, start):
        # make a figure
        self.fig = plt.figure()                            #12
        self.axes = self.fig.add_subplot(111)              #13
        self.counter = 0                                   #14
        self.x = [self.counter]                            #15
        self.y = [start]                                   #16
        self.show_initial_graph()                          #17
        self.window = plt.get_current_fig_manager().window #18

    def show_initial_graph(self):
        """Show a first version of the graph without calculated residuals.
        """
        self.axes.semilogy(self.x, self.y)                 #19
        self.axes.set_title('Solver test program')
        self.axes.set_xlabel('Number of steps')
        self.axes.set_ylabel('Nonlinear residual')
        self.fig.canvas.draw()                             #20

    def update(self, value):                               #21
        """Redraw the graph with an added value for the residual.
        """
        self.counter += 1                                  #22
        self.x.append(self.counter)                        #23
        self.y.append(value)                               #24
        plt.semilogy(self.x, self.y, color='blue')         #25
        plt.draw()                                         #26


def start_animation(start, limit):                         #27
    """Start the animation.
    """

    def animate():                                         #28
        """Animation function will be called by GUI library (Tkinter).
        """
        residual = get_residual()                          #29
        # show value and update graph
        if residual is not None:                           #30
            graph.window.after(1000, animate)              #31
            print residual
            graph.update(residual)                         #32
        else:
            print 'done'                                   #33
    get_residual = Residual(start, limit)                  #34
    graph = ResidualGraph(start)                           #35
    graph.window.after(300, animate)                       #36
    plt.show()                                             #37

if __name__ == '__main__':

    start_animation(1e4, 1e-7)                             #38
