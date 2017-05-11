
# coding: utf-8

# In[87]:

import requests
from bs4 import BeautifulSoup

r=requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

len(all)

all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
#type is string, replace function removes \n and blace space

page_nr=soup.find_all("a",{"class":"Page"})[-1].text


# In[51]:

#loop to extract house prices
for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    
    #No. of beds
    #Try and except here because first house has 0 or unknown beds
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        print(None)
    
    #Square feet
    try:
        print(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        print(None)
    
    #Full baths
    try:
        print(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        print(None)
    
    #Half baths
    try:
        print(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        print(None)
        
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        #print(column_group)
        #Feature loop
        for feature_group,feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            #print(feature_group.text,feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    
    print(" ")


# In[88]:

#Creating dictionary and dataframe
#loop to extract house prices

#Grabs source code for three pages of house data

l=[] #The dictionary list
base_url="http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page)+".html")
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})

    
    for item in all:
        d={}
        d["Address"]=item.find_all("span",{"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"]=item.find_all("span",{"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"]=None
        d["Price"]=item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")

        #No. of beds
        #Try and except here because first house has 0 or unknown beds
        try:
            d["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            d["Beds"]=None

        #Square feet
        try:
            d["Area"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            d["Area"]=None

        #Full baths
        try:
            d["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"]=None

        #Half baths
        try:
            d["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            #print(column_group)
            #Feature loop
            for feature_group,feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                #print(feature_group.text,feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text

        l.append(d)


# In[89]:

l


# In[90]:

import pandas as pd
df=pd.DataFrame(l)


# In[91]:

df


# In[92]:

df.to_csv("wyhouses.csv")

