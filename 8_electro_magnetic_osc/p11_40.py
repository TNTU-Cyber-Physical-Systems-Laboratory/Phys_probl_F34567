import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 11.40", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="w (J/m³):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    w_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.5")
    w_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="S (m²):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    S_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 1")
    S_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="t (s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    t_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 120")
    t_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            w = float(w_entry.get())
            S = float(S_entry.get())
            t = float(t_entry.get())
            c_light = 3e8

            P_avg = w * c_light 
            energy = P_avg * t * S

            result_label.configure(text=f"Poynting vector magnitude: {P_avg:.2e} W/m²\n"
                                       f"Energy transported: {energy:.2e} J")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
