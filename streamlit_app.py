import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="초등 6학년 그래프 만들기", page_icon="📊", layout="centered")
st.title("📊 초등학교 6학년을 위한 그래프 만들기")
st.write("다양한 데이터를 그래프로 보여주고, 그래프의 의미를 쉽게 배워볼 수 있어요.")

graph_option = st.sidebar.selectbox(
    "그래프 종류 선택",
    [
        "과일 판매량 막대그래프",
        "직접 막대그래프 그리기",
        "한 주간 기온 꺾은선그래프",
        "선호 과목 원형그래프",
        "공부 시간과 점수 산점도",
        "운동 시간 영역그래프",
    ],
)

if graph_option == "과일 판매량 막대그래프":
    st.header("🍎 과일 판매량 막대그래프")
    data = pd.DataFrame(
        {
            "과일": ["사과", "바나나", "오렌지", "포도"],
            "판매개수": [15, 22, 13, 9],
        }
    )
    chart = (
        alt.Chart(data)
        .mark_bar(color="#4C78A8")
        .encode(x=alt.X("과일", sort=None), y="판매개수")
        .properties(width=600, height=400)
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("이 그래프는 각 과일이 하루에 몇 개 팔렸는지를 보여줍니다.")

elif graph_option == "직접 막대그래프 그리기":
    st.header("✏️ 직접 막대그래프 그리기")
    st.write("아래에 원하는 항목 이름과 값을 입력하고 '그래프 만들기'를 눌러보세요.")

    with st.form("custom_bar_form"):
        cols = st.columns(2)
        item1 = cols[0].text_input("첫 번째 항목", "사과")
        value1 = cols[1].number_input("값 1", min_value=0, max_value=100, value=15)
        item2 = cols[0].text_input("두 번째 항목", "바나나")
        value2 = cols[1].number_input("값 2", min_value=0, max_value=100, value=22)
        item3 = cols[0].text_input("세 번째 항목", "오렌지")
        value3 = cols[1].number_input("값 3", min_value=0, max_value=100, value=13)
        item4 = cols[0].text_input("네 번째 항목", "포도")
        value4 = cols[1].number_input("값 4", min_value=0, max_value=100, value=9)
        submitted = st.form_submit_button("그래프 만들기")

    data = pd.DataFrame(
        {
            "항목": [item1, item2, item3, item4],
            "값": [value1, value2, value3, value4],
        }
    )

    chart = (
        alt.Chart(data)
        .mark_bar(color="#1F77B4")
        .encode(x=alt.X("항목", sort=None), y="값")
        .properties(width=600, height=400)
    )

    if submitted:
        st.altair_chart(chart, use_container_width=True)
        st.write("직접 입력한 데이터로 막대그래프가 만들어졌어요!")
    else:
        st.info("항목과 값을 입력한 뒤 '그래프 만들기' 버튼을 눌러주세요.")
        st.altair_chart(chart, use_container_width=True)

elif graph_option == "한 주간 기온 꺾은선그래프":
    st.header("🌤️ 한 주간 기온 꺾은선그래프")
    data = pd.DataFrame(
        {
            "요일": ["월", "화", "수", "목", "금", "토", "일"],
            "기온": [18, 20, 21, 19, 22, 23, 20],
        }
    )
    chart = (
        alt.Chart(data)
        .mark_line(point=True, color="#FF7F0E")
        .encode(x=alt.X("요일", sort=None), y="기온")
        .properties(width=600, height=400)
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("이 그래프는 한 주 동안 기온이 어떻게 변하는지를 보여줍니다.")

elif graph_option == "선호 과목 원형그래프":
    st.header("🎨 선호 과목 원형그래프")
    data = pd.DataFrame(
        {
            "과목": ["수학", "과학", "미술", "체육", "음악"],
            "학생 수": [10, 14, 8, 12, 6],
        }
    )
    chart = (
        alt.Chart(data)
        .mark_arc(innerRadius=50)
        .encode(
            theta=alt.Theta(field="학생 수", type="quantitative"),
            color=alt.Color(field="과목", type="nominal"),
            tooltip=["과목", "학생 수"],
        )
        .properties(width=600, height=400)
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("이 원형그래프는 어떤 과목을 좋아하는 학생이 많은지 보여줍니다.")

elif graph_option == "공부 시간과 점수 산점도":
    st.header("📚 공부 시간과 점수 산점도")
    data = pd.DataFrame(
        {
            "공부 시간(시간)": [1, 2, 3, 4, 5, 6, 7],
            "점수": [55, 62, 68, 75, 80, 85, 91],
        }
    )
    chart = (
        alt.Chart(data)
        .mark_circle(size=120, color="#2CA02C")
        .encode(
            x="공부 시간(시간)",
            y="점수",
            tooltip=["공부 시간(시간)", "점수"],
        )
        .properties(width=600, height=400)
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("이 산점도는 공부 시간과 시험 점수 사이의 관계를 보여줍니다.")

else:
    st.header("🏃 운동 시간 영역그래프")
    data = pd.DataFrame(
        {
            "요일": ["월", "화", "수", "목", "금", "토", "일"],
            "운동 시간(분)": [30, 25, 40, 20, 35, 50, 45],
        }
    )
    chart = (
        alt.Chart(data)
        .mark_area(color="#9467BD", opacity=0.5)
        .encode(x=alt.X("요일", sort=None), y="운동 시간(분)")
        .properties(width=600, height=400)
    )
    st.altair_chart(chart, use_container_width=True)
    st.write("이 영역그래프는 한 주 동안 운동한 시간을 보여줍니다.")

if st.checkbox("데이터 표 보기"):
    st.subheader("그래프에 사용된 데이터")
    st.dataframe(data)
