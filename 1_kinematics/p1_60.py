import customtkinter as ctk
import math


def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 1.60", font=("Arial", 20))
    title.pack(pady=10, anchor="w", padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame1, text="A (rad):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    A_entry = ctk.CTkEntry(frame1, placeholder_text="e.g. 10")
    A_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame2, text="B (1/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    B_entry = ctk.CTkEntry(frame2, placeholder_text="e.g. 0.1")
    B_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame3, text="R (m):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    r_entry = ctk.CTkEntry(frame3, placeholder_text="e.g. 0.1")
    r_entry.grid(row=0, column=1, padx=5, pady=5)

    frame4 = ctk.CTkFrame(page, fg_color="transparent")
    frame4.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame4, text="t (s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    t_entry = ctk.CTkEntry(frame4, placeholder_text="e.g. 10")
    t_entry.grid(row=0, column=1, padx=5, pady=5)

    result_at = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_an = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_a = ctk.CTkLabel(page, text="", font=("Arial", 16))

    result_at.pack(pady=5, anchor="w", padx=20)
    result_an.pack(pady=5, anchor="w", padx=20)
    result_a.pack(pady=5, anchor="w", padx=20)

    def calculate():
        try:
            A = float(A_entry.get())
            B = float(B_entry.get())
            r = float(r_entry.get())
            t = float(t_entry.get())

            omega = A * B * math.exp(B * t)
            epsilon = A * B**2 * math.exp(B * t)

            a_t = epsilon * r
            a_n = omega**2 * r
            a = math.sqrt(a_t**2 + a_n**2)

            result_at.configure(text=f"Tangential acceleration aτ = {a_t:.4f} m/s²")
            result_an.configure(text=f"Normal acceleration an = {a_n:.4f} m/s²")
            result_a.configure(text=f"Total acceleration a = {a:.4f} m/s²")

        except ValueError:
            result_at.configure(text="Invalid input")
            result_an.configure(text="")
            result_a.configure(text="")

    ctk.CTkButton(
        page,
        text="Calculate",
        command=calculate
    ).pack(pady=20, anchor="w", padx=20)

    return page
