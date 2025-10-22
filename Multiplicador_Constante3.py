import tkinter as tk
from tkinter import ttk, messagebox

class MultiplicadorConstanteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo de Multiplicador Constante")
        self.root.geometry("900x700")
        self.root.configure(bg="#FFFFFF")  # Fondo blanco

        # Estilo personalizado
        style = ttk.Style()
        style.theme_use('clam')

        # Colores
        blanco = "#FFFFFF"
        rosa = "#F8BBD0"          # Rosa suave
        rosa_oscuro = "#F48FB1"   # Rosa más intenso para hover
        negro = "#000000"

        # Configurar estilos
        style.configure("TButton", background=rosa, foreground=negro, font=("Arial", 10, "bold"), borderwidth=1)
        style.map("TButton", background=[('active', rosa_oscuro)], foreground=[('active', negro)])

        style.configure("Treeview", background=blanco, foreground=negro, fieldbackground=blanco, font=("Courier New", 9))
        style.configure("Treeview.Heading", background=rosa, foreground=negro, font=("Arial", 10, "bold"))
        style.map("Treeview.Heading", background=[('active', rosa_oscuro)])

        # Variables
        self.constante_var = tk.StringVar()
        self.semilla_var = tk.StringVar()
        self.iteraciones_var = tk.StringVar()

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Título central
        title_label = tk.Label(
            self.root,
            text="Algoritmo de Multiplicador Constante",
            font=("Arial", 16, "bold"),
            bg="#FFFFFF",
            fg="#000000"
        )
        title_label.pack(pady=15)

        # Frame para entradas
        input_frame = tk.Frame(self.root, bg="#FFFFFF")
        input_frame.pack(pady=10, padx=20)

        # Etiqueta y entrada para constante
        tk.Label(
            input_frame,
            text="Constante (a):",
            font=("Arial", 11),
            bg="#FFFFFF",
            fg="#000000"
        ).grid(row=0, column=0, sticky="w", padx=10, pady=5)

        constante_entry = tk.Entry(
            input_frame,
            textvariable=self.constante_var,
            width=20,
            font=("Arial", 10),
            relief="solid",
            bd=2,
            bg="white",
            fg="black"
        )
        constante_entry.grid(row=0, column=1, padx=10, pady=5)

        # Etiqueta y entrada para semilla
        tk.Label(
            input_frame,
            text="Y_0 (Semilla):",
            font=("Arial", 11),
            bg="#FFFFFF",
            fg="#000000"
        ).grid(row=1, column=0, sticky="w", padx=10, pady=5)

        semilla_entry = tk.Entry(
            input_frame,
            textvariable=self.semilla_var,
            width=20,
            font=("Arial", 10),
            relief="solid",
            bd=2,
            bg="white",
            fg="black"
        )
        semilla_entry.grid(row=1, column=1, padx=10, pady=5)

        # Etiqueta y entrada para iteraciones
        tk.Label(
            input_frame,
            text="Número de Iteraciones (n):",
            font=("Arial", 11),
            bg="#FFFFFF",
            fg="#000000"
        ).grid(row=2, column=0, sticky="w", padx=10, pady=5)

        iteraciones_entry = tk.Entry(
            input_frame,
            textvariable=self.iteraciones_var,
            width=20,
            font=("Arial", 10),
            relief="solid",
            bd=2,
            bg="white",
            fg="black"
        )
        iteraciones_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botones inferiores
        button_frame = tk.Frame(self.root, bg="#FFFFFF")
        button_frame.pack(pady=15)

        ttk.Button(button_frame, text="🚀 Generar", command=self.generar_numeros).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🧹 Limpiar", command=self.limpiar_tabla).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="❌ Salir", command=self.root.quit).pack(side=tk.LEFT, padx=5)

        # Tabla con Treeview
        self.tree = ttk.Treeview(
            self.root,
            columns=("N", "a", "Y_i", "Producto", "X_{i+1}", "R_i"),
            show="headings",
            height=15
        )

        # Definir encabezados
        self.tree.heading("N", text="N")
        self.tree.heading("a", text="a")
        self.tree.heading("Y_i", text="Y_i")
        self.tree.heading("Producto", text="Producto")
        self.tree.heading("X_{i+1}", text="X_{i+1}")
        self.tree.heading("R_i", text="R_i")

        # Ajustar anchos
        self.tree.column("N", width=40, anchor="center")
        self.tree.column("a", width=60, anchor="center")
        self.tree.column("Y_i", width=80, anchor="center")
        self.tree.column("Producto", width=120, anchor="center")
        self.tree.column("X_{i+1}", width=80, anchor="center")
        self.tree.column("R_i", width=80, anchor="center")

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar tabla y scrollbar
        self.tree.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def generar_numeros(self):
        try:
            a = int(self.constante_var.get())
            semilla = int(self.semilla_var.get())
            n = int(self.iteraciones_var.get())

            if a <= 0 or semilla <= 0 or n <= 0:
                raise ValueError("La constante, semilla y iteraciones deben ser números positivos.")

            # Limpiar tabla
            for item in self.tree.get_children():
                self.tree.delete(item)

            y = semilla
            for i in range(n):
                producto = a * y
                str_producto = str(producto)

                while len(str_producto) < 8:
                    str_producto = '0' + str_producto

                medio = len(str_producto) // 2
                x_str = str_producto[medio - 2:medio + 2]
                x_num = int(x_str)
                r = x_num / 10000.0

                self.tree.insert("", tk.END, values=(
                    i + 1,
                    a,
                    y,
                    str_producto,
                    x_num,
                    f"{r:.4f}"
                ))

                y = x_num

        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def limpiar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiplicadorConstanteApp(root)
    root.mainloop()