st.header('樂天桃猿')
  st.write('第一金剛(2003) – La new熊(2004-2010) – Lamigo 桃猿(2011-2019) – 樂天桃猿(2020 - 至今)')
  image = Image.open('Rakuten.png')
  st.image(image)
  col1, col2 = st.columns(2)
  col1.metric("季冠軍🏆", "14  次")
  col2.metric("年度冠軍🏆", "7  次")
  st.write('2019年07月03日，甫達成季冠軍五連霸的Lamigo桃猿隊於選秀會結束後，突如其來宣佈因不堪連年經營虧損，決定轉賣球隊，也震撼了原先尚在歡慶味全龍隊重返職棒的中華職棒。09月19日，桃猿隊正式宣佈將經營權完全轉售予已在日本職棒擁有東北樂天金鷲隊的日商樂天集團，結束16年職棒經營事業，樂天也向桃猿保證，接手後大高熊育樂股份有限公司（經營桃猿隊）、大桃猿育樂股份有限公司（經營桃園國際棒球場）的球隊相關工作人員都會予以留用。')
  st.write("2021年度歌曲 一起更強")
  audio_file = open("一起更強.mp3", "rb")
  st.audio(audio_file.read()) 
  st.write("嗆司曲 超越夢想")
  audio_file = open("超越夢想.mp3", "rb")
  st.audio(audio_file.read())  
