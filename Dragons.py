import streamlit as st 
from PIL import Image
def Dragons():  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Dragons/Dragons.png')
    st.image(image)
  with col2:
    st.write("""## 味全龍""")
    st.write("""##### WeiChuan Dragons""")
    st.write("""##### 擁有者:頂立開發實業（頂新集團）""")
    st.write("""##### 領隊:丁仲緯""")
    st.write("""##### 總教練:葉君璋""")
    st.write("""##### 識別色彩:紅色""")
  st.write('味全棒球隊(1978-1989年)→味全龍(1990-1999年，2019-至今)')
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "4  次")
  col2.metric("年度冠軍🏆", "4  次")
  st.write('味全龍隊是中華職棒所屬的球隊，歷史可追溯至1980年代的業餘成棒。其首次進軍中職時，是由味全企業出資成立「純青職棒事業股份有限公司」經營；但1999年季後因經營虧損，以及併購母企業的頂新集團無意繼續經營，最終決定解散球隊。但相隔20年後的2019年，頂新集團出乎意料宣佈重組球隊，並通過聯盟審核，以聯盟第五隊的身份重返中華職棒。')
  st.write("2022年度歌曲 龍往直前")
  audio_file = open("Dragons/龍往直前.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("2021年度歌曲 Come Back Again")
  audio_file = open("Dragons/Come Back Again.mp3", "rb")
  st.audio(audio_file.read())  
  st.write("嗆司曲 龍霸四方")
  audio_file = open("Dragons/龍霸四方.mp3", "rb")
  st.audio(audio_file.read()) 
