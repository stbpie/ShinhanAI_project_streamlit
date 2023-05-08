import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 



def pie_chart():
  import koreanize_matplotlib
    
  st.markdown('## 투자 형태에 대한 자산 배분 비율')
  st.markdown('### 성향 분석이 아닌 개개인의 선택에 맞추어 진단한다')
  st.markdown('*적금의 경우 적금과 주택청약의 비율을 8:2로 지정한다')
  st.markdown("1. 안정적인 적금형 = {적금:100}")
  st.markdown('2. 투자 맛보기형 = {적금:80, 안정적 투자:20}')
  st.markdown('3. 투자 즐기기형: = {적금:60, 안정적 투자:40}')
  st.markdown('4. 도전 즐기기형형 = {적금:60, 공격적 투자:40}')

  #num(투자 번호)에 따른 투자 포트폴리오 반환
  num = st.number_input('입력', 1, 4)
  if num == 1:
    ratio = [80, 20]
    labels = ['적금', '주택청약']
    colors = ['silver', 'gold']

    fig, ax = plt.subplots()
    ax.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, colors = colors,shadow=True)
    st.pyplot(fig)

  elif num == 2:
    ratio = [64, 16, 20]
    labels = ['적금', '주택청약', '투자']
    explode = [0.01, 0.01, 0.07]
    colors = ['silver', 'gold', 'whitesmoke']

    fig, ax = plt.subplots()
    ax.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode = explode, colors = colors, shadow=True)
    st.pyplot(fig)

  else:
    ratio = [48, 12, 40]
    labels = ['적금', '주택청약', '투자']
    explode = [0.01, 0.01, 0.07]
    colors = ['silver', 'gold', 'whitesmoke']

    fig, ax = plt.subplots()
    ax.pie(ratio, labels=labels, autopct='%.1f%%', startangle=260, counterclock=False, explode = explode, colors = colors, shadow=True)
    st.pyplot(fig)






def Investor_question():

  st.title('🚗청소년 투자자 성향 설문🚗')

  ans = st.text_input('투자 형태가 안정적인 적금형 {적금: 100}인가요? y/n')
  if (ans == 'n') or (ans == 'N'):
    st.markdown('#### 1. 고객님의 총 자산 규모(순자산)은 다음 중 어느 수준입니까?')
    st.markdown('(1)	10만원 미만')
    st.markdown('(2)	10만원 이상 ~ 70만원 미만')
    st.markdown('(3)	70만만원 이상 ~ 130만원 미만')
    st.markdown('(4)	130만원 이상 ~ 200만원 미만')
    st.markdown('(5)	200만원 이상')
    q1 = st.number_input('입력', 1, 5)
    
    st.markdown('#### 2. 고객님의 연간 소득액은 어떻게 되십니까?(대략 세뱃돈 포함하여)')
    #'https://www.mk.co.kr/news/economy/10723255' 이 기사를 참고하여 q2의 항목을 지정하였음
    st.markdown('(1)	50만원 미만')
    st.markdown('(2)	50만원 이상 ~ 90만원 미만')
    st.markdown('(3)	90만만원 이상 ~ 130만원 미만')
    st.markdown('(4)	130만원 이상 ~ 170만원 미만')
    st.markdown('(5)	200만원 이상')
    q2 = st.number_input('입력2', 1, 5)

    st.markdown('#### 3. 고객님이 선택하신 유형별 비중은 어떻게 되십니까?')
    st.markdown('(1) 투자 맛보기형 = {적금:80, 안정적 투자:20}')
    st.markdown('(2) 투자 즐기기형: = {적금:60, 안정적 투자:40}')
    st.markdown('(3) 도전 즐기기형 = {적금:60, 공격적 투자:40}') 
    q3 = st.number_input('입력3', 1, 5)
    
    st.markdown('#### 4. 투자해보신 경험이 있나요? 있다면 기간은?')
    st.markdown('(1) 있음, 1년 미만')
    st.markdown('(2) 있음, 1년 이상 ~ 3년미만')
    st.markdown('(3) 있음, 3년 이상') 
    st.markdown('(4) 없음') 
    q4 = st.number_input('입력4', 1, 5)
    
    st.markdown('#### 5. 고객님의 금융지식 수준(이해도)는 어느정도라고 생각하십니까?')
    st.markdown('(1) 금융투자상품에 투자해 본 경험이 없음')
    st.markdown('(2) 금융투자상품(주식 , 채권 및 펀드 등)의 구조 및 위험을 일정 부분 이해 ')
    st.markdown('(3) 금융투자상품(주식 , 채권 및 펀드 등)의 구조 및 위험을 깊이 있게 이해 ') 
    q5 = st.number_input('입력5', 1, 5)
    
    st.markdown('#### 6. 고객님의 금융투자상품 취득 및 처분 목적은 무엇입니까?')
    st.markdown('(1) 자산증식')
    st.markdown('(2) 교육과 경험')
    st.markdown('(3) 미래 자금') 
    q6 = st.number_input('입력6', 1, 5)
    
    st.markdown('#### 7. 고객님은 다음 중 어떤 목적으로 투자하는 편입니까?')
    st.markdown('(1) 투자 수익을 고려하나 원금 보존이 더 중요')
    st.markdown('(2) 원금 보존을 고려하나 투자 수익이 더 중요')
    st.markdown('(3) 손실 위험이 있더라도 투자 수익이 중요') 
    q7 = st.number_input('입력7', 1, 5)
    
    st.markdown('#### 8. 고객님께서 투자하고자 하는 자금의 투자예정 기간은 얼마나 되십니까?')
    st.markdown('(1) 3년 미만')
    st.markdown('(2) 3년 이상 ~ 5년 미만')
    st.markdown('(3) 5년 이상 ~ 7년 미만')
    st.markdown('(4) 7년 이상 ~ 10년 미만')
    st.markdown('(5) 10년 이상')
    q8 = st.number_input('입력8', 1, 5)
    
    st.markdown('#### 9. 고객님께서 금융상품 투자를 통해 기대하는 수익과 감수할 수 있는 손실을 가장 잘 표현한 것은 어떤 것입니까?')
    st.markdown('(1) 위험도를 낮춰 시중 금리만큼의 수익')
    st.markdown('(2) 원금의 일부 손실을 감수 및 시중금리보다 조금 높은 수익')
    st.markdown('(3) 원금 손실을 감수하여 좀 더 높은 수익을 기대') 
    st.markdown('(4) 원금을 많이 잃더라도 더 높은 수익 추구') 
    q9 = st.number_input('입력9', 1, 5)


    #설문지를 바탕으로 투자자 성향 점수내기
    #q1과 q2는 q1을 q2로 나눈 값을 다섯 단계로 나누어 점수 배분분 
    sum = 0
    if q1/q2 <0.25:
        sum += 1
    elif q1/q2 <0.5:
        sum += 2
    elif q1/q2 <0.75:
        sum += 3
    else: 
        sum += 4

    #q3
    if q3 == 1:
        sum += 0
    elif q3 == 2:
        sum += 2
    else:
        sum += 4 

    #q4
    if q4 == 1:
        sum += 1
    elif q4 == 2:
        sum += 2
    elif q4 == 3:
        sum += 3
    else:
        sum += 0

    #q5
    if q5 == 1:
        sum += 1
    elif q5 == 2:
        sum += 2
    else:
        sum += 3

    #q6
    if q6 == 1:
        sum += 4
    elif q6 == 2:
        sum += 0
    else:
        sum += 2

    #q7
    if q7 == 1:
        sum += 1.3
    elif q7 == 2:
        sum += 2.6
    else:
        sum += 4

    #q8 
    if q8 == 1:
        sum += 0.8
    elif q8 == 2:
        sum += 1.6
    elif q8 == 3:
        sum += 2.4
    elif q8 == 4:
        sum += 3.2
    else:
        sum += 4 

    #q9
    if q8 == 1:
        sum += 0
    elif q8 == 2:
        sum += 1
    elif q8 == 3:
        sum += 2
    elif q8 == 4:
        sum += 3
    else:
        sum += 4

    sum = round(sum, 2)
    if sum < 10:
        투자형태 = '안정형'
    elif sum < 20:
        투자형태 = '위험중립형'
    else:
        투자형태 = '공격투자형'
    st.write(' \n ### 당신의 점수는 {}점이며'.format(sum))
    st.write('## 투자자형태는 {}입니다'.format(투자형태))
    
    return 투자형태
    
    
    

  else:
    st.write('## 적금형은 투자자 성향 분석이 필요 없습니다!')
    
    
    
    
    
def portfolio(df, 투자형태):
  df['safe_grade'] = 0
  df.loc[df['Sharpe Ratio'] >= 3, 'safe_grade'] = 3
  df.loc[df['Sharpe Ratio'] < 3, 'safe_grade'] = 2
  df.loc[df['Sharpe Ratio'] < 2, 'safe_grade'] = 1


  if 투자형태 == '위험중립형':
    return st.experimental_data_editor(df.loc[df['safe_grade'] == 2, 'Portfolio'])
  elif 투자형태 == '안정형':
    return st.experimental_data_editor(df.loc[df['safe_grade'] == 3, 'Portfolio'])
  else:
    return st.experimental_data_editor(df.loc[df['safe_grade'] == 1, 'Portfolio'])
    
    

pie_chart()


st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)


투자형태 = Investor_question()

df = pd.read_csv('23_.csv')


st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('### 🦉{}에게 추천하는 포트폴리오입니다🦉'.format(투자형태))

portfolio_df = portfolio(df,투자형태)