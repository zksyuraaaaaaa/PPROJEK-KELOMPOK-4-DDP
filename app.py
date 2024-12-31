import streamlit as st
from streamlit_option_menu import option_menu
from kereta import *



# Contoh penggunaan
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Judul menu
        options=["Home","About", "kereta","Mobil","Motor"],  # Opsi menu
        icons=["house","info" "Train","car","motorcycle"],  # Ikon dari font-awesome
        menu_icon="cast",  # Ikon menu utama
        default_index=0,  # Indeks opsi default
        styles={
        "container": {"padding": "5px", "background-color": "#FFFFFF"},
        "icon": {"color": "brown", "font-size": "25px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "pink"},
        }
    )
    


# Menampilkan konten sesuai menu yang dipilih
if selected == "Home":
    st.title("Welcome To ")
    st.image("logoddp.jpg")

elif selected == "About":
    st.title("Tentang Move Master")
    st.write("Move Master dibuat untnuk memudahkan kita menentukan estimasi waktu, kecepatan maupun jarak yang akan kita tempuh. ")

    st.subheader("Aplikasi ini di rancang oleh :")
    st.write("1. Ayu Nur Intany", )
    st.write("2. Maulidya Syifa Aszahra")
    st.write("3. Safira Nur Azkia")
    
elif selected == "kereta": 
    st.title("Aplikasi Perhitungan Jarak, Kecepatan dan Waktu Kereta")
    st.image("kereta.jpg")
    
    def calculate_distance(speed, time):
        return speed * time

    def calculate_time(distance, speed):
        return distance / speed

    def calculate_speed(distance, time):
        return distance / time

    def calculate_multiple():
        st.subheader("Hitung Berulang")
        calculation_type = st.selectbox("Pilih jenis perhitungan", ["Jarak", "Waktu", "Kecepatan"])
        n = st.number_input("Masukkan jumlah perhitungan:", min_value=1, step=1, value=1)

        results = []

        for i in range(n):
            st.write(f"Perhitungan {i + 1}")
            if calculation_type == "Jarak":
                speed = st.number_input(f"Masukkan kecepatan kereta ke-{i + 1} (km/jam):", key=f"speed_{i}", min_value=0.0, step=1.0)
                time = st.number_input(f"Masukkan waktu tempuh ke-{i + 1} (jam):", key=f"time_{i}", min_value=0.0, step=1.0)
                if st.button(f"Hitung Jarak ke-{i + 1}", key=f"button_distance_{i}"):
                    distance = calculate_distance(speed, time)
                    st.write(f"Jarak yang ditempuh adalah {distance:.2f} km.")
                    results.append(distance)

            elif calculation_type == "Waktu":
                distance = st.number_input(f"Masukkan jarak tempuh ke-{i + 1} (km):", key=f"distance_{i}", min_value=0.0, step=1.0)
                speed = st.number_input(f"Masukkan kecepatan kereta ke-{i + 1} (km/jam):", key=f"speed_time_{i}", min_value=0.0, step=1.0)
                if st.button(f"Hitung Waktu ke-{i + 1}", key=f"button_time_{i}"):
                    if speed > 0:
                        time = calculate_time(distance, speed)
                        st.write(f"Waktu yang dibutuhkan adalah {time:.2f} jam.")
                        results.append(time)
                    else:
                        st.error("Kecepatan harus lebih dari 0.")

            elif calculation_type == "Kecepatan":
                distance = st.number_input(f"Masukkan jarak tempuh ke-{i + 1} (km):", key=f"distance_speed_{i}", min_value=0.0, step=1.0)
                time = st.number_input(f"Masukkan waktu tempuh ke-{i + 1} (jam):", key=f"time_speed_{i}", min_value=0.0, step=1.0)
                if st.button(f"Hitung Kecepatan ke-{i + 1}", key=f"button_speed_{i}"):
                    if time > 0:
                        speed = calculate_speed(distance, time)
                        st.write(f"Kecepatan kereta adalah {speed:.2f} km/jam.")
                        results.append(speed)
                    else:
                        st.error("Waktu harus lebih dari 0.")

        return results

    def main():
        

        menu = ["Hitung Satu Kali", "Hitung Berulang"]
        choice = st.sidebar.selectbox("Pilih opsi", menu)

        if choice == "Hitung Satu Kali":
            st.subheader("Hitung Satu Kali")
            single_calculation()
        elif choice == "Hitung Berulang":
            calculate_multiple()

    def single_calculation():
        calculation_type = st.radio("Pilih jenis perhitungan", ["Jarak", "Waktu", "Kecepatan"])

        if calculation_type == "Jarak":
            speed = st.number_input("Masukkan kecepatan kereta (km/jam):", min_value=0.0, step=1.0)
            time = st.number_input("Masukkan waktu tempuh (jam):", min_value=0.0, step=1.0)
            if st.button("Hitung Jarak"):
                distance = calculate_distance(speed, time)
                st.success(f"Jarak yang ditempuh adalah {distance:.2f} km.")

        elif calculation_type == "Waktu":
            distance = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0, step=1.0)
            speed = st.number_input("Masukkan kecepatan kereta (km/jam):", min_value=0.0, step=1.0)
            if st.button("Hitung Waktu"):
                if speed > 0:
                    time = calculate_time(distance, speed)
                    st.success(f"Waktu yang dibutuhkan adalah {time:.2f} jam.")
                else:
                    st.error("Kecepatan harus lebih dari 0.")

        elif calculation_type == "Kecepatan":
            distance = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0, step=1.0)
            time = st.number_input("Masukkan waktu tempuh (jam):", min_value=0.0, step=1.0)
            if st.button("Hitung Kecepatan"):
                if time > 0:
                    speed = calculate_speed(distance, time)
                    st.success(f"Kecepatan kereta adalah {speed:.2f} km/jam.")
                else:
                    st.error("Waktu harus lebih dari 0.")

    if __name__ == "__main__":
        main()
    
elif selected == "Mobil":
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
elif selected == "Motor":
    st.title("Aplikasi Perhitungan Jarak dan Kecepatan Motor")
    st.image("motor.jpg")

    # Fungsi untuk menghitung jarak
    def hitung_jarak(kecepatan, waktu):
        return kecepatan * waktu

    # Fungsi untuk menghitung kecepatan
    def hitung_kecepatan(jarak, waktu):
        return jarak / waktu

    # Fungsi untuk menghitung waktu
    def hitung_waktu(jarak, kecepatan):
        return jarak / kecepatan

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