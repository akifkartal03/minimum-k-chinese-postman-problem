import matplotlib.pyplot as plt
from main import *


# I didn't want to bother with global variables therefore,
# I created a class to encapsulate my chart drawing
class MyChartDraw:

    def __init__(self):
        self.algo = MyAlgorithm()
        self.time_x = []
        self.time_y = []
        self.max_x = []
        self.max_y = []
        self.time_sum = 0
        self.max_sum = 0
        self.time_avg = 0
        self.max_avg = 0

    def init_values1(self):

        self.time_sum = 0
        self.max_sum = 0
        self.time_avg = 0
        self.max_avg = 0

    def init_values2(self):

        self.time_x = []
        self.time_y = []
        self.max_x = []
        self.max_y = []
        self.time_sum = 0
        self.max_sum = 0
        self.time_avg = 0
        self.max_avg = 0

    def print_chart(self,xlabel,ylabel,title,x,y):
        print("chart is printing...")
        print(x)
        print(y)

        # plotting the points
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=12)

        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.title(title)

        plt.show()

    def time_max_vs_n(self,n,k,s,e):
        self.init_values1()
        missing = 0
        for i in range(50):
            self.algo.generate_graph(s,n,e,k,i)
            res = self.algo.my_algorithm(k)
            self.time_sum = self.time_sum + res[1]
            cycles = res[0]
            if len(cycles) > 0:
                maxx = cycles[0]
                lenth = maxx['length']
                self.max_sum = self.max_sum + lenth
                missing = missing+1
        self.time_avg = self.time_sum / 50.0
        self.max_avg = self.max_sum / float(missing)

        self.time_x.append(n)
        self.max_x.append(n)

        self.time_y.append(self.time_avg)
        self.max_y.append(self.max_avg)

    def chart1_time_vs_n(self):
        # k ve edge count sabit n değişiyor
        # n = 5 ile 9 arasında
        # k = 3
        # edge = 8
        # s = 0
        print("chart1")
        self.init_values2()
        for i in range(5,9):
            self.time_max_vs_n(i,3,0,10)
        self.print_chart("number of vertices","Running Time(s)",
                         "Running time with respect to number of vertices",self.time_x,self.time_y)

    def chart2_time_vs_max(self):
        # k ve edge count sabit n değişiyor
        # n = 5 ile 9 arasında
        # k = 3
        # edge = 8
        # s = 0
        print("chart2")
        self.print_chart("number of vertices","Maximum length",
                         "Maximum length with respect to number of vertices",self.max_x,self.max_y)

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
#plot.time_vs_k()
plot.chart1_time_vs_n()
plot.chart2_time_vs_max()
#plot.max_length_vs_k()
#plot.max_length_vs_n()