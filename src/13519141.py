#open file
print("Selamat datang ke program untuk ngitung matkul apa aja yang bisa dihantam di tiap semesternya")
name = input("Masukkan nama file dengan format: 1.txt;2.txt;...;8.txt\n")
file = open("../test/"+name,"r")

# listall merupakan list yang berisi string per line dari file yang masuk
# contoh: c1, c2.
#         c2, c3.
#         c3.
# listall = ["c1 c2", "c2 c3", "c3"]
listall = []
isi = file.readlines()
for i in isi:
    temp = ""
    for j in i:
        if(j==','):
            continue
        elif(j=='.'or j=="\n"):
            break
        else:
            temp+=j
    listall.append(temp)

# matkul adalah jumlah matkul yang ada
matkul = len(listall)
# data adalah matriks yang menandakan relasi matkul dengan pre-requisitenya dengan komposisi
# baris = matkul, kolom = pre-requisite matkul tersebut
data = [[0 for x in range(matkul)] for y in range(matkul)]

# leter_count adalah panjang string dari nama matkul, contoh c1 = 2; if2211 = 6
letter_count = 0
for i in listall[0]:
    if (i==' '):
        break
    letter_count += 1

# individual adalah list matkul yang ada tanpa pre-requisitenya (olahan dari listall)
individual = []
for i in listall:
    temp = ""
    for j in range (letter_count):
        temp+= i[j]
    individual.append(temp)

# membentuk data dengan kondisi keadaan yang real (sinkronisasi dengan info dari file masukan)
for i in range (len(data)):
    # jika panjang string matkul + pre-req lebih dari panjang string matkul (berarti ada pre-req)
    if (len(listall[i])>letter_count):
        # menghitung jumlah pre-req dari suatu matkul
        prec_amount = 0
        for j in listall[i]:
            if(j==' '):
                prec_amount += 1
        # perulangan pre-req untuk mengisi matriks
        # cara kerjanya sebagai berikut
        prec_proc = 0
        while (prec_proc<prec_amount):
            for j in range (len(data[i])):
                correct = True
                # loop dari indeks awal string pre-req
                # perhatikan bahwa acuan yang digunakan untuk mendata pre-req adalah listall
                # pada contoh awal, listall = ["c1 c2", "c2 c3", "c3"], maka start = 3
                start = (letter_count+1)*(prec_proc+1)
                for k in range (letter_count):
                    # listall[i] dengan indeks start = 3
                    # maka "c2" akan dicek dengan masing-masing elemen dari list individual
                    if (listall[i][start]!=individual[j][k]):
                        correct = False
                        break
                    start += 1
                # jika cocok (posisi pre-req sama pada matriks untuk menandakan ada pre-req)
                # matriks akan diisi dengan 1
                if (correct):
                    data[i][j] = 1
                    prec_proc += 1
                    break
                # hasil akhir matriks dengan contoh listall = ["c1 c2", "c2 c3", "c3"],
                # individual = ["c1", "c2", "c3"]
                # 0 1 0
                # 0 0 1
                # 0 0 0
                # yang berarti c1 [indeks 0 - baris 1] memiliki pre-req c2 [indeks 1 - kolom 2]
                # c2 [indeks 1 - baris 2] memiliki pre-req c3 [indeks 2 - kolom 3]
                # c3 tidak memiliki pre-req
        # loop akan berjalan hingga pre-req yang terproses (terisi di matriks) sudah sesuai dengan
        # jumlah pre-req yang telah dikalkukasikan di awal (prec_amount)

# list sorted untuk topological sort                 
sorted = []
# current index untuk menandakan indeks sorted yang sedang digunakan
curr_index = 0
# count semester untuk keluaran
semester = 1

# akan dilakukan perulangan hingga matkul di list sorted berjumlah sama dengan jumlah matkul yang ada
while (len(sorted)<matkul):
    # gone menandakan matkul yang akan disalin dari list individual ke list sorted
    gone = []
    # proses sort dilakukan dengan memroses matriks yang telah dibuat
    for i in range (len(data)):
        clear = True
        visited = False
        # clear di sini menandakan bahwa seluruh kolom bernilai 0 (tidak memiliki pre-requisite)
        # perhatikan perulangan terus dilakukan pada baris matriks
        for j in range (len(data[i])):
            if (data[i][j]!=0):
                clear = False
        # setelah menemukan baris yang memiliki kolom dengan seluruh nilainya 0
        # akan dicek apakah sudah tercatat atau belum di list sorted
        if(clear):
            for k in sorted:
                if(k==individual[i]):
                    visited = True

        # jika clear dan belum ada di sorted maka matkul akan dimasukkan ke list sorted
        if(clear and not visited):
            sorted.append(individual[i])
            gone.append(i)

    # proses keluaran agar sesuai dengan spek
    while(curr_index<len(sorted)):
        # jika pada 1 semester dapat mengambil lebih dari 1 sks
        if(len(sorted)-curr_index>1):
            print("semester",semester,": ",end='')
            while(len(sorted)-curr_index>=1):
                print(sorted[curr_index],end='')
                curr_index += 1
                if(len(sorted)-curr_index>=1):
                    print(", ",end='')
            print()
        # jika hanya 1 sks yang dapat diambil pada semester tersebut
        else:
            print("semester",semester,":",sorted[curr_index])
            curr_index += 1

    # update count semester untuk keluaran
    semester += 1

    # karena matkul pada indeks gone sudah disalin ke list sorted
    # menandakan bahwa matkul telah diambil sehingga
    # dapat dianggap jumlah pre-req matkul lain yang bersangkutan ada yang berkurang
    for i in range (len(data)):
        for j in range (len(data[i])):
            for k in gone:
                if (j==k):
                    data[i][j] = 0
                    
    # ulangi hingga list sorted berjumlah sama dengan jumlah matkul yang ada
    # yang berarti tidak ada lagi pre-requisite yang diproses (matkul beserta pre-req sudah terambil semua)
    # karena jumlah pre-req terus berkurang tiap semesternya (decrease and conquer)



    
            
            
            





    
            
            
            
            
















