from tkinter import *
import datetime 
import time 
import winsound 
from threading import *
from geopy.geocoders import Nominatim
from suntime import Sun
from gnewsclient import gnewsclient
  
# Create Object for tkinter
root = Tk() 
  
# Set geometry 
root.geometry("900x400") 
root.title("ALARM CLOCK")

#function to get news from gnewsclient using user input
def news():
    client=gnewsclient.NewsClient(language=lang.get(),location=loc.get(),
                                topic=top.get(),max_results=3)
    news_list=client.get_news()
    result_title.set(news_list[0]["title"]+ "\n" + news_list[1]["title"]
                    + "\n" + news_list[2]["title"])

#variable classes in tkinter
result_title=StringVar()
result_link=StringVar()
#StringVar() holds a string value in python

#user defined function to get sunrise and sunset time
def sun():
    try:
        geolocator=Nominatim(user_agent="geoapiExercises")
        lad1=str(loc.get())
        location1=geolocator.geocode(lad1)
        latitude=location1.latitude
        longitude=location1.longitude
        
        sun=Sun(latitude,longitude)

        time_zone=datetime.datetime.now()

        sr=sun.get_local_sunrise_time(time_zone)
        ss=sun.get_local_sunset_time(time_zone)

        res_rise=sr.strftime('%H:%M')
        res_dusk=ss.strftime('%H:%M')

        result1.set(res_rise)
        result2.set(res_dusk)
    
    except:
        result1.set("oops something went wrong!")

#variable classes in tkinter
result1=StringVar()
result2=StringVar()

def Threading(): 
    t1=Thread(target=alarm) 
    t1.start() 
  
def alarm(): 
    # Infintite Loop 
    while True: 
        # Set Alarm  
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
  
        # Wait for one seconds 
        time.sleep(1) 
  
        # Get current time 
        current_time = datetime.datetime.now().strftime("%H:%M:%S") 
        print(current_time,set_alarm_time) 
        
        # Check whether set alarm is equal to current time or not 
        if current_time == set_alarm_time: 
            Label(root,text="Wake Up",fg="blue").grid(row=8,column=1)
            Label(root,text="Sunrise",fg='blue').grid(row=13,sticky=W)
            Label(root,text="Sunset",fg='green').grid(row=14,sticky=W)
            news() 
            sun()
            # Playing sound 
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC) 
  
# Add Labels, Frame, Button, Optionmenus 

Label(root,text="Set Time",font=("Helvetica 15 bold")).grid(row=1,sticky=W) 
Label(root, text="Choose Language : ").grid(row=2,sticky=W)
Label(root, text="Choose Location : ").grid(row=3,sticky=W)
Label(root, text="Choose Topic : ").grid(row=4,sticky=W)


lang=Entry(root)
lang.grid(row=2,column=1)

loc=Entry(root)
loc.grid(row=3,column=1)

top=Entry(root)
top.grid(row=4,column=1)



#creating label for class variable
#name using widget Entry
Label(root,text="",textvariable=result_title).grid(row=9,column=1,sticky=W)
Label(root,text="",textvariable=result1).grid(row=13,column=1,sticky=W)
Label(root,text="",textvariable=result2).grid(row=14,column=1,sticky=W)


frame = Frame(root) 
frame.grid(row=1,column=1)
  
hour = StringVar(root) 
hours = ('00', '01', '02', '03', '04', '05', '06', '07', 
         '08', '09', '10', '11', '12', '13', '14', '15', 
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        ) 
hour.set(hours[0]) 
  
hrs = OptionMenu(frame, hour, *hours) 
hrs.grid(row=1,column=1)
  
minute = StringVar(root) 
minutes = ('00', '01', '02', '03', '04', '05', '06', '07', 
           '08', '09', '10', '11', '12', '13', '14', '15', 
           '16', '17', '18', '19', '20', '21', '22', '23', 
           '24', '25', '26', '27', '28', '29', '30', '31', 
           '32', '33', '34', '35', '36', '37', '38', '39', 
           '40', '41', '42', '43', '44', '45', '46', '47', 
           '48', '49', '50', '51', '52', '53', '54', '55', 
           '56', '57', '58', '59', '60') 
minute.set(minutes[0]) 
  
mins = OptionMenu(frame, minute, *minutes) 
mins.grid(row=1,column=2) 
  
second = StringVar(root) 
seconds = ('00', '01', '02', '03', '04', '05', '06', '07', 
           '08', '09', '10', '11', '12', '13', '14', '15', 
           '16', '17', '18', '19', '20', '21', '22', '23', 
           '24', '25', '26', '27', '28', '29', '30', '31', 
           '32', '33', '34', '35', '36', '37', '38', '39', 
           '40', '41', '42', '43', '44', '45', '46', '47', 
           '48', '49', '50', '51', '52', '53', '54', '55', 
           '56', '57', '58', '59', '60') 
second.set(seconds[0]) 
  
secs = OptionMenu(frame, second, *seconds) 
secs.grid(row=1,column=3) 
  
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).grid(row=7,column=1)
  
# Execute Tkinter 
root.mainloop()