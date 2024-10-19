from PIL import Image, ImageTk
from tkinter import Tk, BOTH, X, Toplevel
import tkinter.ttk as ttk
from tkinter.ttk import Frame, Label, Style, Progressbar
import time
import pandas
import numpy
from geopy.geocoders import Nominatim
import json

width = 400
height = 250

def location(place):
    try:
        geolocator = Nominatim(user_agent="traffic_management_system")
        location = geolocator.geocode(place)
        if location:
            lat = "{0:.2f}".format(location.latitude)
            lng = "{0:.2f}".format(location.longitude)
            return '{' + lat + ',' + lng + '}'
        return '{0.00,0.00}'  # Default coordinates if location not found
    except Exception as e:
        print(f"Error getting location for {place}: {str(e)}")
        return '{0.00,0.00}'  # Default coordinates in case of error

# Dictionary with locations
d = {
    1: "Big Ben  " + location("Big Ben, London"),
    2: "Gariahat  " + location("Gariahat, Kolkata"),
    3: "Jadavpur  " + location("Jadavpur, Kolkata"),
    4: "Times Square  " + location("Times Square, New York"),
    5: "Rasbehari  " + location("Rasbehari Avenue, Kolkata"),
    6: "Garia  " + location("Garia, Kolkata"),
    7: "Tollygunge  " + location("Tollygunge, Kolkata"),
    8: "Chingrihata  " + location("Chingrihata, Kolkata"),
    9: "Saltlake  " + location("Salt Lake City, Kolkata")
}

class Traffic(Toplevel):
    # Rest of your Traffic class remains the same
    def __init__(self):
        Toplevel.__init__(self)
        self.title("TRAFFIC MANAGEMENT SYSTEM")
        self.configure(background="white")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.initUI(1, 1, 1, 1)
        for i in range(1, 3):
            for j in range(1, 10):
                self.initUI(i, j, (j - 1) % 3 + 1, (j - 1) // 3 + 1)
            time.sleep(5)

    def initUI(self, path, pic, xi, yi):
        stgImg = Image.open(str((path-1)*5) + "//" + str(pic) + ".jpg")
        stgImg = stgImg.resize((width, height), Image.LANCZOS)
        stgImg2 = ImageTk.PhotoImage(stgImg)
        
        data = pandas.read_csv("output" + str((path-1)*5) + ".csv", header=None)
        var = data.to_numpy()
        
        label = Label(self, image=stgImg2)
        label.image = stgImg2
        label.place(x=543*xi-543+20, y=280*yi-300+10)
        
        label1 = Label(self)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')
        
        progress = Progressbar(label1, style="red.Horizontal.TProgressbar", length=100, mode='determinate')
        progress['value'] = int(var[pic-1][1]*20)
        
        fn = str(var[pic-1][1]) + " mins"
        fn1 = d[pic]
        
        label2 = Label(self, text=fn, font="arial 12 bold", background="#f0d630")
        label2.place(x=543*xi-317-90, y=280*yi-50+17)

        label3 = Label(self, text=fn1, font="arial 12 bold", background="white")
        label3.place(x=543*xi-235.5-90, y=280*yi-50+18)

        progress.pack()
        label1.place(x=543*xi-540+20, y=280*yi-50+18)
        self.update_idletasks()