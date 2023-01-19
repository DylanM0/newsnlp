import requests
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



st.table(me1)
st.table(me2)
st.table(me3)


