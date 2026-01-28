import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 10.27", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="R (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    R_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.04")
    R_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="d (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    d_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 0.05")
    d_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="I (A):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    I_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 4")
    I_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            R = float(R_entry.get())
            d = float(d_entry.get())
            I = float(I_entry.get())
            mu0 = 4 * math.pi * 1e-7
            B_single = (mu0 * I * R**2) / (2 * ((R**2 + (d/2)**2)**1.5))
            B_same = 2 * B_single
            B_opposite = 0

            result_label.configure(text=f"Magnetic field B (same dir): {B_same:.6f} T\n"
                                       f"Magnetic field B (opposite dir): {B_opposite:.6f} T")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
