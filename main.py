import csv
import pandas as pd
import plotly.figure_factory as ff 
import statistics
import plotly.graph_objects as go
import random

df=pd.read_csv("medium_data.csv")
rtime=df["reading_time"].tolist()

def randomSetOfData(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(rtime)-1)
        value=rtime[randomIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return(mean)

meanList=[]
for i in range(0,1000):

    setOfMeans=randomSetOfData(100)
    meanList.append(setOfMeans)

mean=statistics.mean(meanList)
meanListStdev=statistics.stdev(meanList)
populationMean=statistics.mean(rtime)
populationStdev=statistics.stdev(rtime)
print(mean)
print(meanListStdev)
print(populationMean)
print(populationStdev)

ztest1=(mean-populationMean)/populationStdev
print(ztest1)
