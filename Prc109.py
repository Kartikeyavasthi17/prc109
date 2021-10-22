from logging import NullHandler
from os import name
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv 
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("Prc109.csv")
data=df["reading score"].tolist()

mean=statistics.mean(data)
stdDeviation=statistics.stdev(data)
mode=statistics.mode(data)
median=statistics.median(data)

first_std_deviation_start,first_std_deviation_end = mean-stdDeviation,mean+stdDeviation
second_std_deviation_start,second_std_deviation_end=mean-(2*stdDeviation),mean+(2*stdDeviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*stdDeviation),mean+(3*stdDeviation)

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

fig = ff.create_distplot([data],["reading score"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.show()

print("Mean of data is {}".format(mean))
print("The mode of data is {}".format(mode))
print("The median of data is {}".format(median))
print("Standard Deviation of data is {}".format(stdDeviation))
print("{}% of data lies within first standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))