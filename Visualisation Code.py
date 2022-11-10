# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:49:40 2022

@author: Puneet
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import textwrap

# creating function to create a line graph
def line_p(x_axis, y_axis, name, col):
    plt.plot(x_axis,y_axis,label= name, color= col)

# Creating a function to create a pie chart with pie sub plot
def pie_p(y, label, ind):
    #Ind will be taken from the index of the rows
    plt.subplot(3,2,ind+1)
    plt.pie(y,labels = label, shadow= False, autopct="%2.1f%%",textprops={'fontsize': 6})
    plt.title(major["Major"][ind],fontsize = 6.2)

    #Creating a function for Bar plot
def bar_p(a, value1, value2, lab1, lab2):
    #placing values in barx and barx2 for width and length of a bar graph
    barx= np.arange(len(a))
    barx2= [i+w for i in barx]
    #Ploting 1st bar graph
    plt.bar(barx, value1,w,label=lab1)
    #Ploting 2nd bar graph
    plt.bar(barx2, value2,w,label=lab2)
    plt.xticks(barx,a)

#reading a Data set of a csv file
meat = pd.read_csv("C:/Users/Puneet/OneDrive - University of Hertfordshire/Applied DataScience 1/Assignment/Visualization 1/meat_consumption.csv")

#Droping Unwated Columns
meat= meat.drop(["Flag Codes","FREQUENCY",'INDICATOR'],axis=1)
#filtering data as requied
meat=meat[(meat["LOCATION"] == "GBR") & (meat["MEASURE"] == "THND_TONNE") & (meat["TIME"]>= 2005) & (meat["TIME"]<= 2010)]

meat_sheep = meat[(meat["SUBJECT"]=="SHEEP")]
meat_beef = meat[(meat["SUBJECT"]=="BEEF")] #sub dataframe for Beef
meat_poultry = meat[(meat["SUBJECT"]=="POULTRY")] #sub dataframe for Poultry
meat_pig = meat[(meat["SUBJECT"]=="PIG")] ##sub dataframe for Pig

#produsing a line graph  using a line_p function
#line_p(meat_sheep.TIME, meat_sheep.Value, "Sheep","blue")
line_p(meat_beef.TIME, meat_beef.Value, "Beef","red")
line_p(meat_poultry.TIME, meat_poultry.Value, "Poultry","green")
line_p(meat_pig.TIME, meat_pig.Value, "Pig","pink")
plt.xlabel("Years", size=12)
plt.ylabel("Tons", size=12)
plt.title("Meat consumption of Britain from 2005 to 2010")
plt.legend()

#reading a Data set of a csv file
major = pd.read_csv("C:/Users/Puneet/OneDrive - University of Hertfordshire/Applied DataScience 1/Assignment/Visualization 1/recent-grads.csv")
# selecting a data where major category is computers & Mathematics
major=(major.loc[major["Major_category"] == "Computers & Mathematics"])
#droping unwanted data's
major=major.drop(['Rank', "Major_category", 'ShareWomen', 'Sample_size', 'Unemployment_rate', 'Median', 'P25th', 'P75th', 'College_jobs', 'Non_college_jobs', 'Low_wage_jobs', 'Full_time_year_round'], axis=1)
major = (major.loc[major["Major_code"]<=2107])
major = (major.loc[major["Major_code"]>2001])
#Re-arranging the data
major = major.sort_values('Major_code', ascending=True)
#creating a new dataforame for Bar plot required coloumns)
employment = major[["Major_code","Employed", "Full_time", "Part_time", "Unemployed", ]]
employment.head()
#Selecting only required colums for pie chart
major = major[["Major","Men","Women"]]
#selecting a labels for pie chart
my_label = ["Men", "Women"]
#putting value of major to tit so we can use it in title of the pie chart
tit = major["Major"]
l = range(len(tit))
plt.figure(dpi=1080)
#reseting the index of the major dataform so we can use it in subplots of pie chart
major=major.reset_index()
major = major.drop(["index"],axis=1)
#itterating every index
for ind in major.index:
    #Creating a array so pie can be created based on row values
    y = np.array([major["Men"][ind],major["Women"][ind]])
    #Calling pie_p function
    pie_p(y,my_label,ind)
plt.show()



#Assigning a width of the bar plot to w
w=0.4
plt.figure(figsize=(15, 10))
#calling bar_p for creating bar function
bar_p(employment["Major_code"], employment["Employed"], employment["Unemployed"],'Employed Student', 'UnEmployed Student')
#Labeling the plot with required data
plt.xlabel("Major Code")
plt.ylabel("N")
plt.title("Employed Vs Unemployed Students")

plt.legend()
plt.show()






