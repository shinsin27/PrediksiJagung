import streamlit as st
from PIL import Image

st.header('''
Demo model klasifikasi
''')

uploaded_files = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_files is not None:
    st.success("File sukses diupload")
    image_upload = Image.open(uploaded_files)
    st.image(image_upload, caption="Gambar yang anda upload", use_column_width=True, width=200)
    

if st.button("Prediksi Gambar"):
    st.write("Hasil Prediksi")