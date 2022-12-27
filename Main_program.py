import streamlit as st  #streamlit套件
from PIL import Image   #圖片套件
import teams_information
import Baseballfield
import xlrd 
import openpyxl
import pandas as pd

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
  
  image=Image.open('球衣/'+option_teams+'1.jpg')
  for i in image:
    image = Image.open(i)
    size = image.size
    max = 1200                    # 設定長或寬最大的數值
    if size[0]>size[1]:          # 如果原始圖片 width 大於 height
        scale = size[1]/size[0]  # 設定 scale 為 height/width
        w = max                  # 設定調整後的寬度為最大的數值
        h = int(max*scale)       # 設定調整後的高度為 max 乘以 scale ( 使用 int 去除小數點 )
    else:                        # 如果原始圖片 width 小於等於 height
        scale = size[0]/size[1]  # 設定 scale 為 width/height
        w = int(max*scale)       # 設定調整後的寬度為 max 乘以 scale ( 使用 int 去除小數點 )
        h = max                  # 設定調整後的高度為最大的數值
    name = i.split('/')[::-1][0]
    image2 = im.resize((w, h))      # 調整尺寸
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
  
#-----teams_map----------------------------------------- 
Baseballfield.Baseballfield(option_teams)  


#----teams_data-----------------------------------------------------------
st.subheader(option_data)
data = pd.read_excel("data/"+option_data+".xlsx",sheet_name=option_teams,index_col='年度') 
st.dataframe(data)


#-----年度主視覺-----------------------------------------------------------
st.markdown('### 2022年年度主視覺')
image = Image.open("teams_information"+"/"+teams_list[option_teams]+"/"+option_teams+".jpg")
st.image(image)
if option_teams=="台鋼雄鷹":
  st.markdown('##### 附:台鋼雄鷹為2022新加入之球隊，尚未有年度主視覺')

