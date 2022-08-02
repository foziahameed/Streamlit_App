# Submitted BY:Fozia Hameed

from email.headerregistry import Group
import imp
import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import altair as alt
import random



st.title(''' 
            # **Pakistan Agricultural & Population Information Statistics  Web App**

                     ''')
st.image('flag.png',width=200)
st.sidebar.title('Pakistan DashBoard')
st.sidebar.markdown(''' 
This app is to give insights about Population Information 
The data considerd for this analysis from 1950 to 2018.
Select the different options to vary the Visualization
All the Charts are interactive. 

Note: The data arehas been read from the https://www.fao.org/faostat/en/#data/OA

Designed by:Fozia Hameed''')  

df=pd.read_csv('population.csv')
group1=df['Element'].unique().tolist()
color_array=['black', 'silver', 'gray', 'white', 'maroon', 'red', 'purple', 'fuchsia', 'green', 'lime', 'olive', 'yellow', 'navy', 'blue', 'teal', 'aqua', 'orange', 'aliceblue', 'antiquewhite', 'aquamarine',
             'azure', 'beige', 'bisque', 'blanchedalmond', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 
             'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue',
             'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'gainsboro', 'ghostwhite',
             'gold', 'goldenrod', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral', 
             'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 
             'lightyellow', 'limegreen', 'linen', 'magenta', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 
             'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'oldlace', 'olivedrab', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 
             'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'skyblue', 'slateblue', 
             'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'whitesmoke', 'yellowgreen', 'rebeccapurple']




gr=st.selectbox('How you want to see Graph of different groups of population?',('Choose','Single','Cumulative'))
if gr=='Single':
   typ = st.selectbox("Select the type of Chart",('Choose',"Line Chart","Bar Chart"))
   group=st.selectbox('Select Group of Population',df['Element'].unique().tolist())
   
   ca = alt.Chart(df[df["Element"]== group]).encode(x=alt.X("Year",scale=alt.Scale(df['Year'].min(),df['Year'].max())), y=alt.Y("Value",scale=alt.Scale(df['Value'].min(),df['Value'].max())), 
                                                    tooltip=["Year","Value"]).interactive()

                
   if typ == "Line Chart":
         st.altair_chart(ca.mark_line(color=color_array[random.randint(0,150)]),use_container_width=True)
   else  :
         st.altair_chart(ca.mark_bar(color=color_array[random.randint(0,150)]),use_container_width=True)
            


elif gr=='Cumulative':  
   options = st.multiselect(
    'Select Multiple groups',
     df["Element"][:5])
   
   

   fire=alt.Chart(df[df["Element"].isin(options)]).mark_line().encode( x=alt.X("Year"),
      y=alt.Y("Value"),
      color="Element",
      tooltip=["Year","Value"]).interactive()
   
   bar1 = alt.Chart(df[df["Element"].isin(options)]).mark_bar().encode(
    y="Value",
    x=alt.X("Element",sort="-y"),
    color="Element",
    tooltip = ["Year","Value"]
).interactive()
   st.altair_chart(fire|bar1)
   