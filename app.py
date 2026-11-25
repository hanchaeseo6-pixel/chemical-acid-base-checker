import time
import streamlit as st

# 1. 리스트(list) 선언 - 산성 5종, 염기성 5종 총 10종 (snake_case 준수)
formulas = [
    "HCl", "H2SO4", "HNO3", "CH3COOH", "H2CO3",
    "NaOH", "KOH", "Ca(OH)2", "Mg(OH)2", "NH4OH"
]
names = [
    "염산", "황산", "질산", "아세트산(식초)", "탄산",
    "수산화나트륨", "수산화칼륨", "수산화칼슘", "수산화마그네슘", "수산화암모늄(암모니아수)"
]
acid_list = ["HCl", "H2SO4", "HNO3", "CH3COOH", "H2CO3"]
base_list = ["NaOH", "KOH", "Ca(OH)2", "Mg(OH)2", "NH4OH"]

# 2-1. 사용자 정의 함수(def) & 선택구조(if-elif-else) - 물질 판독
def check_substance(formula):
    if formula in acid_list:
        return "산성입니다", "수용액에서 수소 이온(H+)을 내놓기 때문입니다."
    elif formula in base_list:
        return "염기성입니다", "수용액에서 수산화 이온(OH-)을 내놓기 때문입니다."
    else:
        return "판독 불가", "목록에 없는 화학식입니다."

# 2-2. 사용자 정의 함수(def) & 선택구조(if-elif-else) - BTB 용액 가상 실험
def run_btb_experiment(formula):
    if formula in acid_list:
        return "#FFD700", "🟡 용액이 노란색으로 변했습니다! (산성 확인)"
    elif formula in base_list:
        return "#1E90FF", "🔵 용액이 파란색으로 변했습니다! (염기성 확인)"
    else:
        return "#E0F7FA", "반응을 확인할 수 없습니다."

# 3. Streamlit 웹 화면 구성
st.title("🧪 화학식 기반 산성·염기성 물질 판독기")

# [기존 핵심 기능 유지] 산성·염기성 판독
selected = st.selectbox("판독할 화학식을 선택하세요:", formulas)
idx = formulas.index(selected)

if st.button("🔍 산성·염기성 판독하기"):
    result, reason = check_substance(selected)
    st.metric(label=f"선택한 화학식: {selected} ({names[idx]})", value=result)
    st.info(f"💡 **판독 이유:** {reason}")

st.divider()

# [BTB 용액 직접 실험 기능]
st.subheader(f"🧫 [{selected} ({names[idx]})] BTB 용액 가상 실험")
st.write("아래 버튼을 눌러 비커 속 수용액에 BTB 용액을 직접 떨어뜨려 보세요!")

if st.button("💧 BTB 용액 떨어뜨리기 (실험 실행)"):
    with st.spinner("BTB 용액을 떨어뜨려 색 변화를 관찰하는 중..."):
        time.sleep(0.6)
        
    liquid_color, exp_message = run_btb_experiment(selected)
    
    beaker_html = f"""
    <div style="display:flex; flex-direction:column; align-items:center; margin: 15px 0;">
        <div style="width:140px; height:165px; border:4px solid #555; border-top:none; border-radius:0 0 18px 18px; position:relative; background-color:#f9f9f9; overflow:hidden;">
            <div style="position:absolute; bottom:0; width:100%; height:110px; background-color:{liquid_color}; transition: background-color 0.5s;">
            </div>
        </div>
        <p style="margin-top:8px; font-weight:bold; color:#333;">[{selected} 수용액 + BTB 용액 비커]</p>
    </div>
    """
    st.markdown(beaker_html, unsafe_allow_html=True)
    st.success(f"**관찰 결과:** {exp_message}")

st.divider()

# 4. 반복구조(for)로 판독 가능한 물질 안내 표 출력
st.subheader("📋 판독 가능한 화학식 목록 (총 10종)")
info_list = []
for i in range(len(formulas)):
    info_list.append({
        "화학식": formulas[i],
        "물질명": names[i]
    })
st.table(info_list)
