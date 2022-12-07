import streamlit as st
import Brothers
import Unilions
st.title('中華職棒資訊面板系統')
st.sidebar.header('選擇球隊及數據')
option = st.sidebar.selectbox( '選擇球隊？', ['中信兄弟', '統一7-ELEVEn獅', '味全龍', '樂天桃猿','富邦悍將'])
option1 = st.sidebar.selectbox( '選擇所想查看的數據？成績至2014結算至2021由於有些球隊已易主或重新加入，有些數據不可考。', ['球隊成績', '投手成績', '打擊成績', '守備成績'])
expander = st.sidebar.expander("專用數據翻譯")
expander.write("ERA自責分率 StrikeOut三振 BB四死球 Home主場 Away客場 BattingAvg打擊率 OBP上壘率 SLG長打率 Hit安打 Homerun全壘打 FPCT守備率 E失誤")
if option == '中信兄弟':
  Brothers.Brothers()
if option == '統一7-ELEVEn獅':
  Unilions.Unilions()  
