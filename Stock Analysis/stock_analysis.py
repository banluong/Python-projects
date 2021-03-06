
# coding: utf-8

# In[42]:

from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file

start=datetime.datetime(2015,11,1)
end=datetime.datetime(2016,3,10)

df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)

#Creates Status column returning values with function
def inc_dec(c,o):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]

df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)

p=figure(x_axis_type='datetime',width=1000,height=300,responsive=True)
p.title.text="Candlestick chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

#The high-low line
p.segment(df.index,df.High,df.index,df.Low,color="black")

#abs returns the absolute value
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],hours_12,
       df.Height[df.Status=="Increase"],fill_color="#00FF7F",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],hours_12,
       df.Height[df.Status=="Decrease"],fill_color="#FF0000",line_color="black")



output_file("CS.html")
show(p)


# In[ ]:



