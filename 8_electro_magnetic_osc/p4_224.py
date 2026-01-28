import customtkinter as ctk
import math


def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 4.224", font=("Arial", 20))
    title.pack(pady=10, anchor="w", padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame1, text="U₀ (V):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5)
    U_entry = ctk.CTkEntry(frame1, placeholder_text="25")
    U_entry.grid(row=0, column=1, padx=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame2, text="ω (rad/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5)
    omega_entry = ctk.CTkEntry(frame2, placeholder_text="1000·π")
    omega_entry.grid(row=0, column=1, padx=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor="w", padx=20)
    ctk.CTkLabel(frame3, text="C (μF):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5)
    C_entry = ctk.CTkEntry(frame3, placeholder_text="1")
    C_entry.grid(row=0, column=1, padx=5)

    result_L = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_I = ctk.CTkLabel(page, text="", font=("Arial", 16))

    result_L.pack(pady=5, anchor="w", padx=20)
    result_I.pack(pady=5, anchor="w", padx=20)

    def calculate():
        try:
            U0 = float(U_entry.get())
            omega = float(omega_entry.get())
            C = float(C_entry.get()) * 1e-6

            L = 1 / (omega**2 * C)
            I0 = omega * C * U0

            result_L.configure(
                text=f"Inductance: L = {L:.6e} H"
            )
            result_I.configure(
                text=f"I(t) = {I0:.6e} · sin({omega:.2f} t) A"
            )

        except ValueError:
            result_L.configure(text="Invalid input")
            result_I.configure(text="")

    ctk.CTkButton(
        page,
        text="Calculate",
        command=calculate
    ).pack(pady=20, anchor="w", padx=20)

    return page
