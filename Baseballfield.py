from streamlit_folium import folium_static #地圖套件
import folium 
def Taichung():
    col1, col2 = st.columns(2)
    with col1:
        st.header('主場:臺中洲際棒球場')
        st.write('地址：臺中市北屯區崇德路三段835號')
        st.write('觀眾席數：約兩萬席（內野14,321席對號座位，外野5,000席自由座位）')
        st.write('全壘打牆距離：左外野：325英呎 中外野：400英呎 右外野：325英呎')
        image = Image.open('台中洲際球場.png')
        st.image(image)
    with col2:
        m1 = folium.Map(location=[24.19978, 120.68498], zoom_start=16)

        # add marker for Liberty Bell
        tooltip = "臺中洲際棒球場"
        folium.Marker([24.19978, 120.68498], popup="臺中洲際棒球場", tooltip=tooltip
        ).add_to(m1)
        folium_static(m1)
