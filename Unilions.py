import streamlit as st 
from PIL import Image
def Unilions():  
  col1, col2 = st.columns(2)
  with col1:
    image = Image.open('Unilions/Unilions.png')
    st.image(image)
  with col2:
    st.write("""## 統一7-ELEVEn獅""")
    st.write("""##### Uni-lions""")
    st.write("""##### 擁有者:統一企業""")
    st.write("""##### 領隊:蘇泰安""")
    st.write("""##### 總教練:林岳平""")
    st.write("""##### 識別色彩:綠色 → 橘色""")
  st.write('統一棒球隊(1989年)→統一獅(1990–2007年)→統一7-ELEVEn獅(2008–至今)')
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "15  次")
  col2.metric("年度冠軍🏆", "10  次")
  st.write('統一7-ELEVEn獅隊為台灣在1989年成立中華職棒聯盟時的四支創始球隊之一，也是唯一從職棒元年存續至今的球隊，最初僅命名為統一獅隊；是聯盟第一支有二軍的球隊，同時也是目前中華職棒聯盟贏得總冠軍次數最多的球隊，母企業為統一企業。由於中職初創時統一獅隊成軍較晚，人手不足，經驗也有限，因此於職棒元年開打後，即創下八連敗的紀錄，並在上半球季敬陪末座。但秉著「誠實苦幹」的企業精神，統一球團積極整軍經武，使獅子軍下半球季戰績得以回升，全年度排名第三，免於墊底。隔年更在投打戰力補強有成的情況下，於總冠軍賽擊敗味全龍隊，笑擁隊史首座總冠軍獎盃。')
  st.write("2022年度歌曲 大贏四方")
  audio_file = open("Unilions/大贏四方.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("2021年度歌曲 冠軍獅王")
  audio_file = open("Unilions/冠軍獅王.mp3", "rb")
  st.audio(audio_file.read())  
  st.write("嗆司曲 誰與爭鋒")
  audio_file = open("Unilions/誰與爭鋒.mp3", "rb")
  st.audio(audio_file.read()) 


