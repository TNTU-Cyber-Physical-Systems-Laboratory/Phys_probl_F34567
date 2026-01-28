import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 3.23", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="M(platform) (kg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    M_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 100")
    M_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="m(human) (kg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    m_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 60")
    m_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="R (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    R_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 2")
    R_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="f (rev/min):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    f_entry = ctk.CTkEntry(frame4, placeholder_text="e.g., 10")
    f_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            M = float(M_entry.get())
            m = float(m_entry.get())
            R = float(R_entry.get())
            f = float(f_entry.get())
            import math

            omega_initial = 2 * math.pi * f / 60
            I_initial = 0.5*M*R**2 + m*R**2
            I_final = 0.5*M*R**2
            omega_final = I_initial * omega_initial / I_final
            f_final = omega_final * 60 / (2 * math.pi)

            result_label.configure(text=f"New rotation frequency: {f_final:.2f} rev/min")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
