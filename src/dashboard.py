import streamlit as st
import pandas as pd
import plotly.express as px # 동적 그래프를 위해 사용합니다.

# 1. 대시보드 제목
st.title("📊 고객 세분화 분석 대시보드")

# 2. 데이터 불러오기
@st.cache_data # 데이터를 매번 새로 읽지 않도록 캐싱(저장)합니다.
def load_data():

    return pd.read_csv('./data/processed/rfm_with_clusters.csv')


df = load_data()
st.write("컬럼 목록:", df.columns.tolist())
st.write("상위 5행:", df.head())

# 3. 사이드바 - 필터 기능
st.sidebar.header("필터 설정")
selected_cluster = st.sidebar.multiselect("확인할 클러스터 선택", 
                                         options=df['Cluster'].unique(),
                                         default=df['Cluster'].unique())

filtered_df = df[df['Cluster'].isin(selected_cluster)]

# 4. 시각화 - R vs M 산점도 (누가 돈을 많이 쓰고 최근에 왔나?)
# 비유: 밤하늘의 별 중 가장 빛나는 별(VIP)이 어디 있는지 찾는 과정입니다.
fig = px.scatter(filtered_df, x='Recency', y='Monetary', 
                 color='Cluster', size='Frequency',
                 title="최근성 vs 구매 금액 분포")
st.plotly_chart(fig)

# 5. 데이터 표 출력
st.subheader("선택된 고객 리스트")
st.write(filtered_df)