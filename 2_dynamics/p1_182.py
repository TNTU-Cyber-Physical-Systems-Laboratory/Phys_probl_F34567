import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 1.60", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="R (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    r_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 150")
    r_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="μ:", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    mu_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 0.7")
    mu_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            R = float(r_entry.get())
            μ = float(mu_entry.get())
            g = 9.81
            vmax = math.sqrt(μ * g * R)
            result_label.configure(text=f"Maximum speed: {vmax:.2f} m/s")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
