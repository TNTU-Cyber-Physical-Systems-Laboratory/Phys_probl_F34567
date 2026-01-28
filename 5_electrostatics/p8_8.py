import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)


    title = ctk.CTkLabel(page, text="Problem 8.8", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)


    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="m (g):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    m_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 0.1")
    m_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="l (cm):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    l_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 20")
    l_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="α (deg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    theta_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 30")
    theta_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            m = float(m_entry.get()) / 1000 
            l = float(l_entry.get()) / 100  
            alpha = float(theta_entry.get())
            g = 9.81
            alpha_rad = math.radians(alpha)

            k = 9e9  
            q = math.sqrt((m * g * l**2 * math.tan(alpha_rad)**3) / k)

            result_label.configure(text=f"Required charge on each ball: {q:.6e} C")
        except ValueError:
            result_label.configure(text="Invalid input!")
            
    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
