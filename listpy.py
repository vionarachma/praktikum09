Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> bahasa = ['Python', 'Java', 'Javascript', 'Dart', 'Kotlin']

# akses list
cetak('='*70)
cetak('DAFTAR AKSES')
cetak('='*70)
print('Elemen ke 3 adalah ', bahasa[3])
print('Nilai elemen ke 2 sampai ke 4 adalah ', bahasa[2:5])
print('Elemen terakhir adalah ', bahasa[-1])

# ubah element list
cetak('='*70)
print('UBAH ELEMEN LIST')
cetak('='*70)
print(bahasa)
bahasa[3] = 'c++'
print('Elemen ke 4 adalah ', bahasa[3])
print(bahasa)
bahasa[3:] = 'c#', 'PHP'
print(bahasa)

# tambah elemen list
cetak('='*70)
print('TAMBAH ELEMEN LIST')
cetak('='*70)
A = bahasa[0:2]
B = bahasa[2:]
cetak(A)
cetak(B)
B. append('Web')
cetak(B)
B. memperpanjang([1, 2, 3])
cetak(B)
B. memperpanjang(A)
cetak(B)