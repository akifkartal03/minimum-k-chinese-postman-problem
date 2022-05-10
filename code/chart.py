import matplotlib.pyplot as plt
from main import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my chart drawing
class MyChartDraw:
    def __init__(self):
        self.algo = MyAlgorithm()

    def time_vs_k(self):
        x = []
        y = []
        for i in range(5):
            if i == 0:
                time0 = self.algo.my_algorithm1(0, 2 + i, 7, 25 + i, True,True)
            else:
                time0 = self.algo.my_algorithm1(0, 2 + i, 7, 25 + i, False,True)
            x.append(2 + i)
            y.append(time0)

        print(x)
        print(y)

        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)

        # naming the x axis
        plt.xlabel('k')
        # naming the y axis
        plt.ylabel('Running Time(s)')

        # giving a title to my graph
        plt.title('Running time with respect to k')

        # function to show the plot
        plt.show()

    def time_vs_n(self):
        x = []
        y = []
        for i in range(5):
            time2 = self.algo.my_algorithm1(0, 3, 4 + i, 30 + i, True,True)
            x.append(4 + i)
            y.append(time2)

        print(x)
        print(y)

        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)

        # naming the x axis
        plt.xlabel('number of vertices')
        # naming the y axis
        plt.ylabel('Running Time(s)')

        # giving a title to my graph
        plt.title('Running time with respect to number of vertices')

        # function to show the plot
        plt.show()

    def max_length_vs_k(self):
        x = []
        y = []
        for i in range(5):
            if i == 0:
                time3 = self.algo.my_algorithm1(0, 2 + i, 7, 35 + i, True,False)
            else:
                time3 = self.algo.my_algorithm1(0, 2 + i, 7, 35 + i, False,False)
            x.append(2 + i)
            y.append(time3)

        print(x)
        print(y)

        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)

        # naming the x axis
        plt.xlabel('k')
        # naming the y axis
        plt.ylabel('Maximum length')

        # giving a title to my graph
        plt.title('Maximum length with respect to k')

        # function to show the plot
        plt.show()

    def max_length_vs_n(self):
        x = []
        y = []
        for i in range(5):
            time4 = self.algo.my_algorithm1(0, 3, 4+i, 40 + i, True,False)
            x.append(4 + i)
            y.append(time4)

        print(x)
        print(y)

        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)

        # naming the x axis
        plt.xlabel('number of vertices')
        # naming the y axis
        plt.ylabel('Maximum length')

        # giving a title to my graph
        plt.title('Maximum length with respect to number of vertices')

        # function to show the plot
        plt.show()

plot = MyChartDraw()
plot.time_vs_k()
plot.time_vs_n()
plot.max_length_vs_k()
plot.max_length_vs_n()