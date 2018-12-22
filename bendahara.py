## bendahara.py
# -*- coding: utf-8 -*-
##

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Bendahara project               $
$ Coded by Sukmaind               $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Sabtu 22 Desember 2018 10.33 AM $
$ github.com/asterix88            $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""


from time import sleep
import sys
import os


def inti():
	os.system("clear")
	print("\033[1;33mData Keuangan Acara Muda-i\033[0m")
	print()
	with open("uang_gp.txt") as file:
		for line in file:
			line = int(line)
			jumlah = line
			
	print("Jumlah uang saat ini:\n \033[0;31mRp.",jumlah)
	print()
	print("\033[1;32m (1) Masukan Uang ")
	print(" (2) Keluar Uang ")
	print(" (3) Lihat data i/o")
	print(" (00) Keluar ")
	
	mind = input("\t\033[0m(?)\033[0m ")
	if mind == "1":
		print("\033[1;32mBAGIAN PEMASUKAN\033[0m")
		print()
		jm = int(input("Masukan jumlah uang: "))
		tanggal = input("Masukan tanggal dan hari masuk uang: ")
		asal = input("Asal uang: ")
		print("Memproses..")
		sleep(1)
		semua = jumlah + jm
		ff = open("uang_gp.txt","w")
		ff.write(str(semua))
		ff.close()
		print("Berhasil memasukan data ke uang_ppg.txt")
		sleep(0.3)
		print("Memproses..")
		sleep(1)
		gg = open("data-io.txt","a")
		gg.write("===============\n")
		gg.write("  PEMASUKAN \n")
		gg.write("===============\n")
		gg.write("Tanggal : "+tanggal+"\n")
		gg.write("Asal dana : "+asal+"\n")
		gg.write("Jumlah : "+str(jm)+"\n")
		gg.write("===============\n")
		gg.write(" ")
		gg.close()
		print("Berhasil memasukan data ke data-io.txt")
		print()
		inti()
		
	elif mind == "2":
		print("BAGIAN PENGELUARAN")
		print()
		jml = int(input("Jumlah uang yang keluar: "))
		keperluan = input("Keperluan: ")
		tgl = input("Masukan tanggal dan hari pengeluaran uang: ")
		all = jumlah - jml
		print()
		print("Memproses...")
		sleep(1)
		aa = open("uang_gp.txt","w")
		aa.write(str(all))
		aa.close()
		print("Berhasil memperbarui data pengeluaran di uang_gp.txt")
		sleep(0.3)
		print("Memproses..")
		sleep(1)
		bb = open("data-io.txt","a")
		bb.write("===============\n")
		bb.write(" PENGELUARAN\n")
		bb.write("===============\n")
		bb.write("Tanggal : "+tgl+"\n")
		bb.write("Keperluan : "+keperluan+"\n")
		bb.write("Jumlah : "+str(jml)+"\n")
		bb.write("===============\n")
		bb.write(" ")
		bb.close()
		print()
		print("Berhasil memasukan data ke data-io.txt")
		print()
		inti()
		
	elif mind == "3":
		with open("data-io.txt") as baca:
			for line in baca:
				print(line)
				sleep(0.2)
		print(" [a] kembali ke awal")
		print(" [b] keluar")
		m = input("_> ")
		if m == "a":
			inti()
		elif m == "b":
			sys.exit()
		else:
			print("Error input")
			sleep(1)
			sys.exit()
	elif mind == "00":
		sys.exit()
		
	else:
		inti()
		
		

inti()
		
		