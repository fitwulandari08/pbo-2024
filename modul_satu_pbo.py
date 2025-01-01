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

class Sekolah:
    def _init_(self, nama_sekolah, alamat):
        self.nama_sekolah = nama_sekolah
        self.alamat = alamat
        self.guru = []
        self.siswa = []

    def tambah_guru(self, guru):
        self.guru.append(guru)
        print(f"Guru {guru.nama} berhasil ditambahkan ke {self.nama_sekolah}.")

    def tambah_siswa(self, siswa):
        self.siswa.append(siswa)
        print(f"Siswa {siswa.nama} berhasil ditambahkan ke {self.nama_sekolah}.")

    def daftar_guru(self):
        print(f"Daftar Guru di {self.nama_sekolah}:")
        for guru in self.guru:
            print(f"- {guru.nama}, Mata Pelajaran: {guru.mata_pelajaran}")

    def daftar_siswa(self):
        print(f"Daftar Siswa di {self.nama_sekolah}:")
        for siswa in self.siswa:
            print(f"- {siswa.nama}, Kelas: {siswa.kelas}")

class Guru:
    def _init_(self, nama, mata_pelajaran):
        self.nama = nama
        self.mata_pelajaran = mata_pelajaran

class Siswa:
    def _init_(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
