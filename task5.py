from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: скільки хто витратив грошей

data = dict()
for car in list (dataset.keys()):
    for user in list(dataset[car].keys()):
        for price in dataset[car][user]['price']:
            if user in data:
                data[user] += price
            else:
                data[user] = price
print(data)

diagram = go.Pie(labels=list(data.keys()), values=list( data.values()))

plotly.offline.plot([diagram], filename='products.html')
