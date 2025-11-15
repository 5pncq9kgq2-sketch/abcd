import streamlit as st

st.title("간단한 덧셈 계산기")

# 사용자로부터 첫 번째 숫자 입력 받기
# st.number_input은 숫자를 입력받는 위젯입니다.
num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0, step=1.0)

# 사용자로부터 두 번째 숫자 입력 받기
num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0, step=1.0)

# 덧셈 결과 계산
result = num1 + num2

# 결과 출력
st.success(f"두 수의 합계는 {result}입니다.")

