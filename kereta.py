import streamlit as st

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
    st.title("Perhitungan Kereta")

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
