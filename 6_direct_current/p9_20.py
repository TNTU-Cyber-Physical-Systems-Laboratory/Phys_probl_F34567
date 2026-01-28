import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)
    ctk.CTkLabel(page, text="Problem 9.20", font=("Arial", 20)).pack(pady=10)

    frame1 = ctk.CTkFrame(page)
    frame1.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="U (V):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    U_entry = ctk.CTkEntry(frame1, placeholder_text="220")
    U_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page)
    frame2.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="P (W):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    P_entry = ctk.CTkEntry(frame2, placeholder_text="100")
    P_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page)
    frame3.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="t1 (°C):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    t1_entry = ctk.CTkEntry(frame3, placeholder_text="2500")
    t1_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page)
    frame4.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="t2 (°C):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    t2_entry = ctk.CTkEntry(frame4, placeholder_text="2500")
    t2_entry.grid(row=0, column=1, padx=5, pady=5)

    frame5 = ctk.CTkFrame(page)
    frame5.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame5, text="n (times):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    n_entry = ctk.CTkEntry(frame5, placeholder_text="15")
    n_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor="w")

    def calculate():
        try:
            U = float(U_entry.get())
            P = float(P_entry.get())
            t1 = float(t1_entry.get())
            t2 = float(t2_entry.get())
            n = float(n_entry.get())
            R1 = U**2 / P
            R2 = R1 / n
            alpha = (R1 - R2) / (R2 * (t1 - t2))
            result_label.configure(text=f"R2 = {R2:.2f} Ω\nα = {alpha:.5f} 1/°C")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20)
    return page
