import os
import tkinter as tk
from tkinter import filedialog
import time
def main():
	def ldfile():
		flname = filedialog.askopenfilename()
		infl.insert(0,flname)
	def svasfl():
		flname = filedialog.asksaveasfilename()
		outfl.insert(0,flname)
	def convert():
		bk = tk.Tk()
		bk.title("Converting...")
		tk.Label(bk,text = "Converting file..").pack()
		tk.Label(bk,text = "Please be patient, may take some time").pack()
		tk.Label(bk,text = "based on file quality and length").pack()
		tk.Label(bk,text = "Program by Zahran Sajid").pack()
		os.system("ffmpeg -i " + '"' +str(infl.get()) + '" ' + '"' + str(outfl.get()) + "." + fltype.get() + '"')
		tk.Label(bk,text = "All Done!! Closing..")
		time.sleep(2)
		bk.destroy()
	root = tk.Tk()
	root.title("Zahran's Video Converter")
	tk.Label(root,text = "Video Converter").pack()
	tk.Label(root,text = "Input file").pack()
	infl = tk.Entry(root)
	infl.pack()
	inbut = tk.Button(root,text = "Browse..",command = ldfile)
	inbut.pack()
	tk.Label(root,text = "Save As").pack()
	outfl = tk.Entry(root)
	outfl.pack()
	outbut = tk.Button(root,text = "Browse..",command = svasfl)
	outbut.pack()
	tk.Label(root,text = "File Type").pack()
	fltype = tk.Entry(root)
	fltype.pack()
	fltype.insert(0,"mp3")
	tk.Label(root,text = "And finally, Convert...").pack()
	convertbut = tk.Button(root,text = "Convert",command = convert)
	convertbut.pack()
	exbut = tk.Button(root,text = "Exit",command = root.destroy)
	exbut.pack()
	root.mainloop()
if __name__ == '__main__':
	main()
