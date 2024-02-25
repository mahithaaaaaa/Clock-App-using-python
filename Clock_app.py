from tkinter import *
from tkinter.ttk import Combobox
from threading import Thread

from datetime import datetime
from time import sleep,strftime

from PIL import ImageTk, Image
from pygame import mixer

# ******Time*******
def displayTime():
	# creating tkinter window
	root = Tk()
	root.title('Clock')
	# This function is used to display time on the label
	def time():
		string = strftime('%H:%M:%S %p')
		lbl.config(text = string)
		lbl.after(1000, time)
	# Styling the label widget so that clock
	lbl = Label(root, font = ('calibri', 40, 'bold'),
					  background = 'purple',
					  foreground = 'white')
	# Placing clock at the centre of the tkinter window
	lbl.pack(anchor = 'center')
	time()
	mainloop()

# ******StopWatch*******
def stopWatch():
	running = False
	def counter_label(lbl1):
		def count():
			if running:
				global counter
				# To manage the initial delay.
				if counter == 1:
					display = "Starting..."
				else:
					temp_time = datetime.fromtimestamp(counter)
					string = temp_time.strftime("%H:%M:%S")
					display = string
				lbl1.config(text = display)
				lbl1.after(1000, count)
				counter += 1
		# Triggering the start of the counter.
		count()	
	# start function of the stopwatch
	def Start(lbl1):
		global running
		running=True
		counter_label(lbl1)
		start['state']='disabled'
		stop['state']='normal'
		reset['state']='normal'
	# Stop function of the stopwatch
	def Stop():
		global running
		start['state']='normal'
		stop['state']='disabled'
		reset['state']='normal'
		running = False
	# Reset function of the stopwatch
	def Reset(lbl1):
		global counter
		counter=1
		# If rest is pressed after pressing stop.
		if running==False:	
			reset['state']='disabled'
			lbl1['text']='Welcome!'
		# If reset is pressed while the stopwatch is running.
		else:			
			lbl1['text']='Starting...'
	sw = Tk()
	sw.title("Stopwatch")
	# Fixing the window size.
	sw.minsize(width=250, height=70)
	lbl1 = Label(sw, text="Welcome!", fg="black", font="Verdana 30 bold")
	lbl1.pack()
	f = Frame(sw)
	start = Button(f, text='Start', width=6, command=lambda:Start(lbl1))
	stop = Button(f, text='Stop',width=6,state='disabled', command=Stop)
	reset = Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(lbl1))
	f.pack(anchor = 'center',pady=5)
	start.pack(side="left")
	stop.pack(side ="left")
	reset.pack(side="left")
	sw.mainloop()

# ******Alarm******
def Alarm():
	#colors
	bg_color = '#ffffff'
	co1 = "#566FC6" #blue

	window = Tk()
	window.title("Alarm")
	window.geometry('350x150')
	window.configure(bg=bg_color)
	#frame up
	frame_line = Frame(window, width=400, height=5, bg=co1)
	frame_line.grid(row=0, column=0)
	frame_body = Frame(window, width=400, height=290, bg=bg_color)
	frame_body.grid(row=1, column=0)
	#configuring frame body
	img = Image.open('icon1.png')
	img.resize((100, 100))
	img = ImageTk.PhotoImage(img)

	app_image = Label(frame_body, height=100, image=img, bg=bg_color)
	app_image.place(x=10, y=10)

	name = Label(frame_body, text = "Alarm", height=1, font=('Ivy 18 bold'), bg=bg_color)
	name.place(x=125, y=10)

	hour = Label(frame_body, text = "hour", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
	hour.place(x=127, y=40)
	c_hour = Combobox(frame_body, width=2, font=('arial 15'))
	c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
	c_hour.current(0)
	c_hour.place(x=130, y=58)

	min = Label(frame_body, text = "min", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
	min.place(x=177, y=40)
	c_min = Combobox(frame_body, width=2, font=('arial 15'))
	c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
	c_min.current(0)
	c_min.place(x=180, y=58)

	sec = Label(frame_body, text = "sec", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
	sec.place(x=227, y=40)
	c_sec = Combobox(frame_body, width=2, font=('arial 15'))
	c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
	c_sec.current(0)
	c_sec.place(x=230, y=58)

	period = Label(frame_body, text = "period", height=1, font=('Ivy 10 bold'), bg=bg_color, fg=co1)
	period.place(x=277, y=40)
	c_period = Combobox(frame_body, width=3, font=('arial 15'))
	c_period['values'] = ("AM", "PM")
	c_period.current(0)
	c_period.place(x=280, y=58)

	def activate_alarm():
		t = Thread(target=alarm)
		t.start()

	def deactivate_alarm():
		print('Deactivated alarm: ', selected.get())
		mixer.music.stop()

	selected = IntVar()

	rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value = 1, text = "Activate", bg=bg_color, command=activate_alarm, variable=selected)
	rad1.place(x = 125, y=95)

	def sound_alarm():
		mixer.music.load('alarm2.mp3')
		mixer.music.play()
		selected.set(0)

		rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text = "Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
		rad2.place(x = 200, y=95)

	def alarm():
		while True:
			control = selected.get()
			#print(control)

			alarm_hour=c_hour.get()
			alarm_minute = c_min.get()
			alarm_sec = c_sec.get()
			alarm_period = c_period.get()
			alarm_period = str(alarm_period).upper()

			now = datetime.now()
			hour = now.strftime("%I")
			minute = now.strftime("%M")
			second = now.strftime("%S")
			period = now.strftime("%p")

			if control == 1:
				if alarm_period == period:
					if alarm_hour == hour:
						if alarm_minute == minute:
							if alarm_sec == second:
								print("Time to take a break!")
								sound_alarm()
			sleep(1)
	mixer.init()
	window.mainloop()

# ******Timer******
def timer():
	win = Tk()
	win.geometry('350x150')
	#win.resizable(False,False)
	#Configure the background
	win.config(bg='#ffffff')
	#Create Entry Widgets for HH MM SS
	sec = StringVar()
	Entry(win, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=200, y=60)
	sec.set('00')
	mins= StringVar()
	Entry(win, textvariable = mins, width =2, font = 'Helvetica14').place(x=160, y=60)
	mins.set('00')
	hrs= StringVar()
	Entry(win, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=120, y=60)
	hrs.set('00')
	#Define the function for the timer
	def countdowntimer():
		times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
		while times > -1:
			minute,second = (times // 60 , times % 60)
			hour =0
			if minute > 60:
				hour , minute = (minute // 60 , minute % 60)
			sec.set(second)
			mins.set(minute)
			hrs.set(hour)
			win.update()
			# time.sleep(1)
			sleep(1)
			if(times == 0):
				sec.set('00')
				mins.set('00')
				hrs.set('00')
			times -= 1
	Label(win, font =('Helvetica bold',22), text = 'Set the Timer',bg ='#ffffff').place(x=80,y=10)
	Button(win, text='START', bd ='2', bg = '#566FC6',fg='#ffffff',font =('Helveticabold',10), command = countdowntimer).place(x=142, y=105)
	win.mainloop()

print("\n\n\n\n\n")
print("\t\t\t-----------------")
print("\t\t\t|     CLOCK     |")
print("\t\t\t|               |")
print("\t\t\t|  1.Time       |")
print("\t\t\t|  2.Alarm      |")
print("\t\t\t|  3.Stop Watch |")
print("\t\t\t|  4.Timer      |")
print("\t\t\t-----------------")
v = int(input("\t\tEnter your choice: "))
match v:
	case 1:
		displayTime()
	case 2:
		Alarm()	
	case 3:
		stopWatch()
	case 4:
		timer()
	case default:
		print("Enter Valid Input !!!")

