from google_trans_new import google_translator
import streamlit as streamlit
translator = google_translator()
streamlit. title("Language Translator")
text = st.text_input("Enter a text")
translate = translator.translate(text, lang_tgt='fr')
st.write(translate)

