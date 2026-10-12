import streamlit as st

st.set_page_config(page_title="TexColorGuard - 25TE008", layout="centered")
st.title("TexColorGuard - 25TE008")
st.write("Text Color Guard - Color Contrast & Safety Checker")

text_color = st.color_picker("Select Text Color", "#000000")
bg_color = st.color_picker("Select Background Color", "#FFFFFF")

sample_text = st.text_input("Enter your text here:", "Hello World! This is TexColorGuard.")

st.markdown("### Preview:")
st.markdown(
    f'<div style="background-color:{bg_color}; color:{text_color}; padding:30px; border-radius:10px;">{sample_text}</div>',
    unsafe_allow_html=True
)
st.success("File ready for deployment!")
