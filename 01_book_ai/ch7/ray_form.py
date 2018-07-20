# GUI module
# 
#

import tkinter as tk
import tkinter.messagebox
import re
# my module
from ray import Ray
from responder import NOT_FOUND

# globa var
entry = None
response_area = None
action = None
ray = Ray()
study = 0
what = ''

#------------------------------------------------------------------------------#
# talk func
def talk():
	# global var
	global entry, action, study, what

	value = entry.get()     # get input box value
	subject = action.get()  # get subject selected by menu

	print('Form_subject==', subject)
	print('Form_study==', study)

	if not value:
		response_area.configure(text='What????')
	elif subject == 0 and study == 0:
		response = ray.dialogue(value, subject, study, what)
		response_area.configure(text=response)

		# if res-msg of first char is 'Not Found.'
		m = re.match(NOT_FOUND, response)
		if m != None:
			print('NOT FOUND>>', NOT_FOUND)
			study = 1
			what = value
		print('m===',m)
		# clear input box
		entry.delete(0, tk.END)

	elif subject == 0 and study == 1:
		response = ray.dialogue(value, subject, study, what)
		response_area.configure(text=response)

		# clear flag & what
		study = 0
		what = ''
		# clear input box
		entry.delete(0, tk.END)


#------------------------------------------------------------------------------#
# create GUI
def run():
	# global var
	global entry, response_area, action

	# main window
	root = tk.Tk()
	root.geometry('880x460')
	root.title('Super Bot --Ray-- : ')
	font = ('Helevetica', 14)

	#-------------------------------------------------------#
	def callback():
		if tkinter.messagebox.askyesno('T:Quit?', 'M:Update dictionary?'):
			ray.save()
			root.destroy()
		else:
			root.destroy()
		
	#--------------------
	# when window quit
	root.protocol('WM_DELETE_WINDOW', callback)

	#--------------------
	# menu
	menubar = tk.Menu(root)
	root.config(menu=menubar)

	# File メニューを配置
	# メニューバーを引数にしてMenuオブジェクトを生成
	file_menu = tk.Menu(menubar)
	menubar.add_cascade(label='File', menu=file_menu)
	#file_menu.add_command(label='Close')
	file_menu.add_command(label='Close', command=callback)

	# 科目 メニューを配置
	action = tk.IntVar()
	option_menu = tk.Menu(menubar)
	menubar.add_cascade(label='科目', menu=option_menu)
	option_menu.add_radiobutton(label='世界史', variable = action, value = 0)
	option_menu.add_radiobutton(label='英単語', variable = action, value = 1)

	# イメージを表示させる
	canvas = tk.Canvas(
		root,
		width = 870,
		height = 100,
		relief = tk.RIDGE,
		bd = 2
	)
	canvas.place(x=1, y=0)
	# graphic
	img = tk.PhotoImage(file = '120px-Python.gif')
	canvas.create_image(0,0,image = img, anchor = tk.NW)

	# responce area
	response_area = tk.Label(
		root,
		width = 95,
		height = 10,
		bg = 'LightSkyBlue',
		font = font,
		relief=tk.RIDGE,
		bd = 2
	)
	response_area.place(x=4, y=110)

	# create frame
	frame = tk.Frame(
		root,
		relief=tk.RIDGE,
		borderwidth = 2
	)
	entry = tk.Entry(
		frame,
		width = 70,
		font = font
	)
	entry.pack(side=tk.LEFT)
	entry.focus_set()

	# create button in frame
	button = tk.Button(
		frame,
		width = 15,
		text = 'Input',
		command = talk  # call talk()
	)
	button.pack(side=tk.LEFT)

	# set frame
	frame.place(x=30, y=420)  # 左端から30px 上から420px

	# main loop
	root.mainloop()

#==============================================================================#
# start section
#==============================================================================#
if __name__ == '__main__':
	run()

