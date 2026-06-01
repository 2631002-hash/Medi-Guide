import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Medi-Guide",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# CSS 스타일
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.title {
    font-size: 45px;
    font-weight: bold;
    color: #0f6cbd;
}

.subtitle {
    font-size: 20px;
    color: #555;
}

.box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result-box {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    border-left: 8px solid #0f6cbd;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 헤더
# -----------------------------
st.markdown('<div class="title">🩺 Medi-Guide</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI 기반 증상 분석 및 진료 가이드 시스템</div>', unsafe_allow_html=True)

st.warning("⚠️ 본 서비스는 의료 진단을 대체하지 않습니다. 증상이 지속되거나 심각할 경우 반드시 병원을 방문하세요.")

st.divider()

# -----------------------------
# 입력 영역
# -----------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 👤 사용자 정보")

    age = st.selectbox(
        "연령대",
        ["10대", "20대", "30대", "40대", "50대 이상"]
    )

    gender = st.selectbox(
        "성별",
        ["남성", "여성"]
    )

    body_part = st.selectbox(
        "통증 부위",
        ["머리", "목", "가슴", "복부", "등", "팔다리"]
    )

with col2:
    st.markdown("## 🩹 증상 입력")

    symptoms = st.multiselect(
        "동반 증상 선택",
        [
            "두통",
            "발열",
            "기침",
            "메스꺼움",
            "복통",
            "설사",
            "어지러움",
            "피로감",
            "호흡곤란",
            "흉통",
            "근육통"
        ]
    )

    pain = st.slider(
        "통증 강도",
        0,
        10,
        5
    )

    duration = st.number_input(
        "증상 지속 시간 (일)",
        min_value=1,
        max_value=30,
        value=1
    )

    detail = st.text_area(
        "추가 설명",
        placeholder="증상에 대해 자세히 입력하세요"
    )

st.divider()

# -----------------------------
# 분석 버튼
# -----------------------------
if st.button("🔍 증상 분석하기", use_container_width=True):

    severity = "경미"
    color = "success"
    disease = "일반 피로"
    department = "내과"
    guide = "충분한 휴식과 수분 섭취를 권장합니다."
    emergency = False

    # -----------------------------
    # 분석 로직
    # -----------------------------

    if duration >= 3:
        severity = "주의"

    if "발열" in symptoms and "기침" in symptoms:
        disease = "감기 또는 독감"
        department = "호흡기내과"
        guide = "충분한 휴식과 수분 섭취가 필요합니다."
        severity = "주의"

    if "복통" in symptoms and "설사" in symptoms:
        disease = "장염 가능성"
        department = "소화기내과"
        guide = "자극적인 음식을 피하고 수분을 충분히 섭취하세요."
        severity = "주의"

    if pain >= 7:
        severity = "위험"
        guide = "빠른 시일 내 병원 방문을 권장합니다."

    if pain == 10:
        severity = "응급"
        guide = "즉시 응급실 방문이 필요합니다."

    if "호흡곤란" in symptoms or "흉통" in symptoms:
        disease = "심혈관 또는 호흡기 질환 가능성"
        department = "응급의학과"
        if pain >= 3:
            severity = "응급"
            emergency = True
            guide = "즉시 응급실 방문이 필요합니다."

    # -----------------------------
    # 결과 출력
    # -----------------------------

    st.markdown("# 📋 분석 결과")

    if severity == "경미":
        st.success("🟢 현재 상태는 비교적 경미합니다.")

    elif severity == "주의":
        st.warning("🟡 진료가 권장되는 상태입니다.")

    elif severity == "위험":
        st.error("🟠 빠른 병원 방문이 필요합니다.")

    elif severity == "응급":
        st.error("🔴 응급 상황 가능성이 있습니다!")

    st.markdown("---")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 🦠 예상 질환")
        st.info(disease)

        st.markdown("### 🏥 추천 진료과")
        st.success(department)

    with col4:
        st.markdown("### 📌 행동 가이드")
        st.write(guide)

        st.markdown("### 📊 상태 정보")
        st.write(f"통증 강도: {pain}/10")
        st.write(f"지속 기간: {duration}일")

    st.markdown("---")

    # 위험도 바
    st.markdown("### 🚦 심각도 수준")

    if severity == "경미":
        st.progress(25)

    elif severity == "주의":
        st.progress(55)

    elif severity == "위험":
        st.progress(80)

    elif severity == "응급":
        st.progress(100)

    # 응급 상황 안내
    if emergency:
        st.error("🚑 즉시 119 또는 가까운 응급실을 방문하세요.")

    st.divider()

    # 추가 안내
    st.markdown("## 📖 건강 관리 팁")

    st.write("- 충분한 수면과 수분 섭취를 유지하세요.")
    st.write("- 증상이 악화되면 병원을 방문하세요.")
    st.write("- 자가 진단에만 의존하지 마세요.")

# 푸터
st.divider()
st.caption("© 2026 Medi-Guide | AI 기반 의료 보조 서비스")