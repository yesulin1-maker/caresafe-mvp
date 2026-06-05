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
st.subheader("공공서비스가 닿기 전, 보호자와 빠르게 연결되는 모바일 웹 기반 안전연결 서비스")

st.info(
"케어세이프는 공공서비스를 대신하지 않고, 공공서비스가 닿기 전 또는 공백 시간에 "
"보호자와 빠르게 연결되도록 돕는 MVP 실증용 화면입니다."
)

st.warning(
"본 화면은 의료 판단, 진단, 처방, 24시간 관제, 응급 출동을 제공하지 않습니다. "
"테스트 단계에서는 실명·실제 전화번호·실제 질병정보 대신 가상정보 사용을 권장합니다."
)

st.divider()

# -----------------------------

# 상단 지표 카드

# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("SOS 호출", f"{st.session_state.sos_count}건")
st.caption("대상자가 긴급 도움 요청을 누른 기록")

with col2:
    st.metric("QR 응급정보 열람", f"{st.session_state.qr_count}회")
st.caption("응급정보 화면을 확인한 기록")

with col3:
    st.metric("보호자 확인", f"{st.session_state.guardian_check_count}건")
st.caption("보호자가 알림을 확인한 기록")

with col4:
st.metric("마지막 신호", "3분 전")
st.caption("시범기기 또는 웹 사용 흐름 기준")

st.divider()

# -----------------------------

# 탭 구성

# -----------------------------

tab1, tab2, tab3 = st.tabs(
["👵 어르신용 화면", "🆘 QR 응급정보", "👨‍👩‍👧 보호자 대시보드"]
)

# -----------------------------

# 1. 어르신용 화면

# -----------------------------

with tab1:
st.header("1. 어르신용 메인 화면")
st.write("혼자 계신 어르신이 위급하거나 불안할 때 보호자에게 빠르게 연락할 수 있는 화면입니다.")

```
target_name = st.text_input("대상자 이름", "홍길순")
target_age = st.number_input("나이", min_value=1, max_value=120, value=78)

risk_factor = st.selectbox(
    "주요 위험요인",
    [
        "퇴원 후 회복기",
        "독거 고위험 시니어",
        "복약 관리 필요",
        "야간 이동 위험",
        "낙상 우려",
        "보호자 비동거"
    ]
)

guardian_name = st.text_input("보호자 이름", "김보호")
guardian_phone = st.text_input("보호자 연락처", "010-0000-0000")

st.markdown("### 🔴 긴급 도움 요청")

if st.button("🚨 긴급 도움 요청", use_container_width=True):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.sos_count += 1
    st.session_state.logs.append(f"{now} - SOS 호출 버튼 클릭")
    st.error("SOS 호출이 접수되었습니다.")
    st.write("호출 시간:", now)
    st.write("보호자:", guardian_name)
    st.write("보호자 연락처:", guardian_phone)
    st.link_button("📞 보호자에게 전화하기", f"tel:{guardian_phone}")

st.markdown("### 📋 나의 약 정보 확인")
medicine = st.text_input("복약 정보", "혈압약 복용 중")
caution = st.text_input("주의사항", "당뇨 관리 필요")

st.markdown("### 🆔 나의 QR 응급정보")
st.write("QR 코드를 통해 보호자 연락처와 기본 응급정보를 확인할 수 있습니다.")
st.caption("실제 QR 생성 전 단계에서는 이 화면을 QR 응급정보 페이지 예시로 사용합니다.")
```

# -----------------------------

# 2. QR 응급정보

# -----------------------------

with tab2:
st.header("2. QR 응급정보 화면")
st.write("주변 사람이 QR을 확인했을 때 보호자 연락처와 기본 정보를 볼 수 있는 화면입니다.")

```
if st.button("QR 응급정보 열람 테스트", use_container_width=True):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.qr_count += 1
    st.session_state.logs.append(f"{now} - QR 응급정보 열람")
    st.success("QR 응급정보 열람 기록이 추가되었습니다.")

st.info(
    "이 화면은 의료 판단이 아니라 보호자 연락과 기본 정보 확인을 돕기 위한 참고 화면입니다."
)

st.markdown("### 대상자 정보")
st.write("대상자 이름: 홍길순")
st.write("나이: 78세")
st.write("주요 위험요인: 퇴원 후 회복기")

st.markdown("### 참고 건강정보")
st.write("복약 정보: 혈압약 복용 중")
st.write("주의사항: 당뇨 관리 필요")
st.write("알레르기: 테스트 정보 없음")

st.markdown("### 보호자 연락처")
st.write("보호자 이름: 김보호")
st.write("보호자 연락처: 010-0000-0000")

st.link_button("📞 보호자에게 전화하기", "tel:010-0000-0000")
```

# -----------------------------

# 3. 보호자 대시보드

# -----------------------------

with tab3:
st.header("3. 보호자 대시보드")
st.write("보호자가 SOS 호출, QR 열람, 복약·활동 확인, 대응 체크리스트를 확인하는 화면입니다.")

```
st.markdown("### ✅ 오늘 확인 항목")

medicine_check = st.checkbox("오늘 복약 확인")
activity_check = st.checkbox("오늘 기본 활동 확인")
call_check = st.checkbox("보호자 안부 확인 완료")

if medicine_check or activity_check or call_check:
    st.success("복약·활동 확인 기록이 반영되었습니다.")

st.markdown("### 🔔 최근 알림 기록")

if st.session_state.logs:
    for log in reversed(st.session_state.logs):
        st.write("-", log)
else:
    st.caption("아직 기록이 없습니다.")

st.markdown("### 🧭 보호자 대응 체크리스트")
st.write("응급 호출 발생 시 보호자가 순서대로 확인할 수 있는 기본 대응 흐름입니다.")

check1 = st.checkbox("1단계: 대상자에게 전화하기")
check2 = st.checkbox("2단계: 가까운 가족 또는 이웃에게 연락하기")
check3 = st.checkbox("3단계: 필요 시 119에 연락하기")
check4 = st.checkbox("4단계: QR 응급정보 확인하기")
check5 = st.checkbox("5단계: 대응 결과 기록하기")

if check1 and check2 and check3 and check4 and check5:
    st.session_state.guardian_check_count += 1
    st.success("보호자 대응 체크리스트가 모두 완료되었습니다.")

st.markdown("### 📌 선택정보")
with st.expander("선택정보 입력 보기"):
    blood_type = st.selectbox("혈액형", ["미입력", "A형", "B형", "O형", "AB형"])
    allergy = st.text_input("알레르기", "테스트 정보 없음")
    disease = st.text_input("기저질환 정보", "테스트 정보")
    hospital = st.text_input("주치의 / 병원", "테스트 병원")
    device = st.text_input("보조기기", "지팡이")
    advance_directive = st.selectbox(
        "사전연명의료의향서 등록 여부",
        ["미확인", "등록", "미등록"]
    )

    st.warning(
        "본 정보는 응급 상황에서 보호자 연락과 기본 정보 확인을 돕기 위한 참고 정보입니다. "
        "의료 판단을 대신하지 않으며, 테스트 단계에서는 가상정보 사용을 권장합니다."
    )
```

st.divider()

st.caption(
"CareSafe MVP | 보호자 등록 · SOS 호출 · QR 응급정보 · 복약/활동 확인 · 보호자 대응 체크리스트 실증용"
)
