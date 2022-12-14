import streamlit as st
import xlrd 
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import plost
import Brothers
import Unilions
import Rakuten
import Dragons 
import Guardians
import TSGHAWKS
import Baseballfield
st.set_page_config(layout="wide")
st.title('中華職棒資訊面板系統')
st.sidebar.header('選擇球隊及數據')

team_list={'中信兄弟','樂天桃猿','富邦悍將','統一7-ELEVEn獅', '味全龍','台鋼雄鷹'}
question_list={'投手成績', '打擊成績','球隊成績', '守備成績'}
option = st.sidebar.selectbox( '選擇球隊？',team_list)
option1 = st.sidebar.selectbox( '選擇所想查看的數據？成績至2014結算至2021由於有些球隊已易主或重新加入，有些數據不可考。', question_list)

df = pd.read_excel("teamsdata.xlsx",sheet_name=option) 
dount_chart_df = pd.read_excel("teamsdata(dount-chart).xlsx",sheet_name=option)

expander = st.sidebar.expander("專用數據翻譯")
expander.write("ERA自責分率 StrikeOut三振 BB四死球 Home主場 Away客場 BattingAvg打擊率 OBP上壘率 SLG長打率 Hit安打 Homerun全壘打 FPCT守備率 E失誤")
if option == '中信兄弟':
  Brothers.Brothers()
  Baseballfield.Taichung()
if option == '統一7-ELEVEn獅':
  Unilions.Unilions()
  Baseballfield.Tainan()
if option == '樂天桃猿':
  Rakuten.Rakuten() 
  Baseballfield.Taoyuan()
if option == '味全龍':
  Dragons.Dragons()
  Baseballfield.Taipei()
  Baseballfield.Hsinchu()
if option == '富邦悍將':
  Guardians.Guardians()
  Baseballfield.NewTaipei()
if option == '台鋼雄鷹':
  TSGHAWKS.TSGHAWKS()
  Baseballfield.Kaohsiung()
if option1=='球隊成績':
  col1,col2=st.columns((6,4))
  with col1:
      st.markdown('### 球隊成績')
      st.dataframe(df)
  with col2:  
    st.markdown('### 2022年全年度戰績Donut chart')
    plost.donut_chart(
                data=dount_chart_df ,
                theta='戰績',
                color='項目',
                legend='bottom',
                use_container_width=True)
  st.markdown('### 2022年年度主視覺')
  image = Image.open(option+'.jpg')
  st.image(image)
elif option1=='投手成績':
    st.markdown('### 投手成績')
    teamsPitching=pd.read_excel("teamsPitching.xlsx") 
    teamsPitching1=pd.read_excel("teamsPitching.xlsx",sheet_name=option) 
    st.dataframe(teamsPitching1)
    st.header('數據分析')
    #plt.style.use("ggplot")
    #plt.plot(BrothersPitching.年度, BrothersPitching.防禦率,'.-' ,color='yellow')
    #plt.plot(UnilionsPitching.年度, UnilionsPitching.防禦率,'.-' ,color='darkorange')
    #plt.plot(DragonsPitching.年度, DragonsPitching.防禦率, '.-',color='red')
    #plt.plot(GuardiansPitching.年度, GuardiansPitching.防禦率,'.-', color='darkblue')
    #plt.plot(RakutenPitching.年度, RakutenPitching.防禦率,'.-', color='maroon')
    #plt.xticks([2021,2020,2019,2018,2017,2016,2015,2014])
    #plt.xticks(BrothersPitching.年度) # 設定x軸
    #plt.xticks(UnilionsPitching.年度) 
    #plt.xticks(RakutenPitching.年度) 
    #plt.xticks(GuardiansPitching.年度)
    #plt.xticks(DragonsPitching.年度) 
    #plt.title('CTBC Brothers Pitching ERA VS Other Teams ') # 設定圖表標題
    #plt.legend(labels=["BrothersPitching", "UnilionsPitching","DragonsPitching","GuardiansPitching","RakutenPitching"], loc = 'best')
    #st.pyplot(plt) 
 
