import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CareSafe MVP",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# 기본 데이터
# -----------------------------
if "sos_count" not in st.session_state:
    st.session_state.sos_count = 0

if "qr_count" not in st.session_state:
    st.session_state.qr_count = 0

if "guardian_check_count" not in st.session_state:
    st.session_state.guardian_check_count = 0

if "logs" not in st.session_state:
    st.session_state.logs = []

# -----------------------------
# 상단 제목
# -----------------------------
st.title("🛡️ 케어세이프 CareSafe MVP")
st.subheader("퇴원 직후 회복기 환자와 독거 고위험 시니어를 위한 안전연결 서비스")

st.write(
    "케어세이프는 응급 상황에서 대상자와 보호자를 빠르게 연결하고, "
    "QR 응급정보와 대응 체크리스트를 통해 돌봄 공백을 줄이는 모바일 웹 기반 MVP입니다."
)

st.divider()

# -----------------------------
# 핵심 지표
# -----------------------------
st.markdown("### 📊 실증 모니터링 지표")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("SOS 호출", f"{st.session_state.sos_count}건")

with col2:
    st.metric("QR 열람", f"{st.session_state.qr_count}건")

with col3:
    st.metric("보호자 확인", f"{st.session_state.guardian_check_count}건")

with col4:
    st.metric("마지막 신호", "3분 전")

st.divider()

# -----------------------------
# SOS 호출
# -----------------------------
st.markdown("### 🚨 SOS 응급 호출")

if st.button("🚨 SOS 호출하기", use_container_width=True):
    st.session_state.sos_count += 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.logs.append(f"{now} - SOS 호출 발생")
    st.error("SOS 호출이 보호자에게 전달되었습니다.")

# -----------------------------
# QR 응급정보
# -----------------------------
st.markdown("### 🧾 QR 응급정보")

with st.expander("QR 응급정보 확인하기"):
    st.session_state.qr_count += 1
    st.write("이름: 홍길동")
    st.write("나이: 78세")
    st.write("주요 질환: 고혈압, 당뇨")
    st.write("복용 약: 혈압약, 당뇨약")
    st.write("보호자 연락처: 010-0000-0000")
    st.write("주의사항: 낙상 위험, 어지럼증 있음")

# -----------------------------
# 보호자 대응 체크리스트
# -----------------------------
st.markdown("### ✅ 보호자 대응 체크리스트")

check1 = st.checkbox("1. 대상자에게 전화했습니다.")
check2 = st.checkbox("2. 복약 여부를 확인했습니다.")
check3 = st.checkbox("3. 활동 상태를 확인했습니다.")
check4 = st.checkbox("4. 필요 시 119 또는 가까운 가족에게 연락했습니다.")

if st.button("보호자 확인 완료", use_container_width=True):
    st.session_state.guardian_check_count += 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.logs.append(f"{now} - 보호자 확인 완료")
    st.success("보호자 확인 기록이 저장되었습니다.")

st.divider()

# -----------------------------
# 기록
# -----------------------------
st.markdown("### 📝 사용 기록")

if st.session_state.logs:
    for log in reversed(st.session_state.logs):
        st.write(log)
else:
    st.info("아직 기록이 없습니다.")

st.divider()

# -----------------------------
# 안내
# -----------------------------
st.markdown("### 📌 MVP 검증 목적")

st.write(
    "- SOS 호출 버튼을 보호자가 빠르게 확인할 수 있는지 검증합니다.\n"
    "- QR 응급정보가 실제 상황에서 이해하기 쉬운지 확인합니다.\n"
    "- 보호자 대응 체크리스트가 돌봄 공백 상황에서 도움이 되는지 검증합니다.\n"
    "- 초기 10~20명의 보호자를 대상으로 사용성, 응답률, 이해도, 구매의향을 확인합니다."
)
