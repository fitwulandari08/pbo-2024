# modul projek bersama PBO untuk latihan Mahasiswa
# Mata Kulaih Pemrograman Berorientasi Objek (BPO)
# Semua Mahasiswa diharuskan berkontribusi pada modul ini
# Kontribusi berupa membuat class dan fungsi (lihat arahan lengkap di : https://infoummu.github.io/pbo/

# ini class test dari elyas: 
class test:
    def __init__(self, m):
        self.__m=m
    
    def mes(self):
        return self.__m;

# silahkan lanjutkan dengan fungsi dan calss anda dibawah
# pastikan untuk menguji class dan fungsi yang sudah di buat disini
# ini kontribusi dari wulandarai
# modul_satu_pbo.py

class Film:
    def __init__(self, judul, durasi, genre):
        self.judul = judul
        self.durasi = durasi  # Dalam menit
        self.genre = genre

    def tampilkan_info(self):
        return f"Film: {self.judul} | Durasi: {self.durasi} menit | Genre: {self.genre}"


class Jadwal:
    def __init__(self, film, waktu):
        self.film = film
        self.waktu = waktu  # Format: HH:MM

    def tampilkan_jadwal(self):
        return f"{self.film.judul} - Jam: {self.waktu}"


class Pemesanan:
    def __init__(self):
        self.riwayat_pemesanan = []

    def pesan_tiket(self, jadwal, jumlah_tiket):
        self.riwayat_pemesanan.append((jadwal, jumlah_tiket))
        return f"Berhasil memesan {jumlah_tiket} tiket untuk film '{jadwal.film.judul}' pada jam {jadwal.waktu}"

    def tampilkan_riwayat(self):
        if not self.riwayat_pemesanan:
            return "Belum ada pemesanan."

        hasil = "Riwayat Pemesanan:\n"
        for idx, (jadwal, jumlah_tiket) in enumerate(self.riwayat_pemesanan, start=1):
            hasil += f"{idx}. {jadwal.film.judul} - Jam {jadwal.waktu} - {jumlah_tiket} tiket\n"
        return hasil
