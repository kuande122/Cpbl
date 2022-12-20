import streamlit as st  
from PIL import Image  

def teams_information(option_teams):
  if option_teams == '中信兄弟':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/Brothers/Brothers.png')
      st.image(image)
    with col2:
      st.write("""## 中信兄弟""")
      st.write("""##### CTBC Brothers Baseball Club""")
      st.write("""##### 擁有者:中信金控""")
      st.write("""##### 領隊:劉志威""")
      st.write("""##### 總教練:林威助""")
      st.write("""##### 識別色彩:黃色🟨""")
    st.write('兄弟飯店棒球隊(1984-1989年)→兄弟象隊(1990-2013年)→中信兄弟(2014-至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "18  次")
    col2.metric("年度冠軍🏆", "9  次")
    st.write('中信兄弟隊前身兄弟象隊為中職四支創始球隊之一，1992年至1994年曾創下空前的連續三年奪下總冠軍之傲人成績，1992年球季更創下了例行賽45場中37場封王最快速封王的紀錄。之後兄弟象隊於2001年至2003年達成第二次三連霸紀錄，成為中職至今唯一兩度締造三連霸紀錄的球隊。2010年兄弟象隊達成了隊史千勝紀錄，為中職至今唯二達成的球隊，同年下半季取得隊史第11座季冠軍，在當年總冠軍賽以四連勝橫掃興農牛隊，奪下隊史第七座總冠軍，之後10年間，中信兄弟多次闖進總冠軍賽卻始終鎩羽而歸，終於在2021年奪下了隊史第八座總冠軍，奪冠次數僅次於統一7-ELEVEn獅隊，為中華職棒史上奪得總冠軍次數第二多的球隊。')
    st.write("2022年度歌曲 感動黃潮")
    audio_file = open("teams_information/Brothers/感動黃潮.mp3", "rb")
    st.audio(audio_file.read()) 
    st.write("2021年度歌曲 一心兄弟")
    audio_file = open("teams_information/Brothers/一心兄弟.mp3", "rb")
    st.audio(audio_file.read())  
    st.write("嗆司曲 兄弟精神")
    audio_file = open("teams_information/Brothers/兄弟精神.mp3", "rb")
    st.audio(audio_file.read()) 
    
  if option_teams == '統一7-ELEVEn獅':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/Unilions/Unilions.png')
      st.image(image)
    with col2:
      st.write("""## 統一7-ELEVEn獅""")
      st.write("""##### Uni-lions""")
      st.write("""##### 擁有者:統一企業""")
      st.write("""##### 領隊:蘇泰安""")
      st.write("""##### 總教練:林岳平""")
      st.write("""##### 識別色彩:綠色🟩 → 橘色🟧""")
    st.write('統一棒球隊(1989年)→統一獅(1990–2007年)→統一7-ELEVEn獅(2008–至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "15  次")
    col2.metric("年度冠軍🏆", "10  次")
    st.write('統一7-ELEVEn獅隊為台灣在1989年成立中華職棒聯盟時的四支創始球隊之一，也是唯一從職棒元年存續至今的球隊，最初僅命名為統一獅隊；是聯盟第一支有二軍的球隊，同時也是目前中華職棒聯盟贏得總冠軍次數最多的球隊，母企業為統一企業。由於中職初創時統一獅隊成軍較晚，人手不足，經驗也有限，因此於職棒元年開打後，即創下八連敗的紀錄，並在上半球季敬陪末座。但秉著「誠實苦幹」的企業精神，統一球團積極整軍經武，使獅子軍下半球季戰績得以回升，全年度排名第三，免於墊底。隔年更在投打戰力補強有成的情況下，於總冠軍賽擊敗味全龍隊，笑擁隊史首座總冠軍獎盃。')
    st.write("2022年度歌曲 大贏四方")
    audio_file = open("teams_information/Unilions/大贏四方.mp3", "rb")
    st.audio(audio_file.read()) 
    st.write("2021年度歌曲 冠軍獅王")
    audio_file = open("teams_information/Unilions/冠軍獅王.mp3", "rb")
    st.audio(audio_file.read())  
    st.write("嗆司曲 誰與爭鋒")
    audio_file = open("teams_information/Unilions/誰與爭鋒.mp3", "rb")
    st.audio(audio_file.read()) 
    
  if option_teams == '樂天桃猿':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/Rakuten/Rakuten.png')
      st.image(image)
    with col2:
      st.write("""## 樂天桃猿""")
      st.write("""##### Rakuten Monkeys""")
      st.write("""##### 擁有者:樂天株式會社""")
      st.write("""##### 領隊:浦韋青""")
      st.write("""##### 總教練:曾豪駒""")
      st.write("""##### 識別色彩:酒紅色🟥""")
    st.write('台北太陽隊、高屏雷公隊(1997-2002年)→第一金剛隊(2003年)→La New熊隊(2004-2010年)→Lamigo桃猿隊(2011-2019年)→樂天桃猿隊(2020-至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "14  次")
    col2.metric("年度冠軍🏆", "7  次")
    st.write('2019年07月03日，甫達成季冠軍五連霸的Lamigo桃猿隊於選秀會結束後，突如其來宣佈因不堪連年經營虧損，決定轉賣球隊，也震撼了原先尚在歡慶味全龍隊重返職棒的中華職棒。09月19日，桃猿隊正式宣佈將經營權完全轉售予已在日本職棒擁有東北樂天金鷲隊的日商樂天集團，結束16年職棒經營事業，樂天也向桃猿保證，接手後大高熊育樂股份有限公司（經營桃猿隊）、大桃猿育樂股份有限公司（經營桃園國際棒球場）的球隊相關工作人員都會予以留用。')
    st.write("2022年度歌曲 Rise Up")
    audio_file = open("teams_information/Rakuten/Rise Up.mp3", "rb")
    st.audio(audio_file.read()) 
    st.write("2021年度歌曲 一起更強")
    audio_file = open("teams_information/Rakuten/一起更強.mp3", "rb")
    st.audio(audio_file.read())  
    st.write("嗆司曲 超越夢想")
    audio_file = open("teams_information/Rakuten/超越夢想.mp3", "rb")
    st.audio(audio_file.read()) 

  if option_teams == '味全龍':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/Dragons/Dragons.png')
      st.image(image)
    with col2:
      st.write("""## 味全龍""")
      st.write("""##### WeiChuan Dragons""")
      st.write("""##### 擁有者:頂立開發實業（頂新集團）""")
      st.write("""##### 領隊:丁仲緯""")
      st.write("""##### 總教練:葉君璋""")
      st.write("""##### 識別色彩:紅色🟥""")
    st.write('味全棒球隊(1978-1989年)→味全龍(1990-1999年，2019-至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "4  次")
    col2.metric("年度冠軍🏆", "4  次")
    st.write('味全龍隊是中華職棒所屬的球隊，歷史可追溯至1980年代的業餘成棒。其首次進軍中職時，是由味全企業出資成立「純青職棒事業股份有限公司」經營；但1999年季後因經營虧損，以及併購母企業的頂新集團無意繼續經營，最終決定解散球隊。但相隔20年後的2019年，頂新集團出乎意料宣佈重組球隊，並通過聯盟審核，以聯盟第五隊的身份重返中華職棒。')
    st.write("2022年度歌曲 龍往直前")
    audio_file = open("teams_information/Dragons/龍往直前.mp3", "rb")
    st.audio(audio_file.read()) 
    st.write("2021年度歌曲 Come Back Again")
    audio_file = open("teams_information/Dragons/Come Back Again.mp3", "rb")
    st.audio(audio_file.read())  
    st.write("嗆司曲 龍霸四方")
    audio_file = open("teams_information/Dragons/龍霸四方.mp3", "rb")
    st.audio(audio_file.read()) 
    
  if option_teams == '富邦悍將':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/Guardians/Guardians.png')
      st.image(image)
    with col2:
      st.write("""## 富邦悍將""")
      st.write("""##### Fubon Guardians""")
      st.write("""##### 擁有者:富邦金控""")
      st.write("""##### 領隊:林華韋""")
      st.write("""##### 總教練:丘昌榮""")
      st.write("""##### 識別色彩:藍色🟦""")
    st.write('俊國建設棒球隊(1989–1992年)→俊國熊(1993–1995年)→興農熊(1996年)→興農牛(1996–2012年)→義大犀牛(2013–2016年)→富邦悍將(2017–至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "8  次")
    col2.metric("年度冠軍🏆", "3  次")
    st.write('富邦悍將隊（Fubon Guardians）的前身可追溯至成立於1989年的社會甲組球隊俊國建設棒球隊。俊國棒球隊進軍職棒後更名為俊國熊隊，其後歷經三次轉賣，隊名也陸續更改為興農熊隊、興農牛隊、義大犀牛隊，並曾獲得三次總冠軍。2016年季中，當時擁有義大犀牛隊的義联集團宣佈出售球隊，最後由長期贊助業餘棒運的富邦金控以新台幣3億元買下。該年季後，義大隊奪得隊史首座也是最後一座的總冠軍後，隨即自同年11月01日起改由富邦金控接手經營，並在11月15日正式公佈新隊名為富邦悍將隊。')
    st.write("2022年度歌曲 We Will Win")
    audio_file = open("teams_information/Guardians/We Will Win.mp3", "rb")
    st.audio(audio_file.read()) 
    st.write("2021年度歌曲 FIGHT ON")
    audio_file = open("teams_information/Guardians/FIGHT ON.mp3", "rb")
    st.audio(audio_file.read())  
    st.write("嗆司曲 超強一擊")
    audio_file = open("teams_information/Guardians/超強一擊.mp3", "rb")
    st.audio(audio_file.read()) 
    
  if option_teams == '台鋼雄鷹':
    col1, col2 = st.columns(2)
    with col1:
      image = Image.open('teams_information/TSGHAWKS/TSGHAWKS.jpg')
      st.image(image)
    with col2:
      st.write("""## 台鋼雄鷹""")
      st.write("""##### TSG HAWKS""")
      st.write("""##### 擁有者:台灣鋼鐵集團""")
      st.write("""##### 領隊:劉東洋""")
      st.write("""##### 總教練:暫無""")
      st.write("""##### 識別色彩:墨綠色🟩""")
    st.write('台鋼雄鷹隊(2022-至今)')
    col1, col2 = st.columns(2)
    col1.metric("季冠軍🏆", "0  次")
    col2.metric("年度冠軍🏆", "0  次")
    st.write('台鋼雄鷹隊，是中華職棒所屬的球隊。預計於2023年開始於二軍出賽，2024年登上一軍賽事。2019年，解散多年的中華職棒創始球隊味全龍隊重新加盟，使自2008年假球案爆發後便維持四隊規模多年的聯盟，總算盼來期望以久的增隊；擴編第六隊的議題亦迅速浮上檯面，成為2021年年初就任的中職第十一任會長蔡其昌任內首要尋求的目標。該年季後，中信兄弟隊老闆暨中華民國棒球協會理事長辜仲諒於球隊奪冠慶功宴上，首度表示已經擁有臺南台鋼獵鷹籃球隊及台南市台灣鋼鐵足球隊的台灣鋼鐵集團，有意組成球隊投入中職；隨後會長蔡其昌亦證實台鋼已提出間接詢問。2022年01月，台鋼集團正式拜會聯盟，正式表達組成第六隊的意願，且願接受味全隊重新加盟時新擬定的加盟相關條件。2月底，隨另一稍早傳出同樣有意組隊的中華電信放棄計畫，蔡其昌也宣佈由台鋼集團取得組隊資格。台鋼集團隨即在03月02日正式向聯盟遞交加盟意向書，同時表明新球隊命名為「台鋼雄鷹隊」，主場設於2016年後即無職棒球隊進駐的高雄市立澄清湖棒球場，屏東縣立棒球場則作為第二主場。03月30日，台鋼集團向中職挖角宣推部主任劉東洋接任球隊總經理暨領隊，兩天後送出經營計劃書；並在04月27日獲得中職常務理事會審查通過，正式成為中職第六隊。而在台鋼雄鷹隊確定加盟中職後，台灣鋼鐵集團也成為台灣史上首間同時經營籃足棒三項職業運動領域的企業。')
