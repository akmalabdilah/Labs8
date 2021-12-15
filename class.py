import os
import sys

class Mahasiswa:
 nim=''
 nama=''
 tugas=''
 uts=''
 uas=''

dataSiswa = []
pili = 0

def menu():
     os.system('cls')
     print("Menu Aplikasi Data Siswa LinkedList python")
     print("-------------------------------------------")
     print("1. Input Data Siswa")
     print("2. Tampilkan Data Siswa")
     print("3. Update Data Siswa")
     print("4. Hapus Data Siswa")
     print("5. Author")
     print("6. Keluar Aplikasi")
     pilih = int(input("Masukkan pilihan anda : "))
     if pilih == 1 :
          pilih1()
          menu()
     elif pilih == 2:
          tampil()
          input("kembali menu utama")
          menu()
     elif pilih == 3:
          index_update=-1
          tampil()
          id_edit = int(input("Input Nim yang akan di update "))
          for a in range(0, len(dataSiswa)):
               if id_edit == dataSiswa[a].nim:
                    index_update = a
                    break
          if(index_update > -1):
               print("INPUT DATA YANG DI UPATE ")
               siswa = Mahasiswa()
               siswa.nim = (int(input("masukkan nim : ")))
               siswa.nama = (input("masukkan nama siswa : "))
               siswa.tugas = (input("masukan nilai tugas : "))
               siswa.uts = (input("masukan nilai uts : "))
               siswa.uas = (input("masukan nilai uas : "))
               dataSiswa[index_update] = siswa
               print("berhasil update data siswa")
          else : print("nim tidak ditemukan")
          input("kembali menu utama")
          menu()
     elif pilih == 4:
                os.system('cls')
                tampil()
                id_hapus = int(input("Input Nim yang akan di hapus : "))
                for data in dataSiswa:
                    if data.nim == id_hapus:
                         dataSiswa.remove(data)
                    else :
                         print("data tidak di temukan")
                print("DATA MAHASISWA ")
                for data in dataSiswa:
                    print("Nim : "+str(data.nim));
                    print("Nama  : "+data.nama)
                input("kembali menu utama")
                menu()
     elif pilih == 5 :
          author()
          
          menu()
     elif pilih == 6 :
          sys.exit()

def tampil():
	os.system('cls');
	print("DATA MAHASISWA")
	for data in dataSiswa:
		print("Nim : "+str(data.nim)) 
		print("Nama : "+data.nama)
		print("Nilai Tugas : "+data.tugas)
		print("Nilai Uts : "+data.uts)
		print("Nilai Uas : "+data.uas)
		
		print("----------------------")
		
def author():
	os.system('cls')
	print("M. AKMAL AL ABDILAH | 312110034")
	print("UPB 2021")

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		siswaBaru = Mahasiswa() 
		print("INPUT DATA MAHASISWA ") 
		siswaBaru.nim = (int(input("masukkan nim : "))) 
		siswaBaru.nama = (input("masukkan nama siswa : "))
		siswaBaru.tugas = (input("masukan nilai tugas : "))
		siswaBaru.uts = (input("masukan nilai uts : "))
		siswaBaru.uas = (input("masukan nilai uas : "))
		dataSiswa.append(siswaBaru) 
		ulang = input("Apakah Anda Ingin Mengulang (Y/ T)? ")		

menu()



    
