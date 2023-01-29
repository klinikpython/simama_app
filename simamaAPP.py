# file: simamaAPP.py
#
# aplikasi olah data TO SIMAMA
#
# start: 28 Jan 2023
# finish:
# update:
#

import gui.simama_gui as ui
import cfg.simama_cfg as cf
import dat.simama_dba as db
import tkinter as tk

class SimamaAPP:
	def __init__(self, parent, wx, wy):
		self.parent = parent
		
		dba = db.SimamaDBA()
		gui = ui.SimamaGUI(self.parent, sx, sy)
		cfg = cf.SimamaCFG(dba, gui)
		
		gui.atur_kontrol(cfg)
				
				
if __name__ == '__main__':
	def set_geometry_formutama(ukuran):
		if ukuran[0]==1024:
			px = 900
		else:
			px = (ukuran[0]*3)//4
		
		py = ukuran[1] - 80
		
		print(px, py)
		
		return px, py

	root = tk.Tk()
	root.tk.call('info', 'patchlevel')
	
	ukuran_layar = (1366, 768)
	sx, sy = set_geometry_formutama(ukuran_layar)
	
	app = SimamaAPP(root, sx, sy)
	
	root.mainloop()
