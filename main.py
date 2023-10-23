# python case sensitive huruf besar dan kecil, spasi, tab, tanda kutip
# print = cetak
# variable = tempat menampung data
# NAMA = "Danni Adhyatma" #ini tipe data string mau petik satu atau petik dua sama sama string
# USIA = 21 #tipe data integer
# TINGGI_BADAN = 183.5 #tipe data float bilangan desimal
# PUNYA_PACAR = False #tipe data boolean penulisan true dan false di python itu case sensitive. Salah penulisan huruf kapital atau huruf kecil bisa error
# cara konversi tipe data string ke int int("21") ---> 21
# cara konversi tipe data int ke string str(21) ---> "21"
# cara konversi tipe data float float(5) ---> 5.0

# print('hey bro nama gue ' + NAMA)
# print('usia gue ' + str(USIA) + ' tahun')
# print('tinggi badan gue ' + str(TINGGI_BADAN) + " cm")
# print('punya pacar = ' + str(PUNYA_PACAR))
# print('hey bro nama gue ' + NAMA + ' usia gue ' + str(USIA) + ' tahun' + ' tinggi badan gue ' + str(TINGGI_BADAN) + " cm " + 'punya pacar = ' + str(PUNYA_PACAR))

# print(input('halo siapa nama kamu? ')) #memberikan inputan pada bahasa pemrograman python menggunakan function input
# print('siapa nama kucingmu?')
# input_nama_kucing = input()
# print(input_nama_kucing)
# pada bahasa pemrograman python function input mengembalikan nilai dalam bentuk tipe data string

# print('Halo siapa nama kamu?')
# input_nama = input()
# print('Halo siapa nama kucing kamu?')
# input_nama_kucing = input()
# print("Nama kamu " + input_nama + " " + "Nama kucing kamu " + input_nama_kucing)

# operator matematika + - * /
# a = 4
# print(a)
# print(':')
# b = 2
# print(b)

# c = a / b
# print(c)

# a = 9
# b = 2

# c = a / b  # tipe data yang dihasilkannya adalah float atau decimal
# print(c)

# logic di atas tanpa ada inputan dari user. tidak ada function input
# sekarang kita coba buat logic aritmatika menggunakan inputan dari user + - * /

# perlu diingat pengembalian nilai function input itu tipe data string
# a = input('masukan angka pertama: ')
# jadi perlu di konversi dlu pada saat melakukan operator aritmatika,
# pada variable yang menampung inputan dari user
# b = input('masukan angka kedua: ')
# c = int(a) / int(b)
# konversi variable ke int
# si variable c saat ini sudah menjadi tipe data int

# untuk operator (/) pembagian dalam bahasa pemrograman python ketika hasilnya di print,
# akan menghasilkan tipe data float atau desimal. maka pada saat memberikan operator bagi,
# perlu ada tambahan tanda bagi menjadi 2 seperti ini (//) agar hasil bagi tidak desimal
# akan dibulatkan ke bawah jika koma

# kalau mau di print hasil variable c dengan kalimat lain maka harus di konversi ke tipe data str
# print('hasilnya adalah: ' + str(c))


# saldo_awal = input('berapa saldo awalmu: ')  # input keluar jadi str
# deposit = input('berapa mau depositnya: ')  # input keluar jadi str

# munculkan output ke terminal console hasil setelah saldo awal lu di tambahkan dengan deposti

# hasil_penjumlahan = int(saldo_awal) + int(deposit)

# print('ini hasil setelah saldo awal di tambahkan dengan deposit: ' + str(hasil_penjumlahan))


# untuk kali ini kita belajar di string dlu aja
# nama_saya = "dea afrizal"

# print(nama_saya.find('l'))  # menggunakan function find pada variable
# function find ini artinya temukan huruf a ada di index ke berapa atau urutan ke berapa di mulai dari angka 0
# studi kasus di atas dia ngebaca string

# selain itu kita bisa mencari keberadaan huruf di variable menggunakan function in
# outputnya berupa true and false sama seperti tipe data boolean
# print('d' in nama_saya)

# untuk menentukan panjang dari variable dengan tipe data string
# kita bisa menggunakan function length() atau klo dalam bahasa pemrograman python itu len
# print(len(nama_saya))

# selain itu kita juga bisa menggunakan function upper() untuk merubah isi dari variable string
# dari huruf kecil ke huruf kapital
# print(nama_saya.upper())

# selain itu ada function yang bisa digunakan untuk merubah isi dari variable menjadi huruf kapital
# functionnya adalah capitalize()

# ada juga function count('value_from_variable') untuk menghitung jumlah huruf yang ditentukan
# di parameter
# print(nama_saya.count('3'))

# sekarang masuk ke perkondisian, untuk membuat perkondisian bisa menggunakan if,elif,else
# atau bisa switch/case
# usia = 20

# untuk komparasi atau perbandingan menggunakan sama dengannya dua kali ==
# == sama dengan
# > lebih dari
# < kurang dari
# '!=' tidak sama dengan
# <= kurang dari samadengan
# >= lebih dari samadengan

# untuk kasus statement >= maka angka di dalam variable yang sama dengan angka kondisinya
# itu memenuhi atau dianggap benar

# if usia <= 5:
#     print('usia anak Tk')
# elif usia <= 12:
#     print('usia anak esde')
# elif usia <= 15:
#     print('usia anak esempe')
# elif usia <= 18:
#     print('usia anak esema')
# else:
#     print('masuk usia dewasa')

# ada statement AND OR pada bahasa pemrograman python
# usia = input('masukkan usia: ')
# if int(usia) >= 5 and int(usia) <= 10:
#     print('masuk usia anak-anak')
# elif int(usia) >= 11 and int(usia) <= 20:
#     print('masuk usia remaja')
# else:
#     print('usia tidak masuk kategori')

# masuk ke materi looping

# sebelum masuk ke looping ada tipe data yang namanya array.
# array kumpulan value atau nilai nilai yang digabungkan dalam sebuah variable
# kalau array index dibaca dari 0. atau posisi dihitung mulai dari angka 0

# pacar_saya = ['nirina', 'agnes', 'angelica']

# print(pacar_saya[2])
# kita bisa juga menggunakan function len untuk mengetahui panjang data array
# atau jumlah data array
# print(len(pacar_saya))

# kalau kita ingin menampilkan hasil array dalam bentuk urutan ke bawah
# atau mencetak dalam bentuk baris ke bawah
# caranya menggunakan function for. for nama_variable_baru in nama_variable_lama:
# for pacar_kebawah in pacar_saya:
#     print(pacar_kebawah)

# sedikit catatan untuk di bahasa pemrograman python indent pada statement tertentu itu berpengaruh
# jadi perlu diperhatikan untuk indent pada statement yg memuat function tertentu

# misalkan ingin masuk ke looping standard tanpa array bisa menggunakan while
# AWAL = input('masukan nilai awal: ')

# dibawah merupakan syarat dari perulangan apabila sudah tidak memenuhi syarat maka tidak dicetak
# while int(AWAL) <= 10:
#     print(AWAL)
#     AWAL = int(AWAL) + 1
# penulisan nya bisa juga seperti ini: awal += 1

# cara membaca looping di atas adalah
# nilai variable awal yang di inputkan harus memenuhi syarat/kondisi
# ketika masuk ke looping while akan dibaca oleh syarat/kondisi perulangannya
# ketika masih memenuhi syarat maka nilai akan di cetak
# kemudian perulangan membaca lagi variable yang di update + 1 dibaca lagi oleh si perulangan while,
# tetapi
# jika nilai sudah tidak memenuhi/nilai melebihi syarat maka perulangan berhenti nilai tidak dicetak

# ada pr atau tugas dari dea afrizal
saldo_awal = 5000
deposit = input('berapa mau depositnya: ')

saldo_total = saldo_awal + int(deposit)
hutang = 50000


if (saldo_total) >= hutang:
    print('user bisa bayar hutang')
else:
    print('user tidak bisa bayar hutang')

# tampilkan pada terminal dengan mengimplementasikan konsep pengkondisian
# user bisa bayar hutang jika saldo user cukup atau lebih untuk membayar hutang
# user tidak bisa bayar hutang jika saldonya kurang
