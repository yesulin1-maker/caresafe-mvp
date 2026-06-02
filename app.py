import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CareSafe MVP",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ 케어세이프 CareSafe MVP")
st.subheader("공공서비스가 닿기 전, 보호자가 직접 활용할 수 있는 안전연결 흐름")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("SOS 호출", "0건")
    st.caption("대상자가 응급 상황에서 호출한 기록")

with col2:
    st.metric("QR 응급정보 열람", "0회")
    st.caption("보호자·응급 대응자가 확인한 열람 기록")

with col3:
    st.metric("보호자 확인", "0건")
    st.caption("알림 확인 및 대응 여부")

st.divider()

st.header("1. 대상자 기본 정보")

name = st.text_input("대상자 이름", "홍길순")
age = st.number_input("나이", min_value=1, max_value=120, value=78)
risk = st.selectbox(
    "주요 위험 요인",
    ["퇴원 직후 회복기", "독거 고위험 시니어", "복약 관리 필요", "야간 이동 위험", "낙상 우려"]
)

st.header("2. 보호자 정보")

guardian = st.text_input("보호자 이름", "김보호")
phone = st.text_input("보호자 연락처", "010-0000-0000")

st.header("3. 응급 상황 기록")

sos = st.button("🚨 SOS 호출 테스트")

if sos:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.error("SOS 호출이 접수되었습니다.")
    st.write(f"호출 시간: {now}")
    st.write(f"대상자: {name}")
    st.write(f"보호자 연락처: {phone}")

st.header("4. QR 응급정보")

with st.expander("QR 응급정보 보기"):
    st.write("대상자명:", name)
    st.write("나이:", age)
    st.write("위험 요인:", risk)
    st.write("보호자:", guardian)
    st.write("보호자 연락처:", phone)
    st.warning("이 화면은 실제 의료 판단이 아니라, 응급정보와 기본 대응 절차 확인을 돕는 MVP 예시입니다.")

st.divider()

st.caption("CareSafe MVP | 모바일 웹 기반 안전연결 흐름 검증용 화면")