import customtkinter as ctk
import math

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 1.247", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="m (kg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    m_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 1")
    m_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="v_i (m/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    vi_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 10")
    vi_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="α_i (deg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    theta_i_entry = ctk.CTkEntry(frame3, placeholder_text="e.g., 60")
    theta_i_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame4, text="v_r (m/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    vr_entry = ctk.CTkEntry(frame4, placeholder_text="e.g., 6")
    vr_entry.grid(row=0, column=1, padx=5, pady=5)

    frame5 = ctk.CTkFrame(page, fg_color="transparent")
    frame5.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame5, text="α_r (deg):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    theta_r_entry = ctk.CTkEntry(frame5, placeholder_text="e.g., 45")
    theta_r_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            m = float(m_entry.get())
            vi = float(vi_entry.get())
            vr = float(vr_entry.get())
            theta_i = math.radians(float(theta_i_entry.get()))
            theta_r = math.radians(float(theta_r_entry.get()))


            px_i = vi * math.cos(theta_i)
            py_i = vi * math.sin(theta_i)
            px_r = vr * math.cos(theta_r)
            py_r = vr * math.sin(theta_r)

            delta_px = m * (px_r - px_i)
            delta_py = m * (py_r - py_i)
            impulse = math.sqrt(delta_px**2 + delta_py**2)

            KE_i = 0.5 * m * vi**2
            KE_r = 0.5 * m * vr**2
            energy_lost = KE_i - KE_r

            result_label.configure(
                text=f"Impulse on wall: {impulse:.2f} kg·m/s\n"
                     f"Energy lost as heat: {energy_lost:.2f} J"
            )
        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
