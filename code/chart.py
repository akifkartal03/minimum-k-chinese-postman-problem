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

    def print_chart(self, xlabel, ylabel, title, x1, y1, x2, y2, name):
        print("chart is printing...")
        print(x1)
        print(y1)
        print(x2)
        print(y2)

        x1i = list(range(len(x1)))

        # plotting the points
        plt.plot(x1i, y1, color='green', label="heuristic", linestyle='dashed',
                 marker='o', markerfacecolor='green')

        plt.plot(x1i, y2, color='red', label="exhausted search", linestyle='dashed',
                 marker='o', markerfacecolor='red')

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.xticks(x1i, x1)
        plt.title(title)

        plt.legend()
        plt.show()

    def time_max_vs_n(self, n, k, s, e):
        self.init_values1()
        missing = 0
        for i in range(20):
            self.algo.generate_graph(s, n, e, k, i)
            res = self.algo.my_algorithm(k)
            res2 = self.algo.simple_algo(k)
            cycles = res[0]
            cycles2 = res2[0]
            self.time1_sum = self.time1_sum + res[1]
            self.time2_sum = self.time2_sum + res2[1]
            if len(cycles) > 0 and len(cycles2) > 0:
                maxx = cycles[0]
                lenth = maxx['length']
                self.max1_sum = self.max1_sum + lenth
                missing = missing + 1
                maxx2 = cycles2[0]
                lenth2 = maxx2['length']
                self.max2_sum = self.max2_sum + lenth2

        self.time1_avg = self.time1_sum / 20.0
        self.max1_avg = self.max1_sum / float(missing)
        self.time2_avg = self.time2_sum / 20.0
        self.max2_avg = self.max2_sum / float(missing)

        print("missing")
        print(missing)

        self.time1_x.append(e)
        self.max1_x.append(e)
        self.time2_x.append(e)
        self.max2_x.append(e)

        self.time1_y.append(self.time1_avg)
        self.max1_y.append(self.max1_avg)
        self.time2_y.append(self.time2_avg)
        self.max2_y.append(self.max2_avg)

    def chart1_time_vs_n(self):
        # k ve edge count sabit n değişiyor
        # n = 4 ile 9 arasında
        # k = 3
        # edge = 6 , 9 ,11 ,13 ,15 şeklinde değişiyor
        # s = 0
        print("chart1")
        self.init_values2()
        for i in range(4, 8):
            if int((i * (i - 1)) / 2) < 10:
                edge = int((i * (i - 1)) / 2)
            elif int((i * (i - 1)) / 2) > 20:
                edge = 12
            elif 5 < int((i * (i - 1)) / 2) < 15:
                edge = int((i * (i - 1)) / 2) - 1
            else:
                edge = 10
            self.time_max_vs_n(i, 5, 0, edge)
        self.print_chart("number of vertices", "Running Time(s)",
                         "Running time with respect to number of vertices", self.time1_x, self.time1_y, self.time2_x,
                         self.time2_y, "charts/time.png")

    def chart1_time_vs_max(self):
        # k ve edge count sabit n değişiyor
        # n = 4 ile 9 arasında
        # k = 4
        # edge = 8
        # s = 0
        print("chart2")
        self.print_chart("number of vertices", "Maximum length",
                         "Maximum length with respect to number of vertices", self.max1_x, self.max1_y, self.max2_x,
                         self.max2_y, "charts/max.png")

    def chart2_time_vs_edge(self):
        # k ve n count sabit edge değişiyor
        # edge = 8 ile 12 arasında
        # k = 4
        # n = 5
        # s = 0
        print("chart1")
        self.init_values2()
        for i in range(7, 12):
            self.time_max_vs_n(6, 4, 0, i)
        self.print_chart("number of edges", "Running Time(s)",
                         "Running time with respect to number of edges", self.time1_x, self.time1_y, self.time2_x,
                         self.time2_y, "charts/time.png")

    def chart2_max_vs_edge(self):
        # k ve n count sabit edge değişiyor
        # edge = 8 ile 12 arasında
        # k = 4
        # n = 6
        # s = 0
        print("chart4")
        self.print_chart("number of edges", "Maximum length",
                         "Maximum length with respect to number of edges", self.max1_x, self.max1_y, self.max2_x,
                         self.max2_y, "charts/max.png")

    def chart3_time_vs_k(self):
        # k ve n count sabit edge değişiyor
        # edge = 8 ile 12 arasında
        # k = 4
        # n = 5
        # s = 0
        print("chart1")
        self.init_values2()
        for i in range(4, 9):
            self.time_max_vs_n(6, i, 0, 10)
        self.print_chart("k value", "Running Time(s)",
                         "Running time with respect to k value", self.time1_x, self.time1_y, self.time2_x,
                         self.time2_y, "charts/time.png")

    def chart3_max_vs_k(self):
        # k ve n count sabit edge değişiyor
        # edge = 8 ile 12 arasında
        # k = 4
        # n = 6
        # s = 0
        print("chart4")
        self.print_chart("k value", "Maximum length",
                         "Maximum length with respect to k value", self.max1_x, self.max1_y, self.max2_x,
                         self.max2_y, "charts/max.png")

    def time_max_vs_n_heuristic(self, n, k, s, e):
        self.init_values1()
        for i in range(50):
            self.algo.generate_graph(s, n, e, k, i)
            res = self.algo.simple_algo(k)
            self.time1_sum = self.time1_sum + res[1]
            cycles = res[0]
            if len(cycles) == 0:
                print("missing")

        self.time1_avg = self.time1_sum / 50.0
        self.time1_x.append(n)
        self.time1_y.append(self.time1_avg)

    def chart5_time_vs_n(self):
        # k ve edge count sabit n değişiyor
        # n = 4 ile 9 arasında
        # k = 3
        # edge = 6 , 9 ,11 ,13 ,15 şeklinde değişiyor
        # s = 0
        print("chart5")
        self.init_values2()
        for i in range(4, 7):
            if i == 4:
                edge = int((i * (i - 1)) / 2) - 1 #5
                k = 3
            elif i == 5:
                edge = int((i * (i - 1)) / 2) - 2 # 8
                k = 5
            elif i == 6:
                edge = int((i * (i - 1)) / 2) - 5 # 10
                k = 7
            else:
                edge = 5
                k = 4
            self.time_max_vs_n_heuristic(i, k, 0, edge)
        self.print_chart2("number of vertices", "Running Time(s)",
                          "Running time with respect to number of vertices", self.time1_x, self.time1_y)

    def print_chart2(self, xlabel, ylabel, title, x1, y1):
        print("chart is printing...")
        print(x1)
        print(y1)

        x1i = list(range(len(x1)))

        # plotting the points
        plt.plot(x1i, y1, color='green', label="exhausted search", linestyle='dashed',
                 marker='o', markerfacecolor='green')

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.xticks(x1i, x1)
        plt.title(title)

        plt.legend()
        plt.show()


plot = MyChartDraw()
plot.chart2_time_vs_edge()
plot.chart2_max_vs_edge()
# plot.chart1_time_vs_max()
# plot.chart2_time_vs_edge()
# plot.chart2_max_vs_edge()
# plot.chart3_time_vs_k()
# plot.chart3_max_vs_k()

"""
x1 = [4, 5, 6, 7, 8]
y1 = [0.0015796799999999943, 0.0011379750000000133, 0.0005795699999999515, 0.0010612999999999983, 0.001512065000000362]

x2 = [4, 5, 6, 7, 8]
y2 = [0.00360313000000001, 0.008309474999999988, 0.04434918499999998, 0.48101402999999976, 5.51165613]

x3 = [4, 5, 6, 7, 8]
y3 = [113.54545454545455, 103.22222222222223, 118.25, 148.94736842105263, 161.45]

x4 = [4, 5, 6, 7, 8]
y4 = [116.36363636363636, 103.61111111111111, 114.4, 101.57894736842105, 99.65]

plot.print_chart("number of edges", "Running Time(s)",
                         "Running time with respect to number of edges", x1, y1, x2,
                         y2,"charts/time.png")

plot.print_chart("number of edges", "Maximum length",
                 "Maximum length with respect to number of edges", x3, y3, x4, y4, "charts/max.png")

"""
