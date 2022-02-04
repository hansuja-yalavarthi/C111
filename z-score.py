import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0, 1000):
    setOfMeans = randomSetOfMean(100)
    mean_list.append(setOfMeans)
stdev = statistics.stdev(mean_list)
first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - (2 * stdev), mean + (2 * stdev)
third_stdev_start, third_stdev_end = mean - (3 * stdev), mean + (3 * stdev)

df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean_sample3 = statistics.mean(data)
print("Mean of sample 3: ", mean_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_sample3, mean_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_stdev_end, third_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
zScore=(mean-mean_sample3)/stdev
print("z-score is: ", zScore)