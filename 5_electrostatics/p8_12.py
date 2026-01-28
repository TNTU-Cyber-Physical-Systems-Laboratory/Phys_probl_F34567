import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 8.12", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="m (kg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    m_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.003")
    m_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="q (C):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    q_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 0.01e-3")
    q_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="E (V/m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    E_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 1000")
    E_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="α (degrees):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    alpha_entry = ctk.CTkEntry(frame4, placeholder_text="e.g., 90")
    alpha_entry.grid(row=0, column=1, padx=5, pady=5)

    frame5 = ctk.CTkFrame(page, fg_color="transparent")
    frame5.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame5, text="β (degrees):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    beta_entry = ctk.CTkEntry(frame5, placeholder_text="e.g., 60")
    beta_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            m = float(m_entry.get())
            q = float(q_entry.get())
            E = float(E_entry.get())
            alpha_deg = float(alpha_entry.get())
            beta_deg = float(beta_entry.get())
            g = 9.81

            alpha = math.radians(alpha_deg)
            beta = math.radians(beta_deg)


            v2 = 2 * g * (1 - math.cos(alpha)) + 2 * E * q / m * (1 - math.cos(alpha))
            v = math.sqrt(v2) if v2 >= 0 else 0

            T = m * g * math.cos(beta) + m * v**2 
            result_label.configure(text=f"Tension in string: {T:.4f} N")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
