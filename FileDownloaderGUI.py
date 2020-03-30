import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as tkFont
import urllib.request
import math
from os.path import basename
import threading
from tkinter import messagebox

def download_file(url,segments=10): ##Default segments=10
    def callback():
        progress = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate')
        progress.pack()
        progress.place(x=10,y=200)
        request=urllib.request.urlopen(url)
        filename=str(file_name_field.get()) ##filename will be the basepath of url
        meta=request.info()  ## get information from request object used for determining size of content
        file_size=int(meta['Content-Length'])
        buffer_size=file_size/segments
        file_name1.configure(text="Filename: "+filename)
        print("File size : {0:.2f}".format(float((file_size/1024)/1024))) ## get file size in MB
        file_download_size.configure(text="File Size: {0:.2f} MB".format((file_size/1024)/1024))
        total_download=0
        fd=open(filename,'wb')  ## save file to current working directory
        while total_download!=file_size:
            buffer=request.read(int(buffer_size))  ## reading files upto buffer_size
            fd.write(buffer)
            total_download+=len(buffer)
            cur_download.configure(text="Downloaded {0}%".format(math.trunc((int(total_download)/int(file_size))*100)))
            progress['value'] = math.trunc((int(total_download)/int(file_size))*100)## To retrieve percentage of download
        print("Download success")
        fd.close()
        file_download_size.destroy()
        file_name1.destroy()
        progress.destroy()
        cur_download.destroy()
        messagebox.showinfo("File Downloaded", "Your file {0} has been saved in current directory".format(filename))
    t = threading.Thread(target=callback)
    t.start()


def start_download():

    url=str(url_field.get())
    segments=int(segment_field.get())
    download_file(url,segments)
    



root = tk.Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=25)
fontStyle1 = tkFont.Font(family="Lucida Grande", size=13)

w=tk.Label(root,text="File Downloader with segments",font=fontStyle)
url_label=tk.Label(root,text="URL",font=fontStyle1)
segments_label=tk.Label(root,text="Segments",font=fontStyle1)
cur_download=tk.Label(root,text="",fg="green")
file_download_size=tk.Label(root,text="",fg="green")
file_name1=tk.Label(root,text="",fg="green")
url_field = tk.Entry(root,width=100)
file_name_label=tk.Label(root,text="Output File Name",font=fontStyle1)
file_name_field= tk.Entry(root)
segment_field = tk.Entry(root)

button = tk.Button(root,text="Download",font=fontStyle1 ,fg="green",command=start_download)

file_name1.pack()
file_download_size.pack()
file_name_label.pack()
file_name_field.pack()
cur_download.pack()
w.pack()
url_label.pack()
segments_label.pack()
url_field.pack()
segment_field.pack()
button.pack()

file_name1.place(x=10,y=150)
file_download_size.place(x=10,y=165)
file_name_label.place(x=250,y=100)
file_name_field.place(x=390,y=100)

cur_download.place(x=10,y=180)
url_label.place(x=10,y=60)
segments_label.place(x=10,y=100)
url_field.place(x=90,y=60)
segment_field.place(x=90,y=100)
button.place(x=350,y=130)
root.minsize(800,500)
root.mainloop()
