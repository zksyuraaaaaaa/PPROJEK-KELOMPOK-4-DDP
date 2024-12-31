import streamlit as st

# Fungsi untuk menghitung jarak
def hitung_jarak(kecepatan, waktu):
    return kecepatan * waktu

# Fungsi untuk menghitung kecepatan
def hitung_kecepatan(jarak, waktu):
    return jarak / waktu

# Fungsi untuk menghitung waktu
def hitung_waktu(jarak, kecepatan):
    return jarak / kecepatan

# Judul aplikasi
st.title("Aplikasi Perhitungan Jarak dan Kecepatan Motor")

# Pilihan mode perhitungan
mode = st.radio(
    "Pilih perhitungan yang ingin dilakukan:",
    ("Hitung Jarak", "Hitung Kecepatan", "Hitung Waktu")
)

if mode == "Hitung Jarak":
    st.subheader("Hitung Jarak")
    kecepatan = st.number_input("Masukkan kecepatan (km/jam):", min_value=0.0, step=0.1)
    waktu = st.number_input("Masukkan waktu perjalanan (jam):", min_value=0.0, step=0.1)
if st.button("Hitung Jarak"):
        if kecepatan > 0 and waktu > 0:
            jarak = hitung_jarak(kecepatan, waktu)
            st.success(f"Jarak yang ditempuh adalah {jarak:.2f} km.")
        else:
            st.error("Kecepatan dan waktu harus lebih besar dari 0.")

elif mode == "Hitung Kecepatan":
    st.subheader("Hitung Kecepatan")
    jarak = st.number_input("Masukkan jarak (km):", min_value=0.0, step=0.1)
    waktu = st.number_input("Masukkan waktu perjalanan (jam):", min_value=0.0, step=0.1)
    
    if st.button("Hitung Kecepatan"):
        if jarak > 0 and waktu > 0:
            kecepatan = hitung_kecepatan(jarak, waktu)
            st.success(f"Kecepatan rata-rata adalah {kecepatan:.2f} km/jam.")
        else:
            st.error("Jarak dan waktu harus lebih besar dari 0.")
        
elif mode == "Hitung Waktu":
    st.subheader("Hitung Waktu")
    jarak = st.number_input("Masukkan jarak (km):", min_value=0.0, step=0.1)
    kecepatan = st.number_input("Masukkan kecepatan (km/jam):", min_value=0.0, step=0.1)

    if st.button("Hitung Waktu"):
        if jarak > 0 and kecepatan > 0:
            waktu = hitung_waktu(jarak, kecepatan)
            st.success(f"Waktu perjalanan adalah {waktu:.2f} jam.")
        else:
            st.error("Jarak dan kecepatan harus lebih besar dari 0.")

else:
    st.write("Silakan pilih perhitungan yang ingin dilakukan.")