import matplotlib.pyplot as plt
from mecab import MeCab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib
import seaborn as sns
import numpy as np
import pandas as pd
from stqdm import stqdm



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
    
    
    choice = df['모집단위'].unique()
    choice_column = st.selectbox('선택해주세요',choice, )


    명사카운트 = df[df['모집단위'] == choice_column]
    

    from collections import Counter

    
   
    여기 = [i for i in 명사카운트['세특1']]
    
    여기1 = listToString(여기)
    
    
    nouns = mecab.nouns(여기1)
    nouns = [n for n in nouns if len(n) > 1]
    count = Counter(nouns)
    top = count.most_common(20)
    st.table(top)
    
    x = np.arange(len(top))
    keys = [x[0] for x in top] 
    values = [x[1] for x in top] 
    
    plt.figure(figsize=(12,6))
    plt.bar(x, values)
    plt.xticks(x, keys)
    hao1 = plt.savefig(hao)
    st.pyplot(hao1)
    
    
    
    
    
    
    
#     qwe = []
#     for i in stqdm(명사카운트['세특1'].index):
#         nouns = mecab.nouns(명사카운트['세특1'][i])
#         nouns = [n for n in nouns if len(n) > 1]
#         qwe.append(nouns)
    
#     명사카운트['명사'] = qwe
    
    
        

        


#     키워드 =[]
#     for tags in 명사카운트['명사']:
#         tag_list = tags[2:-2].split("', '")
#         for tag in tag_list:
#             키워드.append(tag)



#     from collections import Counter
#     count1 = Counter(키워드)




#     fenxi = pd.DataFrame(count1.most_common(50))
#     fenxi.columns =['tags', 'counts']




#     fig = plt.figure(figsize = (10,20))
#     haohao = sns.barplot(x='counts',y='tags', data=fenxi)

#     box1 = fig.savefig(haohao)
#     st.pyplot(box1)
    
    
    
    
    
    



