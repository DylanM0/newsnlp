import requests
import matplotlib.pyplot as plt
from konlpy.tag import Kkma
from konlpy.tag import Mecab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib

!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
!bash install_mecab-ko_on_colab190912.sh

mecab = Mecab()

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

for kor in cleaned_corpus:
    corpus.append(ko_preprocess_sentence(kor))
    

st.table(corpus)


