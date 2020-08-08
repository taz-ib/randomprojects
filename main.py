from tkinter import *
from tkinter.ttk import *
from speedtest import Speedtest


def update_text():
    server = [4588]
    st = Speedtest()
    st.get_servers(servers=server)
    download = st.download(threads=2)
    upload = st.upload(threads=2)
    download_speed = round(download / 2 ** 20, 2)
    upload_speed = round(upload / (2 ** 20), 2)
    down_label.config(text="Download Speed - " + str(download_speed) + "Mbps")
    up_label.config(text="Upload Speed - " + str(upload_speed) + "Mbps")


root = Tk()
root.title("Internet Speed Checker")
root.geometry('300x300')
button = Button(root, text="Get Speed", width=30, command=update_text)
button.pack()
style = Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='cyan')
bar = Progressbar(root, style='black.Horizontal.TProgressbar', mode='indeterminate')
bar.pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()
info = Label(root, text="")
info.pack()

root.mainloop()
