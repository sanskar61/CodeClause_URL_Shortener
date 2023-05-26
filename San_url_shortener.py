from tkinter import*
import pyshorteners

def shorten_url():
    url = entry.get()
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    result_label.insert(END, shortened_url)

# Create the main window

window = Tk()
window.geometry('350x130')
window.title("URL Shortener")

# Create GUI components
label = Label(window, text="Enter URL:",bg="yellow", foreground="red", font=('Times', 10, 'bold'))
label.pack()

entry = Entry(window, width=30)
entry.pack()

button = Button(window, text="Shorten", command=shorten_url, bg="pink", activebackground="green", foreground="blue", font=('Times', 10, 'bold'))
button.pack()


result_label = Entry(window, width = 30)
result_label.pack()


# Run the main event loop
window.mainloop()
