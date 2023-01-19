import requests
import matplotlib.pyplot as plt
from konlpy.tag import Kkma
from konlpy.tag import Okt
from konlpy.tag import Mecab
from wordcloud import WordCloud
import streamlit as st
import koreanize_matplotlib

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

kor_raw_corpus = st.text_input('한글입력', '당신의 이름은 무엇입니까?')
eng_raw_corpus = st.text_input('영어입력', 'What is your name?')

for kor, eng in cleaned_corpus:
    kor_raw_corpus.append(ko_preprocess_sentence(kor))
    eng_raw_corpus.append(en_preprocess_sentence(eng,s_token=True, e_token=True))

st.table(kor_raw_corpus)
st.table(eng_raw_corpus)


