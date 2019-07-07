import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def PlotFP(plt, titleName,aCenter, bCenter,cCenter, minValue, maxValue):
    xLow = [minValue, aCenter,bCenter]
    yLow = [1,1,0]
    xMiddle = [aCenter,bCenter,cCenter]
    yMiddle = [0, 1, 0]
    xHeight = [bCenter,cCenter,maxValue]
    yHeight = [0, 1, 1]
    plt.title(titleName)
    plt.plot(xLow, yLow, label="Low", marker='o', markerfacecolor='#FD380E', markersize=6, color='#FF5733')#red color
    plt.plot(xMiddle, yMiddle, label="Middle", marker='o', markerfacecolor='#FDEA07', markersize=6, color='#F9EC59')#yelow color
    plt.plot(xHeight, yHeight,label="Height", marker='o', markerfacecolor='#12F908', markersize=6, color='#60F959')#grean color
    plt.legend()
    return plt
def PlotFP(plt, lingVar):
    xLow = [lingVar.terms[0].a, lingVar.terms[0].b,lingVar.terms[0].c]
    yLow = [1,1,0]
    xMiddle = [lingVar.terms[1].a, lingVar.terms[1].b,lingVar.terms[1].c]
    yMiddle = [0, 1, 0]
    xHeight = [lingVar.terms[2].a, lingVar.terms[2].b,lingVar.terms[2].c]
    yHeight = [0, 1, 1]
    plt.title(lingVar.Name)
    plt.plot(xLow, yLow, label="Low", marker='o', markerfacecolor='#FD380E', markersize=6, color='#FF5733')#red color
    plt.plot(xMiddle, yMiddle, label="Middle", marker='o', markerfacecolor='#FDEA07', markersize=6, color='#F9EC59')#yelow color
    plt.plot(xHeight, yHeight,label="Height", marker='o', markerfacecolor='#12F908', markersize=6, color='#60F959')#grean color
    plt.legend()
    return plt