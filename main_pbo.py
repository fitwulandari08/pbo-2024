# For Test using or import modul
# Main code untuk test modul projek bersama

import modul_satu_pbo as msatu

# ini contoh implementasi atau menguji fungsi dan class, versi saya
p = msatu.test("Halo.. This is the MMMMM ");
print ("\nTest Pesan : ", p.mes(), "\n")


# silahkan uji fungsi dan class anda dibawah
# pastikan class dan fungsi sudah anda buat di modul_satu_pbo.py

from modul1_pbo import Sekolah, Guru, Siswa
# Membuat objek Sekolah
sekolah = Sekolah("SMA Harapan Bangsa", "Jl. Pendidikan No. 10")

# Membuat objek Guru
guru1 = Guru("Budi Santoso", "Matematika")
guru2 = Guru("Siti Rahmawati", "Bahasa Inggris")

# Membuat objek Siswa
siswa1 = Siswa("Rina Putri", "10A")
siswa2 = Siswa("Andi Saputra", "10B")

# Menambahkan Guru dan Siswa ke Sekolah
sekolah.tambah_guru(guru1)
sekolah.tambah_guru(guru2)

sekolah.tambah_siswa(siswa1)
sekolah.tambah_siswa(siswa2)
