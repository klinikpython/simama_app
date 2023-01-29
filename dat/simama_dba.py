# file: simama_dba.py
#
# pengaturan DATABASE (Model)
#
# start: 28 Jan 2023
# finish: -
# update: -

import sqlite3 as lite
import os

FILE_SQL = "./dat/simama.sqlite3"


class SimamaDBA:
	def __init__(self):
		self.atur_database()	
		self.buat_db_awal()	

	def atur_database(self):
		# cek status FILE_SQL , ada atau tidak ada
		statusDB = os.path.exists(FILE_SQL)
		
		if statusDB:
			os.remove(FILE_SQL)
	
		self.koneksi = lite.connect(FILE_SQL)
		self.kursor = self.koneksi.cursor()
		
	def buat_db_awal(self):
		self.buat_db_ambang()
		self.buat_db_zona()
		self.buat_db_cabang()
		
	def buat_db_ambang(self):
		sql_nilambang = """
			CREATE TABLE nilai_ambang(
				norut int,
				mapel text primary key,
				nilai int)
			"""
			
		self.kursor.execute(sql_nilambang)
		
	def buat_db_zona(self):
		sql_zona = """
			CREATE TABLE zona_nilai(
				norut int,
				ujian text primary key,
				kritis int,
				aman int,
				bagus int)
			"""
			
		self.kursor.execute(sql_zona)
		
	def buat_db_cabang(self):
		sql_datacab = """
			CREATE TABLE data_cabang(
				norut int,
				namacab text primary key,
				alamat1 text,
				alamat2 text,
				telpcab text,
				logocab text)
			"""
			
		self.kursor.execute(sql_datacab)

	def isi_db_ambang(self, ambang):
		for info in ambang:
			self.kursor.execute(
				"INSERT INTO nilai_ambang VALUES (?,?,?)", info)
						
		self.koneksi.commit()
				
	def isi_db_zona(self, zona):
		self.kursor.execute(
			"INSERT INTO zona_nilai VALUES (?,?,?,?,?)", zona)
						
		self.koneksi.commit()
		
	def isi_db_cabang(self, cabang):
		self.kursor.execute(
			"INSERT INTO data_cabang VALUES (?,?,?,?,?,?)",
			cabang)
			
		self.koneksi.commit()

						
