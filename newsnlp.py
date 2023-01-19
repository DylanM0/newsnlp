import requests
import matplotlib.pyplot as plt
from mecab import MeCab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib


mecab = MeCab()

def ko_preprocess_sentence(sentence, s_token=False, e_token=False):
    sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
    sentence = re.sub(r'[" "]+', " ", sentence)
    sentence = re.sub(r"[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z?.!,]+", " ", sentence)

    sentence = sentence.strip()
    sentence = mecab.morphs(sentence)

    if s_token:
        sentence = '<start> ' + sentence

    if e_token:
        sentence += ' <end>'
    
    return sentence


st.header('연습용 형태소 분석기입니다 ')

corpus = st.text_input('한글입력', '당신의 이름은 무엇입니까?')

corpus1
for kor in corpus:
    corpus1.append(ko_preprocess_sentence(kor))
    

st.table(corpus1)


