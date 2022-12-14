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
    teamsPitching_Brothers=pd.read_excel("teamsPitching.xlsx",sheet_name="中信兄弟") 
    teamsPitching_Unilions=pd.read_excel("teamsPitching.xlsx",sheet_name="統一7-ELEVEn獅") 
    teamsPitching_Rakuten=pd.read_excel("teamsPitching.xlsx",sheet_name="樂天桃猿")
    teamsPitching_Guardians=pd.read_excel("teamsPitching.xlsx",sheet_name="富邦悍將")
    teamsPitching_Dragons=pd.read_excel("teamsPitching.xlsx",sheet_name="味全龍")
    teamsPitching_TSGHAWKS=pd.read_excel("teamsPitching.xlsx",sheet_name="台鋼雄鷹")
    st.dataframe(teamsPitching1)
    st.markdown('### 數據分析')
    plt.style.use("ggplot")
    plt.plot(sheet_name="中信兄弟",teamsPitching.年度, teamsPitching.防禦率,'.-' ,color='yellow') 
    plt.plot(teamsPitching_Unilions.年度, teamsPitching_Unilions.防禦率,'.-' ,color='darkorange')
    plt.plot(teamsPitching_Dragons.年度, teamsPitching_Dragons.防禦率, '.-',color='red')
    plt.plot(teamsPitching_Guardians.年度, teamsPitching_Guardians.防禦率,'.-', color='darkblue')
    plt.plot(teamsPitching_Rakuten.年度, teamsPitching_Rakuten.防禦率,'.-', color='maroon')
    plt.plot(teamsPitching_TSGHAWKS.年度, teamsPitching_TSGHAWKS.防禦率,'.-', color='darkgreen')
    plt.xticks([2022,2021,2020,2019,2018,2017,2016,2015,2014])
    plt.xticks(teamsPitching_Brothers.年度) # 設定x軸
    plt.xticks(teamsPitching_Unilions.年度) 
    plt.xticks(teamsPitching_Dragons.年度) 
    plt.xticks(teamsPitching_Guardians.年度)
    plt.xticks(teamsPitching_Rakuten.年度) 
    plt.xticks(teamsPitching_TSGHAWKS.年度) 
    plt.xlabel('Year',fontsize="10")
    plt.ylabel('ERA',fontsize="10")
    plt.legend(labels=["Brothers Pitching", "Unilions Pitching","Dragons Pitching","Guardians Pitching","Rakuten Pitching","TSGHAWKS Pitching"], loc = 'best')
    st.pyplot(plt) 
 
