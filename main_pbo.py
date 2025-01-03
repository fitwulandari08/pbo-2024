# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py
# ini kontribusi dari wulandari
# main_pbo.py


from modul_satu_pbo import Film, Jadwal, Pemesanan
# Buat beberapa film
film1 = Film("Avatar: The Way of Water", 192, "Fiksi Ilmiah")
film2 = Film("Spider-Man: No Way Home", 148, "Aksi")

# Jadwal
jadwal1 = Jadwal(film1, "13:30")
jadwal2 = Jadwal(film2, "16:00")

# Pemesanan
sistem_pemesanan = Pemesanan()

print(film1.tampilkan_info())
print(film2.tampilkan_info())
print(jadwal1.tampilkan_jadwal())
print(jadwal2.tampilkan_jadwal())

# Pemesanan tiket
print(sistem_pemesanan.pesan_tiket(jadwal1, 2))
print(sistem_pemesanan.pesan_tiket(jadwal2, 4))

# Tampilkan riwayat pemesanan
print(sistem_pemesanan.tampilkan_riwayat())

