import streamlit as st 
from PIL import Image
def Brothers():  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Brothers/Brothers.png')
    st.image(image)
  with col2:
    st.write("""## 中信兄弟""")
    st.write("""##### CTBC Brothers Baseball Club""")
    st.write("""##### 擁有者:中信金控""")
    st.write("""##### 領隊:劉志威""")
    st.write("""##### 總教練:林威助""")
    st.write("""##### 識別色彩:黃色""")
  st.write('兄弟飯店棒球隊(1984-1989年)→兄弟象隊(1990-2013年)→中信兄弟(2014-至今)')
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "18  次")
  col2.metric("年度冠軍🏆", "9  次")
  st.write('中信兄弟隊前身兄弟象隊為中職四支創始球隊之一，1992年至1994年曾創下空前的連續三年奪下總冠軍之傲人成績，1992年球季更創下了例行賽45場中37場封王最快速封王的紀錄。之後兄弟象隊於2001年至2003年達成第二次三連霸紀錄，成為中職至今唯一兩度締造三連霸紀錄的球隊。2010年兄弟象隊達成了隊史千勝紀錄，為中職至今唯二達成的球隊，同年下半季取得隊史第11座季冠軍，在當年總冠軍賽以四連勝橫掃興農牛隊，奪下隊史第七座總冠軍，之後10年間，中信兄弟多次闖進總冠軍賽卻始終鎩羽而歸，終於在2021年奪下了隊史第八座總冠軍，奪冠次數僅次於統一7-ELEVEn獅隊，為中華職棒史上奪得總冠軍次數第二多的球隊。')
  st.write("2022年度歌曲 感動黃潮")
  audio_file = open("Brothers/感動黃潮.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("2021年度歌曲 一心兄弟")
  audio_file = open("Brothers/一心兄弟.mp3", "rb")
  st.audio(audio_file.read())  
  st.write("嗆司曲 兄弟精神")
  audio_file = open("Brothers/兄弟精神.mp3", "rb")
  st.audio(audio_file.read()) 
中信兄弟=Brothers()
  
  
