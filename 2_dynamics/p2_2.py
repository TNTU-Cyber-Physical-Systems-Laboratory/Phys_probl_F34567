import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 2.2", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="m (kg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    m_entry = ctk.CTkEntry(frame1, placeholder_text="Enter mass")
    m_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="α (deg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    alpha_entry = ctk.CTkEntry(frame2, placeholder_text="Enter angle")
    alpha_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="a (m/s²):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    a_entry = ctk.CTkEntry(frame3, placeholder_text="Enter a")
    a_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="μ:", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    mu_entry = ctk.CTkEntry(frame4, placeholder_text="Enter μ")
    mu_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            m = float(m_entry.get())
            alpha = float(alpha_entry.get())
            a = float(a_entry.get())
            μ = float(mu_entry.get())
            g = 9.81
            alpha_rad = math.radians(alpha)

            N1 = m * math.sqrt(a**2 + g**2)
            N2 = m * (g * math.cos(alpha_rad) + a)
            N3 = m * (g * math.cos(alpha_rad) - a)

            result_label.configure(
                text=f"Force on plane moving horizontally: N1 = {N1:.2f} N\n"
                     f"Force up the incline: N2 = {N2:.2f} N\n"
                     f"Force down the incline: N3 = {N3:.2f} N"
            )
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
