import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    ctk.CTkLabel(page, text="Problem 8.122", font=("Arial", 20)).pack(pady=10)

    frame1 = ctk.CTkFrame(page)
    frame1.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="d1 (cm):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    d1_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 3")
    d1_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page)
    frame2.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="d2 (cm):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    d2_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 1")
    d2_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page)
    frame3.pack(pady=10, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="U (kV):", font=("Arial", 16)).grid(row=0, column=0, sticky="w")
    U_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 2")
    U_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor="w")

    def calculate():
        try:
            d1 = float(d1_entry.get()) / 100
            d2 = float(d2_entry.get()) / 100
            U = float(U_entry.get()) * 1e3
            eps0 = 8.854e-12
            S = 60e-4

            C1 = eps0 * S / d1
            C2 = eps0 * S / (d1 - d2)
            delta_W = 0.5 * C1 * U**2 - 0.5 * C2 * U**2
            result_label.configure(text=f"Energy lost: {abs(delta_W):.2e} J")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20)
    return page
