import matplotlib.pyplot as plt
from mecab import MeCab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
from stqdm import stqdm
import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module



def generate_excel_download_link(df):
    # Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_download.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s




st.header('연습용 형태소 분석기입니다 ')
corpus = st.text_input('한글입력', '당신의 이름은 무엇입니까?')


mecab = MeCab()

me1 = mecab.morphs(corpus)
me2 = mecab.nouns(corpus)
me3 = mecab.pos(corpus)


st.subheader('형태소분석_1')
st.table(me1)

st.subheader('형태소_명사추출')
st.table(me2)

st.subheader('형태소분석_2(품사포함)')
st.table(me3)


uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    
#     qwe = []
#     for i in stqdm(df['세특1'].index):
#         nouns = mecab.nouns(df['세특1'][i])
#         nouns = [n for n in nouns if len(n) > 1]
#         qwe.append(nouns)
    
#     df['명사'] = qwe
    
#     generate_excel_download_link(df)
    
    
    합격 = df[df['합격']=='합']
    
    
    choice = 합격['모집단위'].unique()
    choice1 = 합격['편제'].unique()

    choice_column = st.selectbox('선택해주세요',choice, )
    
    options = st.selectbox('선택해주세요',choice1)


    명사카운트 = 합격[(합격['모집단위'] == choice_column)&(합격['편제'] == options)]

  



    from collections import Counter
    
#     키워드=[]
#     for i in 명사카운트['명사']:
#         tag_list = 명사카운트['명사'][i].split("', '")
#         for tag in tag_list:
#             키워드.append(tag)



    여기 = [i for i in 명사카운트['세특1']]

    여기1 = listToString(여기)


    nouns = mecab.nouns(여기1)
    nouns = [n for n in nouns if len(n) > 1]
    count = Counter(nouns)
    top = count.most_common(30)


    fenxi = pd.DataFrame(top)
    fenxi.columns =['tags', 'counts']

    st.table(fenxi)


    fig =  plt.figure(figsize = (10,10))

    sns.barplot(x='counts',y='tags', data=fenxi)

    st.pyplot(fig)
    
        
    ddr = dict(count.most_common(100))
    
    
    wc = WordCloud(background_color="white",
                   width=1000, height=1000, 
                   max_words=30, max_font_size=300).generate_from_frequencies(ddr)

    

    plt.figure(figsize = (17,17))
    plt.imshow(wc)
    plt.axis('off')
    st.pyplot(wc)
    
    
    
#     fig = px.bar(data =fenxi, x=counts, y=tags, color='Profit', template='plotly_white', title=f'<b>Sales & Profit by {choice_column}</b>')

    

    
    
#     hao1 = plt.savefig(hao)
#     st.pyplot(hao1)
    
    
    
    
    
    
    




    
    
    
    
    
    



