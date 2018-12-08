from data import dataset

from task1 import *

import plotly
import plotly.graph_objs as go

#Вивести стовпчикову діаграму: скільки грошей витратили на кожну машину

data = dict()
for car in list (dataset.keys()):
    for user in list(dataset[car].keys()):
        for price_list in dataset[car][user]['price']:
            if car in data:
                data[car] += price_list
            else:
                data[car] = price_list

print(data)

diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
)

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='user expenses.html')