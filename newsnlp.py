import matplotlib.pyplot as plt
from mecab import MeCab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib

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


