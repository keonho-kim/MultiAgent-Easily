import streamlit as st
import openai
from PIL import Image


st.set_page_config(
    page_title="VERIFY YOUR API KEY",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)


st.title("LOGIN")

hide_streamlit_logo = """
    <style>
    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header {visibility:hidden;}
    </style>
"""
st.markdown(hide_streamlit_logo, unsafe_allow_html=True)

st.markdown(
    """
OpenAI API Key는 다음의 링크에 접속하셔서 확인 하실 수 있습니다 😀 \n
[https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys)
"""
)

api_key = st.text_input(
    label="APIKEY",
    placeholder="OpenAI API KEY",
    type="password",
    label_visibility="hidden",
)
t00, t01, t02 = st.columns([3, 50, 3])
with t01:
    api_submit = st.button("로그인", key="submit_apikey")


if api_submit:
    st.session_state["api_type"] = "open_ai"
    st.session_state["api_key"] = api_key
    st.session_state["api_base"] = "https://api.openai.com/v1"
    st.session_state["api_version"] = "2020-11-07"

    openai.api_key = st.session_state["api_key"]
    openai.api_base = st.session_state["api_base"]
    openai.api_version = st.session_state["api_version"]
    openai.api_type = st.session_state["api_type"]

    openai.api_key = st.session_state["api_key"]
    openai.api_type = st.session_state["api_type"]
    openai.api_version = st.session_state["api_version"]
    openai.api_base = st.session_state["api_base"]
    try:
        with st.spinner("로그인 하는 중..."):
            st.session_state["model_list"] = [x.id for x in openai.Model.list().data]
        st.success("로그인 성공!")
        st.session_state["logined"] = True
    except:
        st.error("로그인에 실패하였습니다. API Key를 다시 확인해주세요.")
        st.session_state["logined"] = False
