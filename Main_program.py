import streamlit as st  #streamlit套件
from PIL import Image   #圖片套件
import teams_information
import Baseballfield
import xlrd 
import openpyxl
import pandas as pd
import plost  
import chart

#-----Set up-----------------------------------------------------
st.set_page_config(page_title="CPBL Dashboard",
                   page_icon='⚾',
                   layout="wide")
st.title('中華職棒資訊面板系統')


#-----Sidebar----------------------------------------------------
image=Image.open('CPBL logo.png')
st.sidebar.image(image)
st.sidebar.title('請選擇球隊及想查看的數據🤔?')
teams_list={'中信兄弟':'Brothers','樂天桃猿':'Rakuten','富邦悍將':'Guardians','統一7-ELEVEn獅':'Unilions', '味全龍':'Dragons','台鋼雄鷹':'TSGHAWKS'}
option_teams = st.sidebar.selectbox('選擇球隊🤔？',teams_list)

data_list={'投手成績', '打擊成績','球隊成績', '守備成績'}
option_data = st.sidebar.selectbox('選擇所想查看的數據🤔？成績至2014結算至2022,由於有些球隊已易主或新加入，有些數據不可考。',data_list)

expander = st.sidebar.expander("專用數據翻譯")
expander.write("ERA自責分率 StrikeOut三振 BB四死球 Home主場 Away客場 BattingAvg打擊率 OBP上壘率 SLG長打率 Hit安打 Homerun全壘打 FPCT守備率 E失誤")


#-----teams_information-----------------------------------------
teams_information.teams_information(option_teams)


#-----主客假日球衣-------------------------------------------------------------
col1, col2,col3 = st.columns(3)
with col1:
  st.markdown('### 2022年度主場球衣')
  image=Image.open('球衣/'+option_teams+'1.jpg')
  image2 = image.resize((800,1200)) 
  st.image(image2)
with col2:  
  st.markdown('### 2022年度客場球衣')
  image=Image.open('球衣/'+option_teams+'2.jpg')
  image2 = image.resize((800,1200)) 
  st.image(image2)
with col3:
  st.markdown('### 2022年度假日球衣')
  image=Image.open('球衣/'+option_teams+'3.jpg')
  image2 = image.resize((800,1200)) 
  st.image(image2)
if option_teams=="中信兄弟":  
  st.markdown('##### 附:周二至周四的二連戰，著復古球衣；周末之三連戰則著主場球衣。已拋棄客場球衣。亦無假日版球衣。')
if option_teams=="台鋼雄鷹":
  st.markdown('##### 附:台鋼雄鷹為2022新加入之球隊，尚未有主客場、假日版球衣之設計。')
  
  
#-----teams_map----------------------------------------- 
Baseballfield.Baseballfield(option_teams)  


#----teams_data-----------------------------------------------------------
st.subheader(option_data)
data = pd.read_excel("data/"+option_data+".xlsx",sheet_name=option_teams,index_col='年度') 
st.dataframe(data)
if option_data=='球隊成績':   
   st.markdown('### 球隊數據分析')
   dount_chart_df = pd.read_excel("data/teamsdata(dount-chart).xlsx",sheet_name=option_teams)
   plost.donut_chart(data=dount_chart_df ,               
                        color='項目',
                        theta='戰績',
                        legend='bottom',
                        use_container_width=True)


#-----chart---------------------------------------------------
st.markdown('### 球隊數據分析')
chart.chart(option_data)


#-----年度主視覺-----------------------------------------------------------
st.markdown('### 2022年年度主視覺')
image = Image.open("teams_information"+"/"+teams_list[option_teams]+"/"+option_teams+".jpg")
st.image(image)
if option_teams=="台鋼雄鷹":
  st.markdown('##### 附:台鋼雄鷹為2022新加入之球隊，尚未有年度主視覺之設計。')

