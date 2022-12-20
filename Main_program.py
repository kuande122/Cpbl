import streamlit as st  #streamlit套件


#-----Set up-----------------------------------------------------
st.set_page_config(page_title="CPBL Dashboard",
                   page_icon='⚾',
                   layout="wide")
st.title('中華職棒資訊面板系統')


#-----Sidebar----------------------------------------------------
image=Image.open('CPBL logo.png')
st.sidebar.image(image)
st.sidebar.title('請選擇區域及球隊')
teams_list={'中信兄弟','樂天桃猿','富邦悍將','統一7-ELEVEn獅', '味全龍','台鋼雄鷹'}
option_teams = st.sidebar.selectbox('選擇球隊？',teams_list)
