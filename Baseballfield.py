import streamlit as st 
from PIL import Image
from streamlit_folium import folium_static #地圖套件
import folium 
def Taichung():
    col1, col2 = st.columns(2)
    with col1:
        st.header('主場:臺中洲際棒球場')
        st.write('地址：臺中市北屯區崇德路三段835號')
        st.write('觀眾席數：約兩萬席（內野14,321席對號座位，外野5,000席自由座位）')
        st.write('全壘打牆距離：左外野：325英呎 中外野：400英呎 右外野：325英呎')
        image = Image.open('Baseballfield/台中洲際球場.png')
        st.image(image)
    with col2:
        m1 = folium.Map(width='50%', height='80%',location=[24.19978, 120.68498], zoom_start=16)

        # add marker for Liberty Bell
        tooltip = "臺中洲際棒球場"
        folium.Marker([24.19978, 120.68498], popup="臺中洲際棒球場", tooltip=tooltip
        ).add_to(m1)
        folium_static(m1)
def Tainan():   
  col1, col2 = st.columns(2)
  with col1:  
    st.header('主場:臺南市立棒球場')
    st.write('地址：臺南市南區健康路一段257號')
    st.write('觀眾席數：12,000席')
    st.write('全壘打牆距離：左外野：339英呎 中外野：400英呎 右外野：339英呎')
    image = Image.open('台南球場.jpg')
    st.image(image)
  with col2:  
    m3 = folium.Map(width='50%', height='80%',location=[22.98043, 120.2062], zoom_start=16)

    # add marker for Liberty Bell
    tooltip = "臺南市立棒球場"
    folium.Marker([22.98043, 120.2062], popup="臺南市立棒球場", tooltip=tooltip
    ).add_to(m3)
def Taipei():      
  col1, col2 = st.columns(2)
  with col1:  
    st.header('主場:臺北市立天母棒球場')
    st.write('地址：臺北市士林區三玉里忠誠路二段77號（忠誠路與士東路口）')
    st.write('觀眾席數：10,000席 內野數：10,000席 外野野餐區:')
    st.write('草皮：人工草皮')
    st.write('全壘打牆距離：左外野：325英呎 中外野：400英呎 右外野：325英呎')
    image = Image.open('台北天母球場.jpg')
    st.image(image)
  with col2: 
    m5 = folium.Map(width='50%', height='80%',location=[25.11374, 121.53345], zoom_start=16)

    # add marker for Liberty Bell
    tooltip = "臺北天母棒球場"
    folium.Marker([25.11374, 121.53345], popup="臺北天母棒球場", tooltip=tooltip
    ).add_to(m5)

    #   call to render
    folium_static(m5)
def Taoyuan():        
  col1, col2 = st.columns(2)
  with col1: 
    st.header('主場:桃園國際棒球場')
    st.write('地址：桃園市中壢區芝芭里領航北路1段1號')
    st.write('觀眾席數：兩萬席（內野12,000席，外野8,000席）')
    st.write('全壘打牆距離：左外野：330英呎 中外野：400英呎 右外野：330英呎')
    image = Image.open('桃園球場.png')
    st.image(image)
  with col2: 
    m2 = folium.Map(location=[25.00054,121.20038], zoom_start=16)
    tooltip = "桃園國際棒球場"
    folium.Marker([25.00054,121.20038], popup="桃園國際棒球場", tooltip=tooltip
    ).add_to(m2)
    folium_static(m2)
def NewTaipei():
  col1, col2 = st.columns(2)
  with col1:
     st.header('主場:新北新莊棒球場')
     st.write('全名：新北市立新莊棒球場（XinZhuang Baseball Stadium）')
     st.write('地址：新北市新莊區立德里和興街66號')
     st.write('草皮：天然草皮（百慕達草）')
     st.write('螢幕：外野：LED大螢幕（左）、LED螢幕（右）內野：環狀屏LED')
     st.write('觀眾席數：12,150席 內野數：8,150席 外野數：4,000席')
     st.write('全壘打牆距離：左外野：325英呎 中外野：400英呎 右外野：325英呎')
     image = Image.open('新莊全景.jpg')
     st.image(image)
  with col2:
      # add marker for Liberty Bell
     m = folium.Map(location=[25.04054,121.44768], zoom_start=16)
     tooltip = "新北新莊棒球場"
     folium.Marker([25.04054,121.44768], popup="新北市立新莊棒球場", tooltip=tooltip
     ).add_to(m)

     # call to render Folium map in Streamlit
     folium_static(m)
