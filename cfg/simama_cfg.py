# file: simama_cfg.py
#
# pengaturan FUNGSI (Controller)
#
# start: 28 Jan 2023
# finish: -
# update: -

import json
import xlrd
import xlwt
from .konfigurasi_val import KonfigurasiVAL
#import konfigurasi_pdf as pdf
#import konfigurasi_xls as xls

FILE_CAB = "./src/set/profil_cabang.json"

class SimamaCFG:
	def __init__(self, db, ui):
		self.db = db
		self.ui = ui
		
		self.dba_database_load()
		self.konfigurasi_load()
		
	def dba_database_load(self):
		# ISI DATA AMBANG - SIMAMA
		dat_mat = (1, 'mat', 90) # simama
		dat_eng = (2, 'eng', 90) # simama
		dat_ina = (3, 'ina', 30) # simama
		dat_fis = (4, 'fis', 30) # simama
		dat_kim = (5, 'kim', 30) # simama
		dat_bio = (6, 'bio', 30) # simama
		
		info_ambang = (dat_mat, dat_eng, dat_ina, dat_fis, dat_kim, dat_bio)
		self.db.isi_db_ambang(info_ambang)
		
		# ISI DATA ZONA - SIMAMA
		zona = (1, 'sim', 300, 350, 400) # simama
		self.db.isi_db_zona(zona)
		
		# ISI DATA CABANG
		datacab = self.jso_baca_data_cabang(FILE_CAB)
		self.db.isi_db_cabang(datacab)
		
	def konfigurasi_load(self):
		self.va = KonfigurasiVAL()
		
	def dba_ambil_data_ambang(self):
		mapel = ('mat', 'eng', 'ina', 'fis', 'kim', 'bio')
			
		nil_ambang = []
		for dat in mapel:
			sql = "SELECT nilai FROM nilai_ambang WHERE mapel='{}'".format(dat)
			datnilai = self.dba_eksekusi(sql)
			
			nil_ambang.append(datnilai[0][0])
			
		return tuple(nil_ambang)
		
	def jso_baca_data_cabang(self, data):
		### baca_file json_profil
		f = open(data,)
		data = json.load(f)
		f.close()
		
		datpath = []
		
		for i in data['path']:
			datpath.append(i['filecab'])
			
		filecabang = datpath[0]

		### baca_file json_cabang
		f = open(filecabang,)
		dtcab = json.load(f)
		f.close()
		
		datcabang = [1]
		
		for i in dtcab['cabang']:
			datcabang.append(i['nama'])
			datcabang.append(i['alm1'])
			datcabang.append(i['alm2'])
			datcabang.append(i['telp'])
			datcabang.append(i['logo'])

		return datcabang
		
	def val_ambil_data(self, namafile, paket):
		self.va.atur_validasi(namafile, paket)
		hasil_val = self.va.ambil_data_validasi()
		
		return hasil_val
		
	def xls_baca_file(self, namafile):
		# baca-file-excel
		wb = xlrd.open_workbook(namafile)
		sh = wb.sheet_by_index(0)

		# baris
		b_awal = 2
		b_akhir = sh.nrows - 1
		
		# kolom
		k_awal = 0
		k_akhir = 10
		
		datafile = []
		
		for i in range(b_awal, b_akhir):
			judul = []
			infodat = []
			
			if i==b_awal:
				for j in range(k_awal, k_akhir):
					judul.append(sh.cell(i, j).value)
				datafile.append(judul)
			else:
				for j in range(k_awal, k_akhir):
					isi_sel = sh.cell(i, j).value
					
					if isinstance(isi_sel, str):
						infodat.append(isi_sel)
					else:
						isi_sel = int(isi_sel)
						infodat.append(isi_sel)

				datafile.append(infodat)
				
		return tuple(datafile)

	def dba_eksekusi(self, sql):
		self.db.kursor.execute(sql)
		data = self.db.kursor.fetchall()

		return data	

