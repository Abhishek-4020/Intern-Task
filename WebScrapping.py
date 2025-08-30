import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# URL and ratings map
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

# Scraping function
def scrape_books(pages):
    product_names, prices, ratings = [], [], []

    progress_bar['maximum'] = pages
    try:
        for page in range(1, pages + 1):
            status_var.set(f"Scraping page {page} of {pages}...")
            root.update_idletasks()

            response = requests.get(BASE_URL.format(page))
            soup = BeautifulSoup(response.content, "html.parser")
            articles = soup.find_all("article", class_="product_pod")

            for article in articles:
                name = article.h3.a["title"]
                price = float(article.find("p", class_="price_color").text.strip()[1:])
                rating = RATING_MAP.get(article.p["class"][1], 0)

                product_names.append(name)
                prices.append(price)
                ratings.append(rating)

            progress_bar['value'] = page
            root.update_idletasks()

        df = pd.DataFrame({
            "Product Name": product_names,
            "Price (GBP)": prices,
            "Rating (1-5)": ratings
        })

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Save as"
        )
        if file_path:
            df.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {file_path}")
        else:
            messagebox.showwarning("Cancelled", "Save cancelled")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        status_var.set("Ready")
        progress_bar['value'] = 0


# -------- GUI Setup --------
root = tk.Tk()
root.title("📚 Book Store Scraper")
root.geometry("450x320")
root.resizable(False, False)

style = ttk.Style()
style.configure('TButton', font=('Segoe UI', 10), padding=6)
style.configure('TLabel', font=('Segoe UI', 10))
style.configure('Header.TLabel', font=('Segoe UI', 16, 'bold'))

# Header
header = ttk.Label(root, text="📘 Scrape Books to CSV", style='Header.TLabel')
header.pack(pady=10)

# Input Frame
frame = ttk.Frame(root)
frame.pack(pady=10)

ttk.Label(frame, text="Number of pages to scrape:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
pages_entry = ttk.Entry(frame, width=5)
pages_entry.insert(0, "1")
pages_entry.grid(row=0, column=1, padx=5, pady=5)

# Button Frame
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

def on_scrape():
    try:
        num_pages = int(pages_entry.get())
        if num_pages < 1:
            raise ValueError
        scrape_books(num_pages)
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid positive integer.")

scrape_btn = ttk.Button(btn_frame, text="Start Scraping 🕵️", command=on_scrape)
scrape_btn.pack()

# Progress bar
progress_bar = ttk.Progressbar(root, length=350, mode='determinate')
progress_bar.pack(pady=15)

# Status
status_var = tk.StringVar(value="Ready")
status_label = ttk.Label(root, textvariable=status_var, foreground="blue")
status_label.pack(pady=5)

# Footer
footer = ttk.Label(root, text="Powered by BeautifulSoup + pandas + tkinter", font=("Segoe UI", 8))
footer.pack(pady=5)

root.mainloop()
