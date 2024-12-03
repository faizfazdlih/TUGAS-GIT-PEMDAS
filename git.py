data_panen = {
    'lokasi1' : {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2' : {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450   
        }
    },
    'lokasi3' : {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600   
        }
    },
    'lokasi4' : {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550   
        }
    },
    'lokasi5' : {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480   
        }
    }
}

for i, j in data_panen.items():
    print(i,j)

lokasi2_jagung = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"\nJumlah hasil panen jagung dari lokasi 2 : {lokasi2_jagung}")

lokasi_3 = data_panen['lokasi3']['nama_lokasi']
print(f"\nNama dari lokasi 3 : {lokasi_3}")

padi = [i['hasil_panen']['padi'] for i in data_panen.values()]
kedelai = [i['hasil_panen']['kedelai'] for i in data_panen.values()]
print("\nHasil panen padi dari setiap lokasi : ", padi)
print("Hasil panen kedelai dari setiap lokasi : ", kedelai)

hasil_panen = [padi + kedelai for padi,kedelai in zip(padi, kedelai)]
print("\nTotal jumlah hasil panen padi dan kedelai setiap lokasi : ", hasil_panen)

for i, j in data_panen.items():
    padi = j['hasil_panen']['padi']
    jagung = j['hasil_panen']['jagung']
    nama_lokasi = j['nama_lokasi']

    if padi > 1300 or jagung > 800:
        print(f'\nLokasi {nama_lokasi} memerlukan perhatian khusus')
    else:
        print(f'\nLokasi {nama_lokasi} lokasi tersebut dalam kondisi baik')


print("INI COMMIT KEDUA")