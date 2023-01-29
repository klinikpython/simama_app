# file: konfigurasi_val.py
#
# pengaturan KONFIGURASI_VALIDASI (Controller)
#
# start: 28 Jan 2023
# finish: -
# update: -
#

import xlrd

PESAN = ["File excel tidak sesuai tipe ujian",
		"Validasi SUKSES!"]

# KOLOM: SIMA
KOLOM = (16,)

# MAT, ENG, IND, FIS, KIM, BIO
NILAI_MAX_SIMA = (150, 150, 50, 50, 50, 50)


class KonfigurasiVAL:
	def __init__(self):
		self.stSukses = True
		self.pesan = PESAN[-1]
		
	def atur_validasi(self, namafile, paket):
		self.namafile = namafile
		self.paket = paket
		
		# baca file-excel
		wb = xlrd.open_workbook(self.namafile)
		sh = wb.sheet_by_index(0)
		
		# ambil jumlah kolom file-excel
		jumKolom = sh.ncols
		jumBaris = sh.nrows
		
		#print(jumKolom, jumBaris)
		
		# validasi per bagian
		data_validasi = [self.validasi_kolom]
		
		for i in range(len(data_validasi)):
			if self.stSukses:
				data_validasi[i](sh, jumKolom, jumBaris)
			else:
				break
		
		#print("Status Sukses: {}".format(self.stSukses))
		#print("Informasi : {}".format(self.pesan))
		
	def validasi_kolom(self, sheet, jumkol, jumbar):
		# vaidasi jumlah kolom
		if (self.paket=='sima'):
			if jumkol != KOLOM[0]:
				self.pesan = PESAN[0]
				self.stSukses = False
			else:
				self.pesan = PESAN[-1]
				self.stSukses = True				
				
		#print("==JUMLAH KOLOM== : {}".format(self.pesan))
				
	def ambil_data_validasi(self):
		#print(self.pesan, self.stSukses)
		return (self.pesan, self.stSukses)

				



		

		


