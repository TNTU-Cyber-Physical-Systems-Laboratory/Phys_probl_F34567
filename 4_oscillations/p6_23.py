import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 6.23", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="L (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    L_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.8")
    L_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="a (m/s²):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    a_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 4")
    a_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            L = float(L_entry.get())
            a = float(a_entry.get())
            g = 9.81

            g_eff = math.sqrt(g**2 + a**2)

            T = 2 * math.pi * math.sqrt(L / g_eff)

            result_label.configure(text=f"Period of oscillations: {T:.2f} s")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
