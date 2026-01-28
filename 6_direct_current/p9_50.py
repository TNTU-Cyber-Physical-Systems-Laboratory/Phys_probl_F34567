import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 9.50", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="E (V/m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    E_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 20")
    E_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="j (A/m²):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    j_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 6.58e-6")
    j_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="b+ (m²/V·s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    bplus_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 1.38e-4")
    bplus_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="b- (m²/V·s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    bminus_entry = ctk.CTkEntry(frame4, placeholder_text="e.g., 1.91e-4")
    bminus_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            E = float(E_entry.get())
            j = float(j_entry.get())
            b_plus = float(bplus_entry.get())
            b_minus = float(bminus_entry.get())

            n = j / (E * (b_plus + b_minus))

            result_label.configure(text=f"Ion concentration n: {n:.2e} m⁻³")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
