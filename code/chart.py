import matplotlib.pyplot as plt
from main import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my chart drawing
class MyChartDraw:

    def __init__(self):
        self.algo = MyAlgorithm()
        self.time1_x = []
        self.time1_y = []
        self.max1_x = []
        self.max1_y = []
        self.time1_sum = 0
        self.max1_sum = 0
        self.time1_avg = 0
        self.max1_avg = 0

        self.time2_x = []
        self.time2_y = []
        self.max2_x = []
        self.max2_y = []
        self.time2_sum = 0
        self.max2_sum = 0
        self.time2_avg = 0
        self.max2_avg = 0

    def init_values1(self):

        self.time1_sum = 0
        self.max1_sum = 0
        self.time1_avg = 0
        self.max1_avg = 0

        self.time2_sum = 0
        self.max2_sum = 0
        self.time2_avg = 0
        self.max2_avg = 0

    def init_values2(self):

        self.time1_x = []
        self.time1_y = []
        self.max1_x = []
        self.max1_y = []
        self.time1_sum = 0
        self.max1_sum = 0
        self.time1_avg = 0
        self.max1_avg = 0

        self.time2_x = []
        self.time2_y = []
        self.max2_x = []
        self.max2_y = []
        self.time2_sum = 0
        self.max2_sum = 0
        self.time2_avg = 0
        self.max2_avg = 0

    def print_chart(self, xlabel, ylabel, title, x1, y1, x2, y2,name):
        print("chart is printing...")
        print(x1)
        print(y1)
        print(x2)
        print(y2)

        # plotting the points
        plt.plot(x1, y1, color='green', label="heuristic")

        plt.plot(x2, y2, color='red', label="exhausted search")

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.title(title)

        plt.legend()
        plt.show()
        plt.savefig(name)

    def time_max_vs_n(self, n, k, s, e):
        self.init_values1()
        missing = 0
        for i in range(30):
            self.algo.generate_graph(s, n, e, k, i)
            res = self.algo.my_algorithm(k)
            res2 = self.algo.simple_algo()
            cycles = res[0]
            cycles2 = res2[0]
            if len(cycles) > 0 and len(cycles2) > 0:
                maxx = cycles[0]
                lenth = maxx['length']
                self.max1_sum = self.max1_sum + lenth
                missing = missing + 1
                maxx2 = cycles2[0]
                lenth2 = maxx2['length']
                self.max2_sum = self.max2_sum + lenth2
                self.time1_sum = self.time1_sum + res[1]
                self.time2_sum = self.time2_sum + res2[1]
        self.time1_avg = self.time1_sum / float(missing)
        self.max1_avg = self.max1_sum / float(missing)
        self.time2_avg = self.time2_sum / float(missing)
        self.max2_avg = self.max2_sum / float(missing)

        print("missing")
        print(missing)

        self.time1_x.append(n)
        self.max1_x.append(n)
        self.time2_x.append(n)
        self.max2_x.append(n)

        self.time1_y.append(self.time1_avg)
        self.max1_y.append(self.max1_avg)
        self.time2_y.append(self.time2_avg)
        self.max2_y.append(self.max2_avg)

    def chart1_time_vs_n(self):
        # k ve edge count sabit n değişiyor
        # n = 5 ile 9 arasında
        # k = 3
        # edge = 8
        # s = 0
        print("chart1")
        self.init_values2()
        for i in range(4, 9):
            if int((i*(i-1)) / 2) < 13:
                edge = int((i*(i-1)) / 2) - 1
            else:
                edge = 12
            self.time_max_vs_n(i, 3, 0, edge)
        self.print_chart("number of vertices", "Running Time(s)",
                         "Running time with respect to number of vertices", self.time1_x, self.time1_y, self.time2_x,
                         self.time2_y,"charts/time.png")

    def chart2_time_vs_max(self):
        # k ve edge count sabit n değişiyor
        # n = 5 ile 9 arasında
        # k = 3
        # edge = 8
        # s = 0
        print("chart2")
        self.print_chart("number of vertices", "Maximum length",
                         "Maximum length with respect to number of vertices", self.max1_x, self.max1_y, self.max2_x,
                         self.max2_y,"charts/max.png")

    def time_vs_k(self):
        x = []
        y = []
        for i in range(5):
            if i == 0:
                time0 = self.algo.my_algorithm1(0, 2 + i, 7, 25 + i, True, True)
            else:
                time0 = self.algo.my_algorithm1(0, 2 + i, 7, 25 + i, False, True)
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

    def max_length_vs_k(self):
        x = []
        y = []
        for i in range(5):
            if i == 0:
                time3 = self.algo.my_algorithm1(0, 2 + i, 7, 35 + i, True, False)
            else:
                time3 = self.algo.my_algorithm1(0, 2 + i, 7, 35 + i, False, False)
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
            time4 = self.algo.my_algorithm1(0, 3, 4 + i, 40 + i, True, False)
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
# plot.time_vs_k()
plot.chart1_time_vs_n()
plot.chart2_time_vs_max()
# plot.max_length_vs_k()
# plot.max_length_vs_n()
