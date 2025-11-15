import streamlit as st

# 앱 제목 설정
st.title("아주 쉬운 스트림릿 예제")

# 텍스트 입력 위젯 추가
user_name = st.text_input("이름을 입력하세요:", "여기에 입력하세요")

# 버튼 추가
if st.button("인사하기"):
    st.write(f"안녕하세요, {user_name}님! Streamlit 앱에 오신 것을 환영합니다.")
else:
    st.write("위에 이름을 입력하고 버튼을 눌러보세요.")

# 슬라이더 예제 추가
st.subheader("슬라이더 예제")
age = st.slider("나이를 선택하세요:", 0, 100, 25)
st.write(f"선택한 나이: {age}세")

