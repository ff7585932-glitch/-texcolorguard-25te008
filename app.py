import streamlit as st

st.set_page_config(page_title="TexColorGuard - 25TE008", layout="centered")

st.title("TexColorGuard - 25TE008")
st.write("Text Color Guard - Color Contrast & Safety Checker")

text_color = st.color_picker("Text Color chunno", "#000000")
bg_color = st.color_picker("Background Color chunno", "#FFFFFF")

sample_text = st.text_input("Apna text yahan likho:", "Hello World! This is TexColorGuard.")

st.markdown("### Preview:")
st.markdown(
    f'<div style="background-color:{bg_color}; color:{text_color}; padding:20px; border-radius:10px; border:1px solid #ccc;">{sample_text}</div>',
    unsafe_allow_html=True
)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

r1, g1, b1 = hex_to_rgb(text_color)
r2, g2, b2 = hex_to_rgb(bg_color)

st.write(f"Text RGB: {r1}, {g1}, {b1}")
st.write(f"Background RGB: {r2}, {g2}, {b2}")

st.success("File ready for deployment!")
