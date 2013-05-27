"""A simple stacked plot.
"""

import matplotlib as mpl                                              #1
import matplotlib.pyplot as plt                                       #2
import numpy                                                          #3

# PyLint doesn't find numpy members.
# pylint: disable-msg=E1101


class StackPlot(object):                                              #4
    """A stacked plot.

    Data are stacked on top of each other and the space
    between the lines is filled with color.
    """

    def __init__(self, x, y_data, axes=None, colors=None, names=None,
                 loc='best'):                                         #5
        """Show the plot.
        """
        # We've got plenty of default arguments.
        # pylint: disable-msg=R0913
        # Make sure we can work with numpy arrays.
        self.x = numpy.array(x)                                       #6
        self.y_data = numpy.array(y_data)
        self.axes = axes
        if not axes:
            self.axes = plt.gca()                                     #7
        default_colors = ['r', 'b', 'g', 'y', 'm', 'w']               #8
        self.colors = colors
        self.names = names
        self.loc = loc
        if not self.colors:                                           #9
            # Repeat colors as needed.
            ncolors = len(self.y_data)
            colors = default_colors * (1 + (ncolors // len(default_colors)))
            self.colors = colors[:ncolors]
        self.stacked = None
        self._stack_data()

    def _stack_data(self):                                            #10
        """Accumulate data.
        """
        nlines = self.y_data.shape[0] + 1                             #11
        self.stacked = numpy.zeros((nlines, self.y_data.shape[1]))    #12
        for index in xrange(1, nlines):
            self.stacked[index] = (self.stacked[index - 1] +           #13
                                   self.y_data[index - 1])

    def draw(self):                                                   #14
        """Draw the plot.
        """
        for data1, data2, color in zip(self.stacked[:-1], self.stacked[1:],
                                       self.colors):                  #15
            self.axes.fill_between(self.x, data1, data2, color=color) #16
            self.axes.plot(self.x, data2, 'k', linewidth=0.1)         #17
        if self.names:
            rects = []
            for color in self.colors:                                 #18
                rects.append(plt.Rectangle((0, 0), 1, 1, fc=color))
            self.axes.legend(rects, self.names, loc=self.loc,
                       prop=mpl.font_manager.FontProperties(size=10))

    def __getattr__(self, name):                                      #19
        """Delegate not found attributes to axes.

        This works for set_tile, set_xlabel etc.
        """
        try:
            return getattr(self.axes, name)
        except AttributeError:
            raise AttributeError("'StackPlot' object has no attribute '%s'"
                                 % name)


if __name__ == '__main__':

    def test():                                                       #20
        """Check if it works.
        """
        x = range(10)                                                 #21
        y_data = numpy.ones((5, 10), dtype=numpy.float)               #22
        y_data[1, 1] = 2
        y_data[2, 1] = 2
        y_data[3, 1] = 2
        y_data[1, 2] = 0.5
        y_data[2, 3] = 0.5
        y_data[3, 4] = 0.5
        fig = plt.figure()
        s_plot = StackPlot(x, y_data,
                           axes=fig.add_subplot(111),                 #23
                           names=['a', 'b', 'c', 'd', 'e'])
        s_plot.set_title('My Stacked Plot')                           #24
        s_plot.set_xlabel('x')
        s_plot.set_ylabel('y')
        s_plot.draw()                                                 #25
        plt.show()                                                    #26

    test()
