import customtkinter as ctk


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Amazon Product Download Manager")
        self.geometry("1200x800")
        self.minsize(1000, 700)

        self.create_widgets()

    def create_widgets(self):

        # ===== Title =====
        title = ctk.CTkLabel(
            self,
            text="Amazon Product Download Manager",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=(20, 10))

        # ===== Input Frame =====
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="both", padx=20, pady=10)

        label = ctk.CTkLabel(
            input_frame,
            text="Paste ASIN / UPC List",
            font=("Segoe UI", 18, "bold")
        )
        label.pack(anchor="w", padx=15, pady=(15, 10))

        self.textbox = ctk.CTkTextbox(
            input_frame,
            height=220,
            font=("Consolas", 15)
        )
        self.textbox.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # ===== Buttons =====
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20)

        self.start_btn = ctk.CTkButton(
            button_frame,
            text="▶ Start",
            width=140,
            command=self.start_clicked
        )

        self.pause_btn = ctk.CTkButton(
            button_frame,
            text="⏸ Pause",
            width=140,
            state="disabled"
        )

        self.stop_btn = ctk.CTkButton(
            button_frame,
            text="⏹ Stop",
            width=140,
            state="disabled"
        )

        self.start_btn.pack(side="left", padx=10, pady=15)
        self.pause_btn.pack(side="left", padx=10)
        self.stop_btn.pack(side="left", padx=10)

        # ===== Progress =====
        progress_frame = ctk.CTkFrame(self)
        progress_frame.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            progress_frame,
            text="Progress",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w", padx=15, pady=(15, 10))

        self.progress = ctk.CTkProgressBar(progress_frame)
        self.progress.pack(fill="x", padx=15)

        self.progress.set(0)

        self.status = ctk.CTkLabel(
            progress_frame,
            text="Waiting...",
            font=("Segoe UI", 15)
        )

        self.status.pack(anchor="w", padx=15, pady=(10, 15))

        # ===== Logs =====
        log_frame = ctk.CTkFrame(self)
        log_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        ctk.CTkLabel(
            log_frame,
            text="Logs",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w", padx=15, pady=(15, 10))

        self.logbox = ctk.CTkTextbox(
            log_frame,
            font=("Consolas", 13)
        )

        self.logbox.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.write_log("Amazon Product Download Manager started.")

    def write_log(self, text):
        self.logbox.insert("end", text + "\n")
        self.logbox.see("end")

    def start_clicked(self):

        codes = self.textbox.get("1.0", "end").strip().splitlines()

        codes = [c.strip() for c in codes if c.strip()]

        self.write_log(f"Loaded {len(codes)} products.")

        self.status.configure(
            text=f"{len(codes)} products ready."
        )

        self.progress.set(0)
