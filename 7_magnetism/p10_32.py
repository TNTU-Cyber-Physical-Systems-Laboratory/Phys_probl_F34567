import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 10.32", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="l (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    l_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.4")
    l_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="v (m/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    v_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 5")
    v_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="B (T):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    B_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 0.01")
    B_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="I (A):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    I_entry = ctk.CTkEntry(frame4, placeholder_text="e.g., 20")
    I_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            l = float(l_entry.get())
            v = float(v_entry.get())
            B = float(B_entry.get())
            I = float(I_entry.get())

            P = B * I * l * v

            result_label.configure(text=f"Required power: {P:.2f} W")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
