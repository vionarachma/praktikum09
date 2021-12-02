namaMhs = []
nimMhs = []
nTugasMhs = []
utsMhs = []
uasMhs = []
seluruh = []

sedangkan any:
    nama = input('Nama : ')
 namaMhs. append(nama)
 nim = int(input('NIM : '))
 nimMhs. append(nim)
    nTugas = float(input('Nilai Tugas : '))
 nTugasMhs. append(nTugas)
 uts = float(input('Nilai UTS : '))
 utsMhs. append(uts)
    uas = float(input('Nilai UAS : '))
 uasMhs. append(uas)

    nAkhir = (int(nTugas) * .3) + (int(uts) * .35) + (int(uas) * .35)
 total. append(nAkhir)

    lagi = ''
 sementara lagi != 'y' dan lagi != 't':
        lagi = input('Tambah data (y/t)? ')
 jika lagi == 't':
 cetak('='*70)
 Cetak('| Tidak ada | \t Nama\t | NIM | Tugas | | UTS UAS | Akhir |')
 cetak('='*70)

 for i in range(len(nimMhs)):
 nm = '| %d. | \t%s\t' % (i+1, namaMhs[i])
            im = '    | %d' % nimMhs[i]
 tg = ' | %.2f' % nTugasMhs[i]
 ut = ' | %. 2f' % utsMhs[i]
 ua = ' | %.2f' % uasMhs[i]
 ah = ' | %.2f' % total[i]
            ln = '   |'

 bergabung = nm + im + tg + ut + ua + ah + ln
 cetak(bergabung)

        pecah