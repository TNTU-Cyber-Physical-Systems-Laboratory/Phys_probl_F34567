import customtkinter as ctk

def create_page(parent):
    page = ctk.CTkFrame(parent)

    title = ctk.CTkLabel(page, text="Problem 4.184", font=("Arial", 20))
    title.pack(pady=10, anchor='w', padx=20)

    frame1 = ctk.CTkFrame(page, fg_color="transparent")
    frame1.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame1, text="v (m/s):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    v_entry = ctk.CTkEntry(frame1, placeholder_text="e.g., 340")
    v_entry.grid(row=0, column=1, padx=5, pady=5)

    frame2 = ctk.CTkFrame(page, fg_color="transparent")
    frame2.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame2, text="Frequency f (Hz):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    f_entry = ctk.CTkEntry(frame2, placeholder_text="e.g., 3400")
    f_entry.grid(row=0, column=1, padx=5, pady=5)

    frame3 = ctk.CTkFrame(page, fg_color="transparent")
    frame3.pack(pady=5, anchor='w', padx=20)
    ctk.CTkLabel(frame3, text="Reflection type(less\more):", font=("Arial", 16)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    reflection_entry = ctk.CTkEntry(frame3, placeholder_text="less or more dense")
    reflection_entry.grid(row=0, column=1, padx=5, pady=5)

    result_label = ctk.CTkLabel(page, text="", font=("Arial", 16))
    result_label.pack(pady=10, anchor='w', padx=20)

    def calculate():
        try:
            v = float(v_entry.get())
            f = float(f_entry.get())
            reflection = reflection_entry.get().strip().lower()

            wavelength = v / f

            if reflection == "less":
                node_dist = 0
                antinode_dist = wavelength / 4
                result_label.configure(
                    text=f"Wavelength λ = {wavelength:.4f} m\n"
                         f"Distance from boundary to first node: {node_dist:.4f} m\n"
                         f"Distance from boundary to first antinode: {antinode_dist:.4f} m"
                )
            elif reflection == "more":
                antinode_dist = 0
                node_dist = wavelength / 4
                result_label.configure(
                    text=f"Wavelength λ = {wavelength:.4f} m\n"
                         f"Distance from boundary to first antinode: {antinode_dist:.4f} m\n"
                         f"Distance from boundary to first node: {node_dist:.4f} m"
                )
            else:
                result_label.configure(text="Enter 'less' or 'more' for reflection type!")

        except ValueError:
            result_label.configure(text="Invalid input!")

    ctk.CTkButton(page, text="Calculate", command=calculate).pack(pady=20, anchor='w', padx=20)

    return page
