import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import matplotlib.pyplot as plt #matplotlib(資料繪圖)


def chart(option_data):
  data1=pd.read_excel("data/"+option_data+".xlsx",sheet_name="中信兄弟") 
  data2=pd.read_excel("data/"+option_data+".xlsx",sheet_name="統一7-ELEVEn獅") 
  data3=pd.read_excel("data/"+option_data+".xlsx",sheet_name="樂天桃猿") 
  data4=pd.read_excel("data/"+option_data+".xlsx",sheet_name="富邦悍將") 
  data5=pd.read_excel("data/"+option_data+".xlsx",sheet_name="味全龍") 
  data6=pd.read_excel("data/"+option_data+".xlsx",sheet_name="台鋼雄鷹")  
  col1,col2=st.columns((6,4))
  with col1:
    while option_data=='投手成績':
      plt.style.use("ggplot")
      plt.plot(data1.年度, data1.防禦率,'.-' ,color='yellow') 
      plt.plot(data2.年度, data2.防禦率,'.-' ,color='darkorange')
      plt.plot(data3.年度, data3.防禦率, '.-',color='red')
      plt.plot(data4.年度, data4.防禦率,'.-', color='darkblue')
      plt.plot(data5.年度, data5.防禦率,'.-', color='maroon')
      plt.plot(data6.年度, data6.防禦率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.title('Pitching ERA')
      plt.legend(labels=["Brothers Pitching", "Unilions Pitching","Dragons Pitching","Guardians Pitching","Rakuten Pitching","TSGHAWKS Pitching"], loc = 'best')
      st.pyplot(plt) 
      break
    while option_data=='打擊成績':
      plt.style.use("ggplot")
      plt.plot(data1.年度, data1.打擊率,'.-' ,color='yellow') 
      plt.plot(data2.年度, data2.打擊率,'.-' ,color='darkorange')
      plt.plot(data3.年度, data3.打擊率, '.-',color='red')
      plt.plot(data4.年度, data4.打擊率,'.-', color='darkblue')
      plt.plot(data5.年度, data5.打擊率,'.-', color='maroon')
      plt.plot(data6.年度, data6.打擊率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.title('Batting Avg')
      plt.legend(labels=["Brothers Batting", "Unilions Batting","Dragons Batting","Guardians Batting","Rakuten Batting","TSGHAWKS Batting"], loc = 'best')
      st.pyplot(plt) 
      break
    while option_data=='守備成績':
      plt.style.use("ggplot")
      plt.plot(data1.年度, data1.守備率,'.-' ,color='yellow') 
      plt.plot(data2.年度, data2.守備率,'.-' ,color='darkorange')
      plt.plot(data3.年度, data3.守備率, '.-',color='red')
      plt.plot(data4.年度, data4.守備率,'.-', color='darkblue')
      plt.plot(data5.年度, data5.守備率,'.-', color='maroon')
      plt.plot(data6.年度, data6.守備率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.title('Defense FPCT')
      plt.legend(labels=["Brothers Defense", "Unilions Defense","Dragons Defense","Guardians Defense","Rakuten Defense","TSGHAWKS Defense"], loc = 'best')
      st.pyplot(plt) 
      break
with col2:
    if option_data=='打擊成績':
      plt.style.use("ggplot")
      plt.plot(data1.年度, data1.長打率,'.-' ,color='yellow') 
      plt.plot(data2.年度, data2.長打率,'.-' ,color='darkorange')
      plt.plot(data3.年度, data3.長打率, '.-',color='red')
      plt.plot(data4.年度, data4.長打率,'.-', color='darkblue')
      plt.plot(data5.年度, data5.長打率,'.-', color='maroon')
      plt.plot(data6.年度, data6.長打率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.title('Batting Avg')
      plt.legend(labels=["Brothers Batting", "Unilions Batting","Dragons Batting","Guardians Batting","Rakuten Batting","TSGHAWKS Batting"], loc = 'best')
      st.pyplot(plt) 
      break
