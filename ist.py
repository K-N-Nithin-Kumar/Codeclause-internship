import pyperclip
import pyshorteners
import tkinter as tk
# Initialize the PyShorteners client
s = pyshorteners.Shortener()
# Create a function to shorten the URL
#Gettting the shortened url it is automatically copied to clipboard

def shorten_url():
    url = url_entry.get()
    short_url = s.tinyurl.short(url)
    result_label.config(text=f"Short URL: {short_url}")
    pyperclip.copy(short_url)
# Create the GUI window
window = tk.Tk()
window.title("URL Shortener")

# Create the UI elements
url_label = tk.Label(window, text="Enter URL:")
url_entry = tk.Entry(window, width=100)
shorten_button = tk.Button(window, text="Shorten", command=shorten_url)
result_label = tk.Label(window, text="")

# Add the UI elements to the window
url_label.pack(pady=20)
url_entry.pack(padx=20)
url_entry.pack(pady=20)
shorten_button.pack(pady=20)
result_label.pack(pady=20)

# Start the GUI event loop
window.mainloop()
