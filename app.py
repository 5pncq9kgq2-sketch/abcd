import streamlit as st

# 웹 앱의 제목 설정
st.title("아주 쉬운 스트림릿 앱")

# 텍스트 표시
st.write("버튼을 눌러보세요!")

# 버튼 추가 및 클릭 이벤트 처리
if st.button("클릭!"):
    st.write("버튼이 클릭되었습니다! 🎉")
else:
    st.write("버튼 클릭 대기 중...")

