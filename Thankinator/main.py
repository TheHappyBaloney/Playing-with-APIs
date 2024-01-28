import requests
import io
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk
from flask import Flask, render_template, jsonify
from ttkbootstrap import Style

root = tk.Tk()
root.title("Thankinator")
root.geometry("1000x500")
root.resizable(False, False)
root.configure(bg="white")
style = Style(theme="sandstone")

#define a function to retireve and display an image based on the selected category

def get_image(category):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=2bSdjeiQ2cPm9Gj8pVOvC3tRLgGrBCilIu5NBRJShL8"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((500, 500), resample=Image.LANCZOS))
    return {"image_data": photo}  

def enable_button():
    generate_button.config(state = "normal" if category_var.get() != "Choose a category" else "disabled")

def create_gui():
    global category_var, generate_button, label

    category_var = tk.StringVar(value="Choose a category")
    category_options = ["Choose a category", "People" , "Nature" , "Technology" , "Animals" , "Art" , "Random"]

    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)

    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=15)

    generate_button = ttk.Button(root, text="Generate", state="disabled", command=lambda: get_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root,background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()


if __name__ == "__main__":
    create_gui()



