import streamlit as st  #streamlit套件
import xlrd             #excel套件
import openpyxl         #excel套件
import pandas as pd     #pandas套件(資料分析)
import matplotlib.pyplot as plt #matplotlib(資料繪圖)
def chart(option_data):
  st.markdown('### 數據分析')
  col1,col2=st.columns((6,4))
  with col1:
      data=pd.read_excel("data/"+option_data+".xlsx",sheet_name=None) 

      plt.style.use("ggplot")
      plt.plot(data.年度, data.防禦率,'.-' ,color='yellow') 
      #plt.plot(teamsPitching_Unilions.年度, teamsPitching_Unilions.防禦率,'.-' ,color='darkorange')
      #plt.plot(teamsPitching_Dragons.年度, teamsPitching_Dragons.防禦率, '.-',color='red')
      #plt.plot(teamsPitching_Guardians.年度, teamsPitching_Guardians.防禦率,'.-', color='darkblue')
      #plt.plot(teamsPitching_Rakuten.年度, teamsPitching_Rakuten.防禦率,'.-', color='maroon')
      #plt.plot(teamsPitching_TSGHAWKS.年度, teamsPitching_TSGHAWKS.防禦率,'.-', color='darkgreen')
      plt.xlabel('Season',fontsize="10")
      plt.ylabel('ERA',fontsize="10")
      plt.title('ERA')
      plt.legend(labels=["Brothers Pitching", "Unilions Pitching","Dragons Pitching","Guardians Pitching","Rakuten Pitching","TSGHAWKS Pitching"], loc = 'best')
      st.pyplot(plt) 
 
