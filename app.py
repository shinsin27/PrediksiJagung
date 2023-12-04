import streamlit as st

# Judul aplikasi
st.title('Aplikasi Klasifikasi Tipe Jagung')
# Penjelasan aplikasi
st.write("""
Selamat datang di Aplikasi Klasifikasi Tipe Jagung. Aplikasi ini menggunakan teknologi 
machine learning untuk mengidentifikasi berbagai tipe jagung dari gambar yang diunggah. 
Dengan menggunakan algoritma klasifikasi canggih, aplikasi ini dapat membantu petani, 
peneliti, dan penggemar tanaman dalam mengklasifikasikan tipe jagung dengan mudah dan cepat.
""")

# Menambahkan beberapa penjelasan tambahan jika diperlukan
st.header('Cara Penggunaan')
st.write("""
- Unggah gambar jagung yang ingin Anda klasifikasikan.
- Tunggu hingga sistem memproses gambar.
- Lihat hasil klasifikasi yang ditampilkan oleh aplikasi.
""")