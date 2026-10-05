import streamlit as st

# 網頁標題
st.title("課程回饋表單")

# 1. 姓名文字輸入欄位
name = st.text_input("姓名")

# 2. 科系下拉式選單
department = st.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"]
)

# 3. 課程滿意度 1~5 分
satisfaction = st.slider(
    "課程滿意度",
    min_value=1,
    max_value=5,
    value=3
)

# 4. 意見回饋文字輸入區
feedback = st.text_area("意見回饋")

# 5. 送出按鈕
if st.button("送出"):
    # 6. 按下送出後顯示訊息
    st.success("感謝您的回饋！")