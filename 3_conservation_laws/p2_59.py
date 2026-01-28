import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 2.59", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    

    ctk.CTkLabel(frame1, text="A (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    a_entry = ctk.CTkEntry(frame1, placeholder_text="10")
    a_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ctk.CTkLabel(frame1, text="B (m/s):", font=("Arial", 16)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    b_entry = ctk.CTkEntry(frame1, placeholder_text="-2")
    b_entry.grid(row=1, column=1, padx=5, pady=5)
    
    ctk.CTkLabel(frame1, text="C (m/s²):", font=("Arial", 16)).grid(row=2, column=0, sticky="w", padx=5, pady=5)
    c_entry = ctk.CTkEntry(frame1, placeholder_text="1")
    c_entry.grid(row=2, column=1, padx=5, pady=5)
    
    ctk.CTkLabel(frame1, text="D (m/s³):", font=("Arial", 16)).grid(row=3, column=0, sticky="w", padx=5, pady=5)
    d_entry = ctk.CTkEntry(frame1, placeholder_text="-0.2")
    d_entry.grid(row=3, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="t (s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    t_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 2")
    t_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)


    def calculate():
        try:
            A = float(a_entry.get())
            B = float(b_entry.get())
            C = float(c_entry.get())
            D = float(d_entry.get())
            t = float(t_entry.get())
            m = 2 

            # v = dx/dt = B + 2C t + 3D t^2
            v = B + 2*C*t + 3*D*t**2
            # a = dv/dt = 2C + 6D t
            a = 2*C + 6*D*t
            #  P = F * v = m * a * v
            P = m * a * v

            result_label.configure(text=f"Velocity: {v:.2f} m/s\n"
                                       f"Acceleration: {a:.2f} m/s²\n"
                                       f"Power: {P:.2f} W")
        except ValueError:
            result_label.configure(text="Invalid input!")


    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
