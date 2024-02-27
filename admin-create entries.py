import tkinter as tk
from tkinter import messagebox
import json
import os

dataFile='bookmarkData.json'

def load_categories():
    if not os.path.exists(dataFile) or os.path.getsize(dataFile) == 0:
        with open(dataFile, 'w') as f:
            json.dump([{"Category": "Category 1", "title": "Title 1", "url": "https://example.com"}], f, indent=4)
            return ["Category 1"]  # Return a default category if file is empty or missing
    else:
        with open(dataFile, 'r') as f:
            data = json.load(f)
            categories = sorted(set(entry['Category'] for entry in data))
        return categories

def add_entry():
    category = category_var.get()
    title = title_entry.get()
    url = url_entry.get()

    if category == "" or title == "" or url == "":
        messagebox.showerror("Error", "Please select a category, enter a title, and enter a URL.")
        return

    # Check for duplicate entries
    with open(dataFile, 'r') as f:
        data = json.load(f)
        for entry in data:
            if entry['Category'] == category and entry['title'] == title and entry['url'] == url:
                messagebox.showerror("Error", "Entry already exists.")
                return

    # Add new entry
    new_entry = {"Category": category, "title": title, "url": url}
    data.append(new_entry)
    with open(dataFile, 'w') as f:
        json.dump(data, f, indent=4)
    
    messagebox.showinfo("Success", "Entry added successfully.")

# UI setup
root = tk.Tk()
root.title("Add Entry")

# Category dropdown
category_label = tk.Label(root, text="Category:")
category_label.grid(row=0, column=0, padx=10, pady=5)
category_var = tk.StringVar()
category_dropdown = tk.OptionMenu(root, category_var, *load_categories())
category_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Title entry
title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0, padx=10, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1, padx=10, pady=5)

# URL entry
url_label = tk.Label(root, text="URL:")
url_label.grid(row=2, column=0, padx=10, pady=5)
url_entry = tk.Entry(root)
url_entry.grid(row=2, column=1, padx=10, pady=5)

# Add entry button
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()
