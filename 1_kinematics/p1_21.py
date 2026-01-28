import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 1.21", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="V0 (m/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    v0_entry = ctk.CTkEntry(frame1, placeholder_text="Enter initial speed")
    v0_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="h (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    h_entry = ctk.CTkEntry(frame2, placeholder_text="Enter height")
    h_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="Δt (s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    dt_entry = ctk.CTkEntry(frame3, placeholder_text="Enter time interval")
    dt_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            V0 = float(v0_entry.get())
            h = float(h_entry.get())
            dt = float(dt_entry.get())
            g = 2 * h / ( (dt/2)**2 )
            result_label.configure(text=f"Acceleration: {g:.3f} m/s²")
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
