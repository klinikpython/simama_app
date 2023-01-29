# file: simama_gui.py
#
# pengaturan GUI (View)
#
# start: 28 Jan 2023
# finish: -
# update: -
#

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import tkinter.font as fo
from PIL import ImageTk, Image


MATERI_SIMA = ("Matematika", "Bahasa Inggris", "Bahasa Indonesia", 
				"Fisika", "Kimia", "Biologi")

KOLOM_DATA = [('no', 'NO', 30), ('noji', 'NO UJIAN', 75),
				('nama', 'NAMA PESERTA', 150), ('mat', 'MAT', 40),
				('eng', 'ENG', 40),('ind', 'IND', 40),('fis', 'FIS', 40),
				('kim', 'KIM', 40),('bio', 'BIO', 40),('tot', 'NILAI', 50), 
				('rank', 'RANK', 50), ('stat', 'STATUS', 75)]
				
KOLOM_PANEL = [('a', 'A', 10), ('b', 'B', 30), ('c', 'C', 50), ('d', 'D', 100),
				('e', 'E', 100), ('f', 'F', 100), ('g', 'G', 100),
				('h', 'H', 100), ('i', 'I', 100), ('j', 'J', 10)]
				
JENJANG = ("11 SMA", "11 MA", "12 SMA", "12 MA", "12 SMK",
	"ALUMNI", "CPNS", "PPPK")


class SimamaGUI:
	def __init__(self, parent, wx, wy):
		self.parent = parent
		
		self.parent.title("Olah Data Tryout :: SIMAMA")
		self.parent.resizable(False, False)
		#self.protocol("WM_DELETE_WINDOW", self.klik_btn_x)

		self.tengah_layar(wx, wy)
		self.atur_style()
		self.atur_komponen()		

		self.form_load()
		self.konfig = None
		
	def tengah_layar(self, panjang, lebar):
		setX = (self.parent.winfo_screenwidth()-panjang)/2
		setY = (self.parent.winfo_screenheight()-lebar-80)/2

		self.parent.geometry("%ix%i+%i+%i"%(panjang, lebar, setX, setY))
		
	def atur_style(self):
		sty = ttk.Style()
		sty.configure('bg.TFrame', background='white')
		sty.configure('bg.TLabel', background='white')
		sty.configure('teks.TLabel', background='#D2DC02', foreground='#201E1E')
			
	def atur_komponen(self):
		# atur frame_utama
		mainframe = ttk.Frame(self.parent, style='bg.TFrame', borderwidth=5)
		mainframe.pack(fill='both', expand=1)
		
		# label judul
		st_judul = fo.Font(size=20, weight='bold')
		judul = ttk.Label(mainframe, text='  Import File SIMAMA', 
			style='teks.TLabel', anchor='w', font=st_judul)
		judul.pack(side='top', fill='x', ipady=10)
		
		## box1
		box1 = ttk.Frame(mainframe, style='bg.TFrame')
		box1.pack(side='top', fill='x', pady=5)
		self.view_box1(box1)
		
		## box2
		box2 = ttk.Frame(mainframe, style='bg.TFrame')
		box2.pack(side='top', fill='both', expand=1)
		
		#### box21
		box21 = ttk.Frame(box2, style='bg.TFrame')
		box21.pack(side='left', fill='y')
		self.view_box21(box21)
		
		#pembatas
		ttk.Separator(box2, orient='vertical').pack(side='left',
			fill='y', padx=5)
		
		#### box22
		box22 = ttk.Frame(box2, style='bg.TFrame')
		box22.pack(side='left', fill='both', expand=1)
		self.view_box22(box22)
		
	def form_load(self):
		self.namfiledat = None
		self.datafile = None
		self.btn_input.focus_set()
		
	def atur_kontrol(self, ctrl):
		self.konfig = ctrl
		
	def view_box1(self, frame):
		self.img_input = ImageTk.PhotoImage(Image.open("./src/ico/file.png"))
		self.img_view = ImageTk.PhotoImage(Image.open("./src/ico/search.png"))

		self.btn_input = ttk.Button(frame, text=' Input File',
			command=self.klik_btn_input, width=15,
			image=self.img_input, compound='left')
		self.btn_input.pack(side='left')
		
		self.ent_input = ttk.Entry(frame)
		self.ent_input.pack(side='left', fill='x', expand=1, padx=5)
						
		self.btn_lihat = ttk.Button(frame, command=self.klik_btn_lihat, 
			width=3, image=self.img_view, compound='left')
		self.btn_lihat.pack(side='left')
		
	def view_box21(self, frame):
		#title_profil
		st_profil = fo.Font(size=12, weight='bold')
		judul = ttk.Label(frame, text='  Profil Ujian', style='teks.TLabel',
			anchor='w', font=st_profil)
		judul.pack(side='top', fill='x', ipady=8)
		
		# nama-ujian
		ttk.Label(frame, text='Nama Ujian : ',style='bg.TLabel').pack(side='top', anchor='w')
		self.ent_namji = ttk.Entry(frame, width=35)
		self.ent_namji.pack(side='top', fill='x')
		
		# tgl-ujian
		ttk.Label(frame, text='Tanggal Ujian : ',style='bg.TLabel').pack(side='top', anchor='w')
		self.ent_tagji = ttk.Entry(frame)
		self.ent_tagji.pack(side='top', fill='x')
		
		# jenjang
		ttk.Label(frame, text='Jenjang Kelas : ',style='bg.TLabel').pack(side='top', anchor='w')
		self.cbx_jenjang = ttk.Combobox(frame, values=JENJANG, state='readonly',
			width=30)
		self.cbx_jenjang.pack(side='top', fill='x')
		
		# jum-peserta
		ttk.Label(frame, text='Jumlah Peserta : ',style='bg.TLabel').pack(side='top', anchor='w')
		self.ent_jumpes = ttk.Entry(frame)
		self.ent_jumpes.pack(side='top', fill='x')
		
		# urutan-materi
		ttk.Label(frame, text='Urutan Mapel : ',style='bg.TLabel').pack(side='top', anchor='w')
		
		urutanframe = ttk.Frame(frame, style='bg.TLabel')
		urutanframe.pack(side='top', fill='x')
		
		ttk.Label(urutanframe, text='[ A ] Mapel 1  :   ', style='bg.TLabel').grid(row=0, column=0)
		self.cbx_urut1 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut1.grid(row=0, column=1, sticky='w'+'e')
		
		ttk.Label(urutanframe, text='[ B ] Mapel 2  :   ', style='bg.TLabel').grid(row=1, column=0)
		self.cbx_urut2 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut2.grid(row=1, column=1, sticky='w'+'e', pady=3)
		
		ttk.Label(urutanframe, text='[ C ] Mapel 3  :   ', style='bg.TLabel').grid(row=2, column=0)
		self.cbx_urut3 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut3.grid(row=2, column=1, sticky='w'+'e')
		
		ttk.Label(urutanframe, text='[ D ] Mapel 4  :   ', style='bg.TLabel').grid(row=3, column=0)
		self.cbx_urut4 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut4.grid(row=3, column=1, sticky='w'+'e', pady=3)
		
		ttk.Label(urutanframe, text='[ E ] Mapel 5  :   ', style='bg.TLabel').grid(row=4, column=0)
		self.cbx_urut5 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut5.grid(row=4, column=1, sticky='w'+'e')

		ttk.Label(urutanframe, text='[ F ] Mapel 6  :   ', style='bg.TLabel').grid(row=5, column=0)
		self.cbx_urut6 = ttk.Combobox(urutanframe, state='readonly')
		self.cbx_urut6.grid(row=5, column=1, sticky='w'+'e', pady=3)
		
		self.cb_urut_isi(MATERI_SIMA)

		# tombol proses
		self.img_proses = ImageTk.PhotoImage(Image.open("./src/ico/oke.png"))

		self.btn_proses = ttk.Button(frame, text=' Proses',
			command=self.klik_btn_proses, image=self.img_proses, compound='left')
		self.btn_proses.pack(side='top', fill='x', pady=5)
				
	def view_box22(self, frame):
		#title_tabel
		st_tabel = fo.Font(size=12, weight='bold')
		judul = ttk.Label(frame, text='  Tabel Hasil Akhir', style='teks.TLabel',
			anchor='w', font=st_tabel)
		judul.pack(side='top', fill='x', ipady=8)
		
		# set tabel
		dataFile = ttk.Frame(frame, style='bg.TFrame')
		dataFile.pack(side='top', fill='both', expand=1, pady=3)
		
		self.trvDatFile = ttk.Treeview(dataFile, show='headings',
			selectmode='browse')
		vbar = tk.Scrollbar(dataFile, orient='vertical')

		vbar.pack(side='right', fill='y')
		self.trvDatFile.pack(side='top', fill='both', expand=1)

		self.trvDatFile.config(yscrollcommand=vbar.set)
		vbar.config(command=self.trvDatFile.yview)

		idx = ['nama']
		self.set_kolom_tabel(KOLOM_DATA, self.trvDatFile, idx)
		
		# frame-tombol
		tombolframe = ttk.Frame(frame, style='bg.TFrame')
		tombolframe.pack(pady=5)
		
		self.img_rekap = ImageTk.PhotoImage(Image.open("./src/ico/excel.png"))
		self.img_ekspor = ImageTk.PhotoImage(Image.open("./src/ico/pdf.png"))
		self.img_tutup = ImageTk.PhotoImage(Image.open("./src/ico/close.png"))

		self.btn_ekspor = ttk.Button(tombolframe, text=' Ekspor Semua',
			command=self.klik_btn_ekspor, width=15,
			image=self.img_ekspor, compound='left')
		self.btn_ekspor.pack(side='right')

		self.btn_ekspor1 = ttk.Button(tombolframe, text=' Ekspor Satu',
			command=self.klik_btn_ekspor1, width=15,
			image=self.img_ekspor, compound='left')
		self.btn_ekspor1.pack(side='right', padx=5)
		
		self.btn_rekap = ttk.Button(tombolframe, text=' Rekap Hasil',
			command=self.klik_btn_rekap, width=15,
			image=self.img_rekap, compound='left')
		self.btn_rekap.pack(side='right')
		
	def set_kolom_tabel(self, kolom, tree, indeks):
		datkol = []

		for i in kolom:
			datkol.append(i[0])

		tree.config(column=datkol)

		for kol, judul, pjg in kolom:
			tree.heading(kol, text=judul)
			if kol in indeks:
				tree.column(kol, width=pjg, anchor='w')
			else:                
				tree.column(kol, width=pjg, anchor='center')
		
	def klik_btn_input(self):
		print("KLIK === TOMBOL INPUT FILE")
		namafile = fd.askopenfilename(title = "Pilih File Tryout",
			filetypes=[('File Excel', '*.xls')],
			parent=self.parent)

		if len(namafile)==0:
			print("### tidak-ada-file-terpilih")
			pass
		else:
			print("### file-sudah-terpilih")
			self.namfiledat = namafile
			
			# hapus isi entry-file, kemudian isi sesuai file-data
			print("### isi-entry-namafile")
			self.ent_input.delete(0, 'end')
			self.ent_input.insert('end', self.namfiledat)

			# validasi data input
			print("### validasi-file-terpilih")
			dataValid = self.konfig.val_ambil_data(self.namfiledat, 'sima')
			self.datafile = self.konfig.xls_baca_file(self.namfiledat)
			
			#print(self.datafile)
			
			#print("Status Valid: {}".format(dataValid[1]))
			#print("Info Valid: {}".format(dataValid[0]))
			
			if dataValid[1]:
				print("### file-valid-proses")
				
				if not self.stTampilkanData:
					self.on_komponen()
					self.stTampilkanData = True
					
				# bersihkan database
				print("### hapus-database-awal")
				self.md.dba_hapus_data()
				
				# baca data xls
				print("### membaca-file-input")
				datasis = self.md.xls_baca_file(self.namfiledat)
				#print(datasis)
				
				# simpan data ke database
				print("### simpan-data-siswa")
				self.md.dba_isi_data(datasis)
				
				# tampilkan data ke tabel
				print("### ambil-data-untuk-tabel")
				datasis_show = self.md.dba_ambil_data_show()	
				
				print("### tampilkan-data-pada-tabel")
				self.hapus_tabel(self.trvDatFile)
				self.tampilkan_data(self.trvDatFile, datasis_show)
				
				self.btn_rekap.focus_set()					
				mb.showinfo("Informasi", dataValid[0], parent=self)
			else:
				print("### file-tidak-valid")
				
				# hapus isi entry-file
				self.ent_input.delete(0, 'end')
				
				if self.stTampilkanData:
					self.off_komponen()
					self.stTampilkanData = False
					
				self.hapus_tabel(self.trvDatFile)
					
				self.btn_input.focus_set()					
				mb.showinfo("Informasi", dataValid[0], parent=self)
						
	def klik_btn_lihat(self):
		objSimaPanel = SimamaPanel(self.parent, self.datafile)

	def klik_btn_proses(self):
		pass
		
	def klik_btn_batal(self):
		pass
		
	def klik_btn_ekspor1(self):
		pass

	def klik_btn_ekspor(self):
		pass
		
	def klik_btn_rekap(self):
		pass
		
	def cb_urut_isi(self, listdata):
		self.cbx_urut1.config(values = listdata)
		self.cbx_urut2.config(values = listdata)
		self.cbx_urut3.config(values = listdata)
		self.cbx_urut4.config(values = listdata)
		self.cbx_urut5.config(values = listdata)
		self.cbx_urut6.config(values = listdata)
		

class SimamaPanel(tk.Toplevel):
	def __init__(self, parent, data):
		tk.Toplevel.__init__(self, parent)
		
		self.title("Laporan Hasil SIMAMA")
		self.resizable(False, False)
		self.transient(parent)
		self.grab_set()
		self.protocol("WM_DELETE_WINDOW", self.klik_btn_x)
		self.parent = parent
		self.data = data

		self.tengah_layar(1000, 200)
		self.atur_style()	
		self.atur_komponen()
		
		self.form_load()
		
		self.wait_window()
		
	def tengah_layar(self, panjang, lebar):
		setX = (self.parent.winfo_screenwidth()-panjang)/2
		setY = (self.parent.winfo_screenheight()-lebar-80)/2

		self.geometry("%ix%i+%i+%i"%(panjang, lebar, setX, setY))
		
	def atur_style(self):
		sty = ttk.Style()
		sty.configure('bg.TFrame', background='white')
		sty.configure('bg.TLabel', background='white')
		
	def atur_komponen(self):
		# atur frame_utama
		framepanel = ttk.Frame(self, style='bg.TFrame', borderwidth=5)
		framepanel.pack(fill='both', expand=1)
		
		self.view_panel(framepanel)
		
	def view_panel(self, frame):
		dataFile = tk.Frame(frame)
		dataFile.pack(side='left', fill='both', expand=1)
		
		self.trvDatFile = ttk.Treeview(dataFile, show='headings',
			selectmode='browse')
		vbar = tk.Scrollbar(dataFile, orient='vertical')

		vbar.pack(side='right', fill='y')
		self.trvDatFile.pack(side='top', fill='both', expand=1)

		self.trvDatFile.config(yscrollcommand=vbar.set)
		vbar.config(command=self.trvDatFile.yview)

		idx = ['c']
		self.set_kolom_tabel(KOLOM_PANEL, self.trvDatFile, idx)
				
	def set_kolom_tabel(self, kolom, tree, indeks):
		datkol = []

		for i in kolom:
			datkol.append(i[0])

		tree.config(column=datkol)

		for kol, judul, pjg in kolom:
			tree.heading(kol, text=judul)
			if kol in indeks:
				tree.column(kol, width=pjg, anchor='w')
			else:                
				tree.column(kol, width=pjg, anchor='center')
		
	def form_load(self):
		self.hapus_tabel(self.trvDatFile)
		self.tampilkan_data(self.trvDatFile, self.data)
		
		self.trvDatFile.focus_set()
		
	def klik_btn_x(self, event=None):
		self.destroy()
		
	def tampilkan_data(self, tree, data):
		for dat in data:
			tree.insert('', 'end', values=dat)

		indeks = tree.get_children()
		tree.selection_set(indeks[0])
		
	def hapus_tabel(self, tree):
		indeks = tree.get_children()

		for i in indeks:
			tree.delete(i)
		


				
