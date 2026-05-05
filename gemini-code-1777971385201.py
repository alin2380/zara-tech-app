import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class ZaraTechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zara Tech Mart - Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#f0f2f5")

        # Database Setup
        self.conn = sqlite3.connect("zaratech.db")
        self.create_tables()

        # Styles
        self.primary_color = "#2c3e50"
        self.secondary_color = "#34495e"
        self.text_color = "white"

        # --- Sidebar ---
        self.sidebar = tk.Frame(self.root, bg=self.primary_color, width=220)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = tk.Label(self.sidebar, text="ZARA TECH", font=("Arial", 16, "bold"), 
                                   bg=self.primary_color, fg="#1abc9c", pady=20)
        self.logo_label.pack()

        # --- Main Workspace ---
        self.workspace = tk.Frame(self.root, bg="white")
        self.workspace.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        self.create_menu()
        self.show_dashboard()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER)")
        self.conn.commit()

    def create_menu(self):
        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Inventory", self.inventory_section),
            ("Sales", lambda: messagebox.showinfo("Info", "Sales Section Coming Soon")),
            ("Customers", lambda: messagebox.showinfo("Info", "Customer Management Coming Soon")),
            ("RMA Section", lambda: messagebox.showinfo("Info", "RMA Module Coming Soon")),
            ("Exit", self.root.quit)
        ]

        for text, cmd in buttons:
            btn = tk.Button(self.sidebar, text=text, font=("Arial", 11), bg=self.secondary_color, 
                            fg=self.text_color, bd=0, pady=10, anchor="w", padx=20, 
                            cursor="hand2", command=cmd)
            btn.pack(fill="x", pady=2)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#1abc9c"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.secondary_color))

    def clear_workspace(self):
        for widget in self.workspace.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_workspace()
        tk.Label(self.workspace, text="Welcome to Zara Tech Mart", font=("Arial", 22, "bold"), bg="white").pack(pady=40)
        tk.Label(self.workspace, text="Location: Badda, Dhaka", font=("Arial", 12), bg="white").pack()

    def inventory_section(self):
        self.clear_workspace()
        tk.Label(self.workspace, text="Inventory Management", font=("Arial", 18, "bold"), bg="white").pack(pady=10)
        
        # Simple Add Product Form
        form_frame = tk.Frame(self.workspace, bg="white")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", bg="white").grid(row=0, column=0)
        e_name = tk.Entry(form_frame)
        e_name.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Price:", bg="white").grid(row=0, column=2)
        e_price = tk.Entry(form_frame)
        e_price.grid(row=0, column=3, padx=5)

        def add_data():
            if e_name.get() and e_price.get():
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (e_name.get(), e_price.get()))
                self.conn.commit()
                messagebox.showinfo("Success", "Product Added!")
                self.inventory_section()
            else:
                messagebox.showwarning("Error", "Fill all fields")

        tk.Button(form_frame, text="Add", command=add_data, bg="#1abc9c", fg="white").grid(row=0, column=4, padx=10)

        # Show Table
        tree = ttk.Treeview(self.workspace, columns=("ID", "Name", "Price"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Product Name")
        tree.heading("Price", text="Price")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price FROM products")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZaraTechApp(root)
    root.mainloop()