# This code makes use of the tkinter and selenium modules to gather the latest python events and display it in a GUI
# window that uses the tkinter library. First, the root window is initialized and configured to give it a title and
# background color. Then, a selenium webdriver is used to navigate to the python homepage in order to extract the
# desired data. Labels are then set up for the date and the event, with grid positions and formatting. A for loop is
# then used to navigate the XPath for the latest five python events, for the date and event respectively. The loop
# appends labels to the root window with the desired data, along with configurations for font, anchor, and background
# color. Lastly, the webdriver is closed and the root window is executed.

from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize root window
root = Tk()
root.title("Python Latest Events")
root.config(padx=20, pady=40, bg="#CFB997")

# Navigate to python home page
driver = webdriver.Chrome()
driver.get('https://www.python.org/')

# Set labels
date_label = []
event_label = []
date = Label(text="Date", font="Arial 18 bold", bg="#CFB997", fg="#567189", pady=10, anchor="w")
date.grid(row=0, column=0)
event = Label(text="Event", font="Arial 18 bold", bg="#CFB997", fg="#567189", pady=10, anchor="w", width=40)
event.grid(row=0, column=1)

# Find the latest python events
for i in range(5):
    date_label.append(Label(root,
                            text=driver.find_element(By.XPATH,
                                                     f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/time').text.split(
                                "T")[0]))
    event_label.append(Label(root,
                             text=driver.find_element(By.XPATH,
                                                      f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i + 1}]/a').text))

    # Set grid positions and formatting
    date_label[i].grid(row=i + 1, column=0)
    event_label[i].grid(row=i + 1, column=1)
    event_label[i].config(anchor='w')
    date_label[i].config(font="Arial 18", bg="#7B8FA1", fg="#CFB997")
    event_label[i].config(font="Arial 18", padx=10, width=40, anchor="w", bg="#567189", fg="#FAD6A5")

# Close browser and run window
driver.quit()
root.mainloop()