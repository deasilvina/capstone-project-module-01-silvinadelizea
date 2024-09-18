import getpass
from prettytable import PrettyTable
from datetime import datetime 
from colorama import Fore, Style, init
init(autoreset=True) 

daftar_mobil = [
    ["Fortuner", 2021, "Hitam", "B1234XY", "Toyota", "Matic", 7, 600000 ],
    ["Avanza", 2017, "Silver", "B5678AB", "Toyota", "Manual", 7, 400000],
    ["Innova", 2024, "Putih", "B9101CD", "Toyota", "Matic", 7, 600000],
    ["Rush", 2019, "Putih", "B2345EF", "Toyota", "Manual", 5, 500000],
    ["Ertiga", 2020, "Putih", "B6789GH", "Suzuki", "Matic", 7,400000],
    ["Xpander", 2018, "Putih", "B4567EJ", "Mitsubishi", "Matic", 7, 500000],
    ["Gran Max", 2023, "Silver", "B4788MN", "Daihatsu", "Manual", 9, 400000],
    ["Luxio", 2021, "Silver", "B6678JP", "Daihatsu", "Manual", 7, 400000],
    ["Xenia", 2016, "Putih", "B7779KV", "Daihatsu", "Manual", 7, 350000],
    ["Pajero", 2015, "Hitam", "B9083DS", "Mitsubishi", "Matic", 7, 400000]
]

pengakses = ["Athirah", "Dini", "Yusuf", "Ira", "Dea"]
password = "7899"
daftar_members = []
history_mobil = []

#1 : Fungsi untuk menampilkan menu
def show_menu():
    print(Fore.GREEN + "Menu yang bisa kamu pilih : ".center(50))
    print("1. Menampilkan daftar mobil yang tersedia ")
    print("2. Memasukkan data mobil baru")
    print("3. Mengubah data mobil yang tersedia")
    print("4. Booking mobil")
    print("5. Riwayat peminjaman mobil") 
    print("6. Pendaftaran membership") 
    print("7. Menghapus data mobil")
    print(Fore.RED + "8. EXIT")
    while True:
        try:
            print()
            pilihan = int(input(Fore.CYAN + "Masukkan opsi yang dipilih: "))
            print()
            
            if pilihan == 1:
                show_car(daftar_mobil)
                while True:
                    kembali_menu = input( "Apakah Anda ingin kembali ke menu utama (ya/tidak): ").strip().lower()
                    if kembali_menu == 'ya':
                        print()
                        print(Fore.CYAN+ " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                        show_menu()  # Kembali ke menu utama (keluar dari loop dan tampilkan menu lagi)
                    elif kembali_menu == 'tidak':
                        print(Fore.GREEN + "Terima kasih!")
                        exit()  # Keluar dari program
                    else:
                        print(Fore.RED + "Harap jawab sesuai pilihan 'ya' atau 'tidak'!")
            

            elif pilihan == 2:
                print()
                add_newcar(daftar_mobil)

            elif pilihan == 3:
                edit_mobil(daftar_mobil)

            elif pilihan == 4:
                booking_mobil(daftar_mobil)

            elif pilihan == 5:
                show_history()

            elif pilihan == 6:
                register_membership()

            elif pilihan == 7:
                delete_mobil(daftar_mobil)

            elif pilihan == 8:
                print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                exit()  # Keluar dari program
            else:
                print(Fore.RED + "Pilihan hanya tersedia dari 1-8. Silakan coba lagi!")
        
        except ValueError:
            print(Fore.RED + "Input harus berupa angka yang sesuai. Silakan coba lagi!")

#2 : Fungsi untuk login admin 
def login():
    while True: 
        print(Fore.CYAN+ " 𓆩♡𓆪 Selamat Datang di Engene's Rental 𓆩♡𓆪 ".center(50))
        print(Fore.GREEN + "=== Login ===".center(50))
        print()

        # Memasukkan nama dan password
        nama = input("Masukkan nama = ").strip().capitalize()
        masukpassword = getpass.getpass("Masukkan password = ").strip()

        # Mengecek apakah nama dan password diinput sesuai type
        if not nama.isalpha():  # alphabet letters
            print(Fore.RED + "Maaf, nama yang Anda input salah. Nama harus berupa huruf. Silakan coba lagi.")
        elif not masukpassword.isdigit():  # harus angka
            print(Fore.RED + "Maaf, password yang Anda input salah. Password harus berupa angka. Silakan coba lagi.")
        else:
            # Mengecek apakah nama dan password masuk dalam deretan admin yang boleh mengakses sistem
            if nama in pengakses and masukpassword == password:
                print(Fore.GREEN + "Login berhasil! Selamat datang, " + nama + "!")
                print()
                show_menu()  # Panggil menu setelah login berhasil
                return  # Keluar dari fungsi login setelah login berhasil
            elif nama in pengakses and masukpassword != password:
                print(Fore.RED + "Maaf, password yang Anda masukkan salah. Silakan coba lagi!")
            elif nama not in pengakses and masukpassword == password:
                print(Fore.RED + "Nama tidak ditemukan. Silahkan coba lagi!")
            else:
                print(Fore.RED + "Nama dan password tidak ditemukan. Silakan coba lagi!")

        # Tanya apakah ingin mencoba login lagi setelah gagal
        while True:
            lanjut_login = input(Fore.CYAN + "Apakah Anda ingin mencoba login lagi? (ya/tidak): ").strip().lower()
            if lanjut_login == 'ya':
                print(Fore.GREEN + "Silakan coba login lagi.")
                print()
                break  # Kembali ke awal loop untuk login lagi
            elif lanjut_login == 'tidak':
                print(Fore.CYAN + "Terima kasih telah menggunakan Engene's Rental! Sampai jumpa!")
                exit()  # Mengakhiri program
            else:
                print(Fore.RED + "Harap menjawab sesuai dengan opsi yang diberikan (ya/tidak).")



#3 : Fungsi yang menunjukkan tabel mobil yang tersedia
def show_car(daftar_mobil):
    print(Fore.BLUE + "🚙 DAFTAR MOBIL ENGENE'S RENTAL CAR 🚙".center(120))
    if not daftar_mobil:  # Cek apakah daftar mobil kosong
        print(Fore.RED + "Maaf,tidak ada mobil yang tersedia saat ini.".center(120))
        print()
        while True:
            kembali_menu = input("Apakah Anda ingin kembali ke menu utama (ya/tidak): ").strip().lower()
            if kembali_menu == 'ya':
                print(Fore.CYAN + "𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪".center(50))
                show_menu()  # Kembali ke menu utama
                return
            elif kembali_menu == 'tidak':
                print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                exit()  # Mengakhiri program
            else:
                print(Fore.RED + "Harap jawab sesuai pilihan 'ya' atau 'tidak'!")
    else:
        # Jika mobil ada, tampilkan daftar
        table = PrettyTable()  # Menggunakan PrettyTable untuk membuat tabelnya
        table.field_names = ["No.", "Model", "Tahun Produksi", "Warna", "Plat Nomor", "Merk", "Transmission", "Jumlah Penumpang", "Harga Sewa Harian"]

        # Isi dalam tabel
        for i, item in enumerate(daftar_mobil, start=1):
            table.add_row([i, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])
        print(table)


#4 : Fungsi untuk menambahkan mobil baru ke tabel
def add_newcar(daftar_mobil):
    while True:
        print(Fore.CYAN + " DATA MOBIL BARU ".center(100))
        print()
        print("Harap masukkan data mobil dengan lengkap:")

        # input nama mobil
        while True:
            nama_mobil = input("- Masukkan model mobil : ").strip().title()
            if len(nama_mobil) == 0:
                print(Fore.RED + "Model mobil tidak boleh kosong. Silakan masukkan model mobil.")
            elif nama_mobil.replace(" ", "").isalnum():
                break
            else:
                print(Fore.RED + "Model mobil harus berupa huruf dan/atau angka. Silakan coba lagi!")
            print()

        # input tahun produksi
        while True:
            tahun_produksi = input("- Masukkan tahun produksi : ").strip()
            if len(tahun_produksi) == 0:
                print(Fore.RED + "Tahun produksi tidak boleh kosong. Silakan masukkan tahun produksi.")
            else:
                try:
                    tahun_produksi = int(tahun_produksi)
                    if tahun_produksi > 0:       # Memastikan tahun produksi lebih dari 0
                        break
                    else:
                        print(Fore.RED + "Tahun produksi harus lebih dari 0. Silakan coba lagi!")
                except ValueError:
                    print(Fore.RED + "Tahun produksi harus berupa angka. Silakan coba lagi!")
            print()

        # input warna
        while True:
            warna = input("- Warna : ").strip().title()
            if len(warna) == 0:
                print(Fore.RED + "Warna tidak boleh kosong. Silakan masukkan warna mobil.")
            elif warna.replace(" ", "").isalpha():
                break
            else:
                print(Fore.RED + "Warna harus berupa huruf. Silakan coba lagi!")
            print()

        # input plat nomor
        while True:
            plat_nomor = input("- Plat nomor : ").strip().upper()

            # cek duplikasi
            duplicate_found = False
            for mobil in daftar_mobil:
                if plat_nomor == mobil[3]:  # membandingkan plat nomor yang diinput dengan plat nomor yang ada di table
                    print(Fore.RED + "Plat nomor sudah ada. Silakan masukkan plat nomor yang berbeda!")
                    duplicate_found = True
                    break

            if duplicate_found == False :
                if len(plat_nomor) == 0:
                    print(Fore.RED + "Plat nomor tidak boleh kosong. Silakan masukkan plat nomor.")
                elif plat_nomor.isalnum():
                    break
                else:
                    print(Fore.RED + "Plat nomor harus berupa huruf dan angka. Silakan coba lagi!")
            print()

        # input merk
        while True:
            merk = input("- Merk : ").strip().title()
            if len(merk) == 0:
                print(Fore.RED + "Merk tidak boleh kosong. Silakan masukkan merk mobil.")
            elif merk.replace(" ", "").isalpha():
                break
            else:
                print(Fore.RED + "Merk harus berupa huruf. Silakan coba lagi!")
            print()

        # input transmisi
        while True:
            transmission = input("- Transmission (manual/matic): ").strip().capitalize()
            if len(transmission) == 0:
                print(Fore.RED + "Transmisi tidak boleh kosong. Silakan pilih 'Manual' atau 'Matic'.")
            elif transmission == 'Matic' or transmission == 'Manual':
                break
            else:
                print(Fore.RED + "Transmisi harus berupa 'Matic' atau 'Manual'. Silakan coba lagi!")
            print()

        # input jumlah penumpang
        while True:
            jumlah_penumpang = input("- Jumlah penumpang : ").strip()
            if len(jumlah_penumpang) == 0:
                print(Fore.RED + "Jumlah penumpang tidak boleh kosong. Silakan masukkan jumlah penumpang!")
            else:
                try:
                    jumlah_penumpang = int(jumlah_penumpang)
                    if jumlah_penumpang > 0:  # Memastikan jumlah penumpang lebih dari 0
                        break
                    else:
                        print(Fore.RED + "Jumlah penumpang harus lebih dari 0. Silakan coba lagi!")
                except ValueError:
                    print(Fore.RED + "Jumlah penumpang harus berupa angka yang valid. Silakan coba lagi!")
            print()

        # input harga sewa harian
        while True:
            harga_harian = input("- Harga sewa harian : ").strip()
            if len(harga_harian) == 0:
                print(Fore.RED + "Harga sewa harian tidak boleh kosong. Silakan masukkan harga sewa!")
            else:
                try:
                    harga_harian = int(harga_harian)
                    break
                except ValueError:
                    print(Fore.RED + "Harga sewa harian harus berupa angka. Silakan coba lagi!")
            print()

        # menambahkan inputan ke daftar 
        daftar_mobil.append([nama_mobil, tahun_produksi, warna, plat_nomor, merk, transmission, jumlah_penumpang, harga_harian])

        print(Fore.GREEN + "Mobil " + (nama_mobil) + " berhasil ditambahkan!")
        print()
        show_car(daftar_mobil)

        # Menanyakan apakah ingin menambahkan mobil lagi
        while True:
            lanjut_tambah = input(Fore.CYAN + "Apakah Anda ingin menambahkan mobil lain? (ya/tidak): ").strip().lower()
            if lanjut_tambah == 'ya':
                print()
                break  # Kembali ke awal untuk menambah mobil lagi
            elif lanjut_tambah == 'tidak':
                # Menanyakan apakah ingin kembali ke menu utama
                kembali_menu = input(Fore.CYAN + "Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                if kembali_menu == 'ya':
                    print()
                    print(Fore.CYAN + "𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪".center(50))
                    show_menu()  # Kembali ke menu utama
                    return  # Keluar dari fungsi
                elif kembali_menu == 'tidak':
                    print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                    exit()  # Mengakhiri program
                else:
                    print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak).")
            else:
                print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak).")


#6 : Fungsi untuk mengedit mobil
def edit_mobil(daftar_mobil):
    while True:
        # Menampilkan tabel mobil
        print()
        show_car(daftar_mobil)

        # Meminta input mobil dan plat nomor
        cari_mobil = input("Masukkan model mobil yang ingin diedit: ").strip().lower()
        cari_plat = input("Plat nomor: ").strip().upper()

        mobil_ditemukan = None
        nama_ada = False
        plat_ada = False

        # Loop untuk mencari mobil yang cocok
        for mobil in daftar_mobil:
            if mobil[0].lower() == cari_mobil:
                nama_ada = True  # Nama mobil ditemukan
            if mobil[3].upper() == cari_plat:
                plat_ada = True  # Plat nomor ditemukan
            if mobil[0].lower() == cari_mobil and mobil[3].upper() == cari_plat:
                mobil_ditemukan = mobil
                print(Fore.GREEN + "Mobil ditemukan: " + str(mobil_ditemukan))
                break  # Keluar dari loop jika mobil ditemukan

        # Proses pengeditan
        if mobil_ditemukan:
            while True:
                print("\nPilih bagian data mobil yang ingin diubah: ")
                print("1. Model mobil")
                print("2. Tahun produksi")
                print("3. Warna")
                print("4. Plat nomor")
                print("5. Merk")
                print("6. Transmission")
                print("7. Jumlah penumpang")
                print("8. Harga sewa harian")
                print("9. Kembali ke menu utama")

                jawaban = input("Masukkan nomor pilihan (pisahkan dengan koma jika lebih dari satu): ").split(',')

                # Validasi input
                valid = True
                for i in jawaban:
                    i = i.strip()  # Hapus spasi dari input
                    if not i.isdigit():  # Harus angka
                        print(Fore.RED + "Harap masukkan opsi dalam bentuk angka dan tidak boleh kosong!")
                        valid = False
                        break
                    if int(i) < 1 or int(i) > 9:  # Kondisi harus sesuai angka
                        print(Fore.RED + "Harap memilih sesuai opsi yang tersedia (1-9)!")
                        valid = False
                        break

                if not valid:
                    continue  # Ulangi input jika ada yang tidak valid

                # Jika input valid, lanjutkan proses pengeditan
                for i in jawaban:
                    i = int(i.strip())
                    if i == 1:
                        while True:
                            nama_mobil_baru = input("Masukkan model mobil baru: ").title().strip()
                            if len(nama_mobil_baru) == 0:
                                print(Fore.RED + "Model mobil tidak boleh kosong. Silakan coba lagi!")
                            elif nama_mobil_baru.replace(" ", "").isalnum():
                                mobil_ditemukan[0] = nama_mobil_baru
                                break
                            else:
                                print(Fore.RED + "Model mobil harus berupa huruf. Silakan coba lagi!")

                    elif i == 2:
                        while True:
                            try:
                                tahun_produksi_baru = input("Masukkan tahun produksi mobil baru: ").strip()
                                if len(tahun_produksi_baru) == 0:
                                    print(Fore.RED + "Tahun produksi tidak boleh kosong. Silakan coba lagi!")
                                else:
                                    tahun_produksi_baru = int(tahun_produksi_baru)
                                    mobil_ditemukan[1] = tahun_produksi_baru
                                    break
                            except ValueError:
                                print(Fore.RED + "Tahun produksi harus berupa angka. Silakan coba lagi!")

                    elif i == 3:
                        while True:
                            warna_baru = input("Masukkan warna mobil baru: ").title().strip()
                            if len(warna_baru) == 0:
                                print(Fore.RED + "Warna tidak boleh kosong. Silakan coba lagi!")
                            elif warna_baru.isalpha():
                                mobil_ditemukan[2] = warna_baru
                                break
                            else:
                                print(Fore.RED + "Warna harus berupa huruf. Silakan coba lagi!")

                    elif i == 4:
                        while True:
                            plat_nomor_baru = input("Masukkan plat nomor mobil baru: ").upper().strip()
                            if len(plat_nomor_baru) == 0:
                                print(Fore.RED + "Plat nomor tidak boleh kosong. Silakan coba lagi!")
                            elif plat_nomor_baru.isalnum():
                                mobil_ditemukan[3] = plat_nomor_baru
                                break
                            else:
                                print(Fore.RED + "Plat nomor harus berupa huruf dan angka. Silakan coba lagi!")

                    elif i == 5:
                        while True:
                            merk_baru = input("Masukkan merk mobil baru: ").title().strip()
                            if len(merk_baru) == 0:
                                print(Fore.RED + "Merk tidak boleh kosong. Silakan coba lagi!")
                            elif merk_baru.replace(" ", "").isalpha():
                                mobil_ditemukan[4] = merk_baru
                                break
                            else:
                                print(Fore.RED + "Merk harus berupa huruf. Silakan coba lagi!")

                    elif i == 6:
                        while True:
                            transmission_mobil_baru = input("Masukkan transmission baru (matic/manual): ").title().strip()
                            if len(transmission_mobil_baru) == 0:
                                print(Fore.RED + "Transmisi tidak boleh kosong. Silakan coba lagi!")
                            elif transmission_mobil_baru in ['Matic', 'Manual']:
                                mobil_ditemukan[5] = transmission_mobil_baru
                                break
                            else:
                                print(Fore.RED + "Transmisi harus berupa 'Matic' atau 'Manual'. Silakan coba lagi!")

                    elif i == 7:
                        while True:
                            try:
                                jumlah_penumpang_mobil_baru = input("Masukkan jumlah penumpang baru: ").strip()
                                if len(jumlah_penumpang_mobil_baru) == 0:
                                    print(Fore.RED + "Jumlah penumpang tidak boleh kosong. Silakan coba lagi!")
                                else:
                                    jumlah_penumpang_mobil_baru = int(jumlah_penumpang_mobil_baru)
                                    if jumlah_penumpang_mobil_baru > 0:
                                        mobil_ditemukan[6] = jumlah_penumpang_mobil_baru
                                        break
                                    else:
                                        print(Fore.RED + "Jumlah penumpang harus lebih dari 0. Silakan coba lagi!")
                            except ValueError:
                                print(Fore.RED + "Jumlah penumpang harus berupa angka yang valid. Silakan coba lagi!")

                    elif i == 8:
                        while True:
                            try:
                                harga_harian_baru = input("Masukkan harga sewa harian baru: ").strip()
                                if len(harga_harian_baru) == 0:
                                    print(Fore.RED + "Harga sewa harian tidak boleh kosong. Silakan coba lagi!")
                                else:
                                    harga_harian_baru = int(harga_harian_baru)
                                    mobil_ditemukan[7] = harga_harian_baru
                                    break
                            except ValueError:
                                print(Fore.RED + "Harga sewa harian harus berupa angka. Silakan coba lagi!")

                    elif i == 9:
                        print()
                        print(Fore.CYAN+ " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                        show_menu()
                        return

                # Menampilkan tabel mobil setelah diedit
                print()
                show_car(daftar_mobil)

                # Pertanyaan apakah ingin mengedit mobil lain atau kembali ke menu utama
                while True:
                    lanjut_bagian = input("Apakah Anda ingin mengubah data bagian lain? (ya/tidak): ").strip().lower()
                    if lanjut_bagian == 'ya':
                        break  # Kembali ke awal untuk memilih bagian lain
                    elif lanjut_bagian == 'tidak':
                        break  # Keluar dari loop
                    else:
                        print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")

                if lanjut_bagian == 'tidak':
                    # Menanyakan apakah ingin mengedit mobil lain
                    while True:
                        lanjut_cari = input("Apakah Anda ingin mencoba mengubah data mobil lain? (ya/tidak): ").strip().lower()
                        if lanjut_cari == 'ya':
                            return edit_mobil(daftar_mobil)  # Kembali ke awal untuk memasukkan mobil dan plat nomor lagi
                        elif lanjut_cari == 'tidak':
                            while True:
                                kembali_menu = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                                if kembali_menu == 'ya':
                                    print()
                                    print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                                    show_menu()
                                    return
                                elif kembali_menu == 'tidak':
                                    print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                                    exit()
                                else:
                                    print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")
                        else:
                            print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")

        else:
            # Jika mobil tidak ditemukan, tampilkan pesan sesuai kondisi
            if nama_ada and not plat_ada:
                print(Fore.RED + "Mobil " + cari_mobil.title() + " ditemukan, tetapi plat nomor " + cari_plat + " tidak tersedia.")
            elif not nama_ada and plat_ada:
                print(Fore.RED + "Plat nomor " + cari_plat + " ditemukan, tetapi mobil " + cari_mobil.title() + " tidak tersedia.")
            else:
                print(Fore.RED + "Mobil dengan jenis " + cari_mobil.title() + " dan plat nomor " + cari_plat + " tidak ditemukan.")

            # Setelah pesan ditampilkan, tanyakan apakah ingin mengedit lagi atau kembali ke menu utama
            while True:
                lanjut_edit = input(Fore.CYAN + "Apakah Anda masih ingin mencoba untuk mengubah data mobil yang tersedia ? (ya/tidak): ").strip().lower()
                if lanjut_edit == 'ya':
                    break  # Kembali ke awal untuk mencoba mengedit mobil lain
                elif lanjut_edit == 'tidak':
                    kembali_menu = input(Fore.CYAN + "Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                    if kembali_menu == 'ya':
                        print()
                        print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                        show_menu()
                        return
                    elif kembali_menu == 'tidak':
                        print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                        exit()
                    else:
                        print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")
                else:
                    print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")



#7 : Fungsi untuk mendaftarkan membership
def register_membership():
    while True:   
        print((Fore.GREEN + "FORMULIR PENDAFTARAN MEMBERSHIP ENGENE'S RENTAL CAR").center(30))
        print("Harap mengisi data diri sebagai berikut: ")

        # Input nama member (boleh berisi spasi dan tidak boleh kosong)
        while True:
            nama_member = input("1. Nama : ").strip().title()
            if len(nama_member) == 0:
                print(Fore.RED + "Nama tidak boleh kosong. Silakan masukkan nama yang valid.")
            elif nama_member.replace(" ", "").isalpha():
                break
            else:
                print(Fore.RED + "Nama harus hanya berisi huruf. Silakan coba lagi!")

        # Validasi NIK harus berupa angka
        while True:
            try:
                nomor_ktp_member = int(input("2. NIK : "))
                break
            except ValueError:
                print(Fore.RED + "NIK harus berupa angka. Silakan coba lagi.")
        
        # Validasi alamat (boleh berisi spasi dan tidak boleh kosong)
        while True:
            alamat_member = input("3. Alamat : ").strip()
            if len(alamat_member) == 0:
                print(Fore.RED + "Alamat tidak boleh kosong. Silakan masukkan alamat yang valid.")
            else:
                break

        # Validasi tempat lahir (boleh berisi spasi dan tidak boleh kosong)
        while True:
            tempatlahir_member = input("4. Tempat lahir : ").strip().title()
            if len(tempatlahir_member) == 0:
                print(Fore.RED + "Tempat lahir tidak boleh kosong. Silakan masukkan tempat lahir yang valid.")
            elif tempatlahir_member.replace(" ", "").isalpha():
                break
            else:
                print(Fore.RED + "Tempat lahir harus hanya berisi huruf. Silakan coba lagi.")
        
        # Validasi tanggal lahir dengan format dd-mm-yyyy
        while True:
            tanggal_lahir_member = input("5. Tanggal lahir (dd-mm-yyyy): ").strip()
            try:
                datetime.strptime(tanggal_lahir_member, "%d-%m-%Y")
                break  # Berhenti jika format benar
            except ValueError:
                print(Fore.RED + "Tanggal lahir harus sesuai format dd-mm-yyyy. Silakan coba lagi.")

        # Validasi nomor telepon harus berupa angka
        while True:
            try:
                nomor_telepon_member = int(input("6. Nomor telepon : "))
                break
            except ValueError:
                print(Fore.RED + "Nomor telepon harus berupa angka. Silakan coba lagi.")
        
        # Validasi email tidak boleh kosong dan harus valid
        while True:
            email_member = input("7. Email : ").strip()
            if len(email_member) == 0:
                print(Fore.RED + "Email tidak boleh kosong. Silakan masukkan email yang valid.")
            elif "@" in email_member and "." in email_member:
                break
            else:
                print(Fore.RED + "Email harus valid dan sesuai format. Silakan coba lagi.")

        # Simpan data member ke dictionary
        member_data = {
            "nama": nama_member,
            "NIK": nomor_ktp_member,
            "alamat": alamat_member,
            "tempat_lahir": tempatlahir_member,
            "tanggal_lahir": tanggal_lahir_member,
            "nomor_telepon": nomor_telepon_member,
            "email": email_member
        }

        # Menampilkan ringkasan data member
        print("\nFORMULIR PENDAFTARAN MEMBERSHIP ENGENE'S RENTAL CAR")
        print("Nama: " + member_data["nama"])
        print("NIK: " + str(member_data["NIK"]))
        print("Tempat Lahir: " + member_data["tempat_lahir"])
        print("Tanggal Lahir: " + member_data["tanggal_lahir"])
        print("Alamat: " + member_data["alamat"])
        print("Nomor Telepon: " + str(member_data["nomor_telepon"]))
        print("Email: " + member_data["email"])
        print()
        
        print(Fore.GREEN + "\nPendaftaran membership berhasil!")

        # Tambahkan data member ke daftar membership
        daftar_members.append(member_data)
        print(Fore.YELLOW + "Selamat, " + nama_member + "! Kamu telah terdaftar sebagai member.")
        print()

        # Menanyakan apakah ingin mendaftarkan member lain
        while True:
            tambah_lagi = input("Apakah Anda ingin mengisi data lagi untuk pendaftaran membership? (ya/tidak): ").strip().lower()
            if tambah_lagi == 'ya':
                break  # Kembali ke awal untuk menambah member baru
            elif tambah_lagi == 'tidak':
                # Menanyakan apakah ingin kembali ke menu utama
                while True:
                    kembali_menu = input("Apakah Anda ingin kembali ke menu utama (ya/tidak): ").strip().lower()
                    if kembali_menu == 'ya':
                        print()
                        print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                        show_menu()  # Kembali ke menu utama
                        return  # Keluar dari fungsi
                    elif kembali_menu == 'tidak':
                        print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                        exit()  # Keluar dari program
                    else:
                        print(Fore.RED + "Harap jawab sesuai pilihan 'ya' atau 'tidak'.")
            else:
                print(Fore.RED + "Harap jawab sesuai pilihan 'ya' atau 'tidak'.")

        


#8 : Fungsi untuk booking mobil
def booking_mobil(daftar_mobil):
    while True:  # Loop keseluruhan proses booking
        print()
        print((Fore.CYAN + "FORMULIR SEWA MOBIL").center(50))
        print()
        print(Fore.GREEN + "Data Penyewa")

        # 1. Input nama pelanggan (boleh berisi spasi dan tidak boleh kosong)
        while True:
            nama_pelanggan = input("1. Nama : ").strip().title()
            if len(nama_pelanggan) == 0:
                print(Fore.RED + "Nama tidak boleh kosong. Silakan masukkan nama yang valid.")
            elif nama_pelanggan.replace(" ", "").isalpha():
                break
            else:
                print(Fore.RED + "Nama harus hanya berisi huruf. Silakan coba lagi!")

        # 2. Validasi NIK harus berupa angka
        while True:
            try:
                nomor_ktp = int(input("2. NIK : "))
                break
            except ValueError:
                print(Fore.RED + "NIK harus berupa angka. Silakan coba lagi.")
        
        # 3. Validasi alamat (boleh berisi spasi dan tidak boleh kosong)
        while True:
            alamat_penyewa = input("3. Alamat : ").strip()
            if len(alamat_penyewa) == 0:
                print(Fore.RED + "Alamat tidak boleh kosong. Silakan masukkan alamat yang valid.")
            else:
                break

        # 4. Validasi nomor telepon harus berupa angka
        while True:
            try:
                nomor_telepon = int(input("4. Nomor telepon : "))
                break
            except ValueError:
                print(Fore.RED + "Nomor telepon harus berupa angka. Silakan coba lagi.")
        
        # 5. Validasi email tidak boleh kosong dan harus valid
        while True:
            email_penyewa = input("5. Email : ").strip()
            if len(email_penyewa) == 0:
                print(Fore.RED + "Email tidak boleh kosong. Silakan masukkan email yang valid.")
            elif "@" in email_penyewa and "." in email_penyewa:
                break
            else:
                print(Fore.RED + "Email harus valid dan sesuai format. Silakan coba lagi.")
       
        # Periksa apakah pelanggan adalah member
        is_member = False
        for member in daftar_members:
            if (member['nama'] == nama_pelanggan and 
                member['NIK'] == nomor_ktp and
                member['alamat'] == alamat_penyewa and
                member['nomor_telepon'] == nomor_telepon and
                member['email'] == email_penyewa):
                is_member = True
                break

        print()
        show_car(daftar_mobil)

        # Data kedua: Mobil yang disewa
        
        while True:
            print()
            print(Fore.GREEN + "Data mobil yang disewa")
            data_mobil = input("1. Mobil: ").strip().title()
            plat_nomor = input("2. Plat Nomor: ").strip().upper()
            
            mobil_ditemukan = None
            for mobil in daftar_mobil:
                if mobil[0] == data_mobil and mobil[3] == plat_nomor:
                    mobil_ditemukan = mobil
                    break

            if mobil_ditemukan:
                break
            else:
                print(Fore.RED + "Mobil " + data_mobil + " dengan plat nomor " + plat_nomor + " tidak ditemukan.")
                
                # Menanyakan apakah ingin melanjutkan mencari mobil
                while True:
                    lanjut_cari = input(Fore.CYAN + "Apakah Anda ingin tetap melanjutkan pencarian mobil untuk disewa? (ya/tidak): ").strip().lower()
                    if lanjut_cari == 'ya':
                        break  # Kembali ke pengisian data mobil
                    elif lanjut_cari == 'tidak':
                        # Menanyakan apakah ingin kembali ke menu utama
                        kembali_menu = input(Fore.CYAN + "Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                        print()
                        if kembali_menu == 'ya':
                            print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                            show_menu()
                            return
                        elif kembali_menu == 'tidak':
                            print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                            exit()
                        else:
                            print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")
                    else:
                        print(Fore.RED + "Harap jawab sesuai dengan opsi yang diberikan (ya/tidak)!")

        # Validasi transmission
        while True:
            data_transmission = input("3. Transmission: ").strip().capitalize()
            if data_transmission == mobil_ditemukan[5]:
                break
            else:
                print(Fore.RED + "Transmission yang tersedia untuk mobil ini adalah " + mobil_ditemukan[5] + ". Silakan coba lagi!")

        # Validasi jumlah penumpang
        while True:
            try:
                data_jumlahpenumpang = int(input("4. Jumlah Penumpang: "))
                if data_jumlahpenumpang <= mobil_ditemukan[6] and data_jumlahpenumpang > 0:
                    break
                elif data_jumlahpenumpang == 0:
                    print(Fore.RED + "Jumlah penumpang tidak boleh 0. Silakan masukkan jumlah yang valid!")
                else:
                    print(Fore.RED + "Mobil ini hanya bisa menampung kurang atau sama dengan " + str(mobil_ditemukan[6]) + " orang penumpang.")
            except ValueError:
                print(Fore.RED + "Jumlah penumpang harus berupa angka dan tidak boleh kosong. Silakan coba lagi!")

        # Input tanggal mulai dan selesai
        while True:
            try:
                data_mulai = input("6. Tanggal mulai (dd-mm-yyyy): ").strip()
                data_akhir = input("7. Tanggal selesai (dd-mm-yyyy): ").strip()

                # Mengonversi string tanggal menjadi objek datetime
                tanggal_mulai = datetime.strptime(data_mulai, "%d-%m-%Y")
                tanggal_selesai = datetime.strptime(data_akhir, "%d-%m-%Y")

                # Menghitung selisih hari
                selisih_hari = (tanggal_selesai - tanggal_mulai).days + 1  # Tambah 1 hari untuk menghitung hari pertama juga

                if selisih_hari <= 0:
                    print(Fore.RED + "Tanggal selesai harus lebih besar dari tanggal mulai. Silakan coba lagi!")
                else:
                    break
            except ValueError:
                print(Fore.RED + "Masukkan tanggal dengan format yang benar (dd-mm-yyyy).")


        # Menghitung total harga sewa berdasarkan selisih hari
        harga_perhari = mobil_ditemukan[7]
        total_harga_sewa = harga_perhari * selisih_hari

        # Berikan diskon 30% jika pelanggan adalah member
        print()
        print(Fore.GREEN + "Total pembayaran: ")
        if is_member == True :
            diskon = total_harga_sewa * 0.30
            total_harga_sewa -= diskon
            print("Selamat, Anda mendapatkan diskon 30%!")
            print("Biaya yang harus Anda bayar setelah diskon adalah: Rp" + str(int(total_harga_sewa)))
        else:
            print(Fore.GREEN + "Total biaya yang harus Anda bayar adalah: Rp" + str(int(total_harga_sewa)))

        # Proses pembayaran
        while True:
            try:
                jumlah_bayar = int(input("Masukkan jumlah pembayaran: Rp"))
                if jumlah_bayar >= total_harga_sewa:
                    kembalian = int(jumlah_bayar - total_harga_sewa)
                    print(Fore.GREEN + "Pembayaran berhasil!")
                    print("Kembalian Anda: Rp" + str(kembalian))
                    break
                else:
                    print(Fore.RED + "Uang Anda kurang sebesar Rp" + str(total_harga_sewa - jumlah_bayar) + ". Silakan bayar kembali.")
            except ValueError:
                print(Fore.RED + "Masukkan jumlah pembayaran yang valid!")

        # Menambahkan data transaksi ke dalam history_mobil
        history_mobil.append({
            "nama_pelanggan": nama_pelanggan,
            "nomor_ktp": nomor_ktp,
            "alamat_penyewa": alamat_penyewa,
            "nomor_telepon": nomor_telepon,
            "email_penyewa": email_penyewa,
            "mobil": mobil_ditemukan[0],
            "plat_nomor": mobil_ditemukan[3],
            "transmission": mobil_ditemukan[5],
            "jumlah_penumpang": mobil_ditemukan[6],
            "tanggal_mulai": data_mulai,
            "tanggal_selesai": data_akhir
        })

        # Menghapus mobil yang sudah disewa dari daftar_mobil
        daftar_mobil.remove(mobil_ditemukan)
        
        # Pertanyaan kembali ke menu atau lanjut
        while True:
            print()
            pilihan = input("Apakah Anda ingin melakukan transaksi lagi dan menyewa mobil lain? (ya/tidak) :  ").strip().lower()
            if pilihan == "ya":
                break  # Kembali ke pengulangan awal untuk mengisi data diri dan booking lagi
            elif pilihan == "tidak":
                # Menanyakan apakah ingin kembali ke menu utama
                kembali_menu = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                if kembali_menu == "ya":
                    print()
                    print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                    show_menu()  # Kembali ke menu utama
                    return  # Keluar dari fungsi booking
                elif kembali_menu == "tidak":
                    print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                    exit()  # Mengakhiri program
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan ketik 'ya' atau 'tidak'.")
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan ketik 'ya' atau 'tidak'.")



#9 : Fungsi untuk menunjukkan riwayat penyewaan 
def show_history():
    print((Fore.CYAN + "RIWAYAT PENYEWAAN MOBIL").center(100))  # Pastikan untuk memanggil center pada string
    print()
    if not history_mobil:
        print((Fore.RED + "Belum ada riwayat penyewaan mobil.").center(100))
        while True:
            print()
            kembali_menu = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
            if kembali_menu == 'ya':
                print()
                print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                show_menu()  # Kembali ke menu utama
                return
            elif kembali_menu == 'tidak':
                print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                exit()  # Mengakhiri program
            else:
                print(Fore.RED + "Input tidak valid. Silakan ketik 'ya' atau 'tidak'!")
    else:
        # Format string sebelum print, menggunakan center untuk menempatkannya di tengah
        table = PrettyTable()
        table.field_names = [
            "No.", "Nama Penyewa", "NIK", "Alamat", "Nomor Telepon", "Email", 
            "Model Mobil", "Plat Nomor", "Transmission", "Jumlah Penumpang", 
            "Tanggal Mulai", "Tanggal Selesai"
        ]

        # Menambahkan data riwayat penyewaan ke dalam tabel
        for i, riwayat in enumerate(history_mobil, start=1):
            table.add_row([
                i, riwayat["nama_pelanggan"], riwayat["nomor_ktp"], riwayat["alamat_penyewa"],
                riwayat["nomor_telepon"], riwayat["email_penyewa"], riwayat["mobil"],
                riwayat["plat_nomor"], riwayat["transmission"], riwayat["jumlah_penumpang"],
                riwayat["tanggal_mulai"], riwayat["tanggal_selesai"]
            ])
        
        print(table)

        # Menanyakan apakah ingin kembali ke menu utama atau mengakhiri program
        while True:
            kembali_menu = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
            if kembali_menu == 'ya':
                print()
                print(Fore.CYAN + " 𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪 ".center(50))
                show_menu()  # Kembali ke menu utama
                return
            elif kembali_menu == 'tidak':
                print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                exit()  # Mengakhiri program
            else:
                print(Fore.RED + "Input tidak valid. Silakan ketik 'ya' atau 'tidak'!")


#10 : Fungsi untuk delete mobil
def delete_mobil(daftar_mobil):
    while True:
        show_car(daftar_mobil)  # Menampilkan daftar mobil yang tersedia
        
        # Input mobil yang akan dihapus
        cari_mobil = input("Masukkan model mobil yang ingin dihapus: ").strip().title()
        cari_plat = input("Masukkan plat nomor mobil yang ingin dihapus: ").strip().upper()
        
        # Mencari mobil sesuai input
        mobil_ditemukan = None
        for mobil in daftar_mobil:
            if mobil[0] == cari_mobil and mobil[3] == cari_plat:
                mobil_ditemukan = mobil
                break

        if mobil_ditemukan:
            while True:
                # Konfirmasi penghapusan
                konfirmasi = input("Apakah Anda yakin ingin menghapus mobil " + mobil_ditemukan[0] + " dengan plat nomor " + mobil_ditemukan[3] + "? (ya/tidak): ").strip().lower()
                
                if konfirmasi == 'ya':
                    daftar_mobil.remove(mobil_ditemukan)
                    print(Fore.GREEN + "Mobil " + mobil_ditemukan[0] + " dengan plat nomor " + mobil_ditemukan[3] + " berhasil dihapus.")
                    
                    # Menampilkan tabel mobil setelah penghapusan
                    print()
                    show_car(daftar_mobil)  # Menampilkan daftar mobil yang tersisa
                    break
                elif konfirmasi == 'tidak':
                    print(Fore.RED + "Penghapusan dibatalkan.")
                    break
                else:
                    print(Fore.RED + "Mohon jawab sesuai dengan opsi yang diberikan (ya/tidak).")
            
            # Pertanyaan setelah penghapusan atau pembatalan
            while True:
                lanjut_hapus = input("Apakah Anda ingin menghapus mobil lain? (ya/tidak): ").strip().lower()
                if lanjut_hapus == 'ya':
                    break  # Kembali ke awal untuk menghapus mobil lain
                elif lanjut_hapus == 'tidak':
                    jawaban_kembali_kemenuutama = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                    if jawaban_kembali_kemenuutama == 'ya':
                        print(Fore.CYAN + "𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪".center(50))
                        show_menu()
                        return  # Kembali ke menu utama dan keluar dari fungsi
                    elif jawaban_kembali_kemenuutama == 'tidak':
                        print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                        exit()  # Mengakhiri program tanpa input tambahan
                    else:
                        print(Fore.RED + "Harap jawab sesuai pilihan yang tersedia, yaitu 'ya' atau 'tidak'.")
                else:
                    print(Fore.RED + "Harap jawab sesuai dengan opsi yang tersedia, yaitu 'ya' atau 'tidak'.")

        else:
            print(Fore.RED + "Mobil " + cari_mobil + " dengan plat nomor " + cari_plat + " tidak ditemukan.")
            while True:
                lanjut_hapus = input("Apakah Anda ingin mencoba menghapus mobil lain? (ya/tidak): ").strip().lower()
                if lanjut_hapus == 'ya':
                    break  # Kembali ke awal untuk menghapus mobil lain
                elif lanjut_hapus == 'tidak':
                    jawaban_kembali_kemenuutama = input("Apakah Anda ingin kembali ke menu utama? (ya/tidak): ").strip().lower()
                    print()
                    if jawaban_kembali_kemenuutama == 'ya':
                        print(Fore.CYAN + "𓆩♡𓆪 Selamat Datang di Engene's Rental Car 𓆩♡𓆪".center(50))
                        show_menu()
                        return  # Kembali ke menu utama dan keluar dari fungsi
                    elif jawaban_kembali_kemenuutama == 'tidak':
                        print(Fore.GREEN + "Terima kasih telah berkunjung ke Engene's Rental Car!")
                        exit()  # Mengakhiri program tanpa input tambahan
                    else:
                        print(Fore.RED + "Harap jawab sesuai pilihan yang tersedia, yaitu 'ya' atau 'tidak'.")
                else:
                    print(Fore.RED + "Harap jawab sesuai dengan opsi yang tersedia, yaitu 'ya' atau 'tidak'.")

login()
show_menu()


