import streamlit as st


# Judul aplikasi
st.title("Aplikasi Menghitung Jarak, Kecepatan, dan Waktu pada Mobil")
st.image("iconcar.jpg")

# Pilihan jenis mobil
car_type = st.selectbox(
    "Pilih jenis mobil:",
    ["mobil bensin", "mobil diesel", "mobil hybrid"]
)

# Faktor efisiensi (contoh, hanya untuk simulasi)
efficiency_factor = {
    "mobil bensin": 1.0,
    "mobil diesel": 0.9,
    "mobil hybrid": 0.8,
}

def calculate_distance(speed, time, efficiency):
    return speed * time * efficiency

def calculate_speed(distance, time, efficiency):
    return (distance / time) / efficiency

def calculate_time(distance, speed, efficiency):
    return (distance / speed) * efficiency

# Pilihan perhitungan
calculation_type = st.selectbox(
    "Pilih apa yang ingin dihitung:",
    ["Jarak", "Kecepatan", "Waktu"]
)

# Input data berdasarkan pilihan
if calculation_type == "Jarak":
    st.header("Menghitung Jarak")
    speed = st.number_input("Masukkan kecepatan (m/s):", min_value=0.0, format="%.2f")
    time = st.number_input("Masukkan waktu (menit):", min_value=0.0, format="%.2f")
    if st.button("Hitung Jarak"):
        distance = calculate_distance(speed, time, efficiency_factor[car_type])
        st.success(f"Jarak (dengan faktor efisiensi {car_type}): {distance:.2f} meter")
elif calculation_type == "Kecepatan":
    st.header("Menghitung Kecepatan")
    distance = st.number_input("Masukkan jarak (meter):", min_value=0.0, format="%.2f")
    time = st.number_input("Masukkan waktu (menit):", min_value=0.0, format="%.2f")
    if st.button("Hitung Kecepatan"):
        if time > 0:
            speed = calculate_speed(distance, time, efficiency_factor[car_type])
            st.success(f"Kecepatan (dengan faktor efisiensi {car_type}): {speed:.2f} m/s")
        else:
            st.error("Waktu harus lebih besar dari nol.")
elif calculation_type == "Waktu":
    st.header("Menghitung Waktu")
    distance = st.number_input("Masukkan jarak (meter):", min_value=0.0, format="%.2f")
    speed = st.number_input("Masukkan kecepatan (m/s):", min_value=0.0, format="%.2f")
    if st.button("Hitung Waktu"):
        if speed > 0:
            time = calculate_time(distance, speed, efficiency_factor[car_type])
            st.success(f"Waktu (dengan faktor efisiensi {car_type}): {time:.2f} menit")
        else:
            st.error("Kecepatan harus lebih besar dari nol.")
