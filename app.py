 import streamlit as st

st.set_page_config(page_title="عِلسان المغربي", page_icon="🇲🇦")

st.title("عِلسان المغربي 🇲🇦")
st.write("الله الوطن الملك")

st.success("مرحبا بك! عِلسان كيتوجد باش يخدم على الإنترنت.")

nom = st.text_input("شنو سميتك؟")

if st.button("سَلّم على عِلسان"):
    if nom:
        st.write(f"مرحبا {nom}! أنا عِلسان المغربي.")
    else:
        st.warning("كتب سميتك أولا.")
