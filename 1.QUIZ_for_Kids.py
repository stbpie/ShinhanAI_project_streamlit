# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:43:40 2023

@author: NADA
"""
# 유형부분 집계 추가 완료
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import os
import openai
import streamlit as st
import re

page_no = "1"
url = f"https://sgsg.hankyung.com/sgplus/quiz?page={page_no}"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"} #google에 user agent string 검색
quiz_link = requests.get(url, headers = headers)
html = bs(quiz_link.text, 'html.parser')

data = []
for p in html.find_all('p'):
    data.append(p.text)

dfs = []

# 리스트를 데이터프레임으로 변환
for a in range(0,5):
    df_a = pd.DataFrame(data, columns=['text'])
    
    df_a = pd.DataFrame(df_a['text'][2:-1])
    
    temp_a = df_a['text'].iloc[a]
    temp_a = temp_a.split('?')
    
    question = []
    answer_list = []
    temp_a = df_a['text'].iloc[a]
    question.append(temp_a.split('?')[0] + '?')
    answer_list.append(temp_a.split("?")[1].split('.')[0][:-1])
    question.append(temp_a.split("?")[1].split('.')[1] + '?')
    answer_list.append(temp_a.split("?")[2].split('.')[0][:-1])
    
    question = []
    answer_list = []
    answer = []
    
    # 첫번째 질문 저장 
    temp_a = df_a['text'].iloc[a]
    question.append(temp_a.split('?')[0] + '?')
    
    # 첫번째 문제부터 마지막 문제까지만 저장 
    for i in range(1, len(temp_a.split('?'))-1):
        answer_list.append(temp_a.split("?")[i].split('.')[0][:-1])
        question.append(temp_a.split("?")[i].split('.')[1] + '?')
    
    # 마지막 문제
    answer_list.append(temp_a.split('?')[-1].split('▶')[0])
    
    # 정답 처리
    a = temp_a.split('?')[-1].split('▶')[1]
    a = a.replace(' ①', '①').replace(' ②', '②').replace(' ③', '③').replace(' ④', '④')
    answer = a.split(' ')[2:]

    df_a = pd.DataFrame()
    df_a['질문'] = question
    df_a['보기 답'] = answer_list
    df_a['답'] = answer
    
    dfs.append(df_a)  # 생성된 데이터프레임을 리스트에 추가


result = pd.concat(dfs)

result = result.reset_index(drop = True)
for i in result.index:
  result.loc[i, '답'] = result.loc[i, '답'][-1]


 
result.loc[result['답'] == '①', '답'] = 1
result.loc[result['답'] == '②', '답'] = 2

num = 1
for i in ['①', '②', '③', '④']:
  result.loc[result['답'] == i, '답'] = num
  num += 1
result['질문'].iloc[0] = result['질문'].iloc[0][2:]

result['답'] = pd.to_numeric(result['답'], errors='coerce')

result['유형'] = ['정치', '규제', '시사', '개념', '개념', '정치', '정치', '정치', '개념', '정치',
                 '정치', '금융', '금융', '개념', '금융', '개념', '개념', '개념', '개념', '시사',
                 '정치', '개념', '개념', '개념', '정치', '정치', '정치', '개념', '금융', '시사',
                 '금융', '개념', '개념', '정치', '금융', '개념', '정치', '금융', '금융', '개념']


# result인덱스 리셋
result.reset_index(drop=True, inplace=True)

# api key 가져오기
os.environ.get("jiji.api_key")
openai.api_key = os.environ["jiji.api_key"]

st.title("Quiz Program")

def display_question(index):
    question_number = index + 1
    st.write(f"{question_number}번 문제:")
    question_area = st.empty()
    answer_area = st.empty()

    random_question = result.loc[index:index, :]
    qa = random_question['질문'].values[0]
    dat = random_question['보기 답'].iloc[0]

    pattern1 = r"① (.*?)② (.*?)③ (.*?)④ (.*?)$"
    pattern2 = r"①(.*?)②(.*?)③(.*?)④(.*?)$"

    match1 = re.search(pattern1, dat)
    match2 = re.search(pattern2, dat)

    if match1:
        select1, select2, select3, select4 = match1.group(1), match1.group(2), match1.group(3), match1.group(4)
    elif match2:
        select1, select2, select3, select4 = match2.group(1), match2.group(2), match2.group(3), match2.group(4)
    else:
        print("일치하는 패턴을 찾을 수 없습니다.")
        select1, select2, select3, select4 = None, None, None, None

    qc = random_question['답'].values[0]
    tata = {'Select1': [select1], 'Select2': [select2], 'Select3': [select3], 'Select4': [select4]}
    options_df = pd.DataFrame(tata)
    correct_answer = options_df.iloc[0, qc - 1]

    question_area.write(qa)
    answer = answer_area.radio("답을 고르세요.", [select1, select2, select3, select4], key=index)
    st.write(f"선택한 답: {answer}")

    return answer, correct_answer, qa, select1, select2, select3, select4, random_question['유형'].values[0]

def next_question():
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    st.session_state.current_index += 1
    if st.session_state.current_index >= len(result):
        st.session_state.current_index = 0

def check_answer(selected_answer, correct_answer, question_type):
    if "num_correct" not in st.session_state:
        st.session_state.num_correct = 0
    if "correct_by_type" not in st.session_state:
        st.session_state.correct_by_type = {}
    if "total_by_type" not in st.session_state:
        st.session_state.total_by_type = {}

    if question_type not in st.session_state.correct_by_type:
        st.session_state.correct_by_type[question_type] = 0
    if question_type not in st.session_state.total_by_type:
        st.session_state.total_by_type[question_type] = 0

    st.session_state.total_by_type[question_type] += 1

    if selected_answer == correct_answer:
        st.session_state.num_correct += 1
        st.session_state.correct_by_type[question_type] += 1
        st.write("정답입니다!")
    else:
        st.write("틀렸습니다. 다시 시도해보세요.")
        st.write(f"현재까지 맞춘 문제 수: {st.session_state.num_correct}")
    # st.write(f"유형별 정답 수: {st.session_state.correct_by_type}")

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

answer, correct_answer, qa, select1, select2, select3, select4, question_type = display_question(st.session_state.current_index)

col1, col2, col3 = st.columns([0.045, 0.35, 0.05])  # 이 부분을 수정하여 세 개의 컬럼을 생성하고, 각 컬럼의 너비를 조절합니다.

submit_button = col1.button("제출")  # col1에 '제출' 버튼을 추가합니다.
next_button = col2.button("다음")  # col2에 '다음' 버튼을 추가합니다.
explain_button = col3.button("해설보기")  # col3에 '해설보기' 버튼을 추가합니다.

if submit_button:
    check_answer(answer, correct_answer, question_type)

if next_button:
    next_question()
    st.experimental_rerun()  # 현재 스크립트를 다시 실행합니다. 이렇게 하면 문제와 보기가 갱신됩니다.

if explain_button:
    response = openai.Completion.create(
        model="text-davinci-003",  # text-davinci-003라는 모델을 사용.
        prompt="질문 : {0}과  보기 : {1},{2},{3},{4} 그리고 답 : {5} 를 활용해 문제를 풀고 간략하게 설명해주세요".format(qa, select1, select2, select3, select4, correct_answer),
        temperature=1,  # 0으로 되어있었음
        max_tokens=2000,  # 높을수록 말이 길게 나온다.
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    st.write(response['choices'][0]['text'].strip())

# 질문 입력 위젯 생성
input_box = st.sidebar.text_input("질문을 입력하세요:")

# 버튼 생성
button = st.sidebar.button("답변 확인")

if button:
    response = openai.Completion.create(
      model="text-davinci-003", # text-davinci-003라는 모델을 사용.
      prompt="{0}을 어린이가 이해할 수 있도록 쉽게 설명해주세요".format(input_box),
      temperature=1, # 0으로 되어있었음
      max_tokens=1000, # 높을수록 말이 길게 나온다.
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    st.sidebar.write(response['choices'][0]['text'].strip())

# 질문 입력 위젯이 스크롤을 내리면 따라 내려오도록 함
st.sidebar.markdown('<br><br><br><br><br>', unsafe_allow_html=True)

# 결과보기 버튼 추가
result_button = st.button("결과보기")

if result_button:
    st.write(f"전체 정답 수: {st.session_state.num_correct}")
    st.write("유형별 정답률:")

    for question_type in st.session_state.correct_by_type:
        correct_count = st.session_state.correct_by_type[question_type]
        total_count = st.session_state.total_by_type[question_type]
        accuracy = (correct_count / total_count) * 100
        st.write(f"{question_type}: {accuracy:.2f}%")