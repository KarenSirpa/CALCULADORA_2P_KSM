import tkinter as tk
from tkinter import ttk, messagebox

# ✅ Importa tus módulos existentes
from cuadrados_medios1 import CuadradosMediosApp
from Productos_Medios2 import ProductosMediosApp
from Multiplicador_Constante3 import MultiplicadorConstanteApp
from prueba_kerland import PruebaKerlandApp
from exponencial import ExponencialApp
from generador_uniforme import GeneradorUniformeApp
from generador_gamma import GammaApp
from generador_normal import GeneradorNormalApp
from generador_weibull import GeneradorWeibullApp
from generador_uniforme2 import GeneradorUniforme2App
from generador_bernoulli import GeneradorBernoulliApp
from generador_binomial import GeneradorBinomialApp
from generador_poisson import GeneradorPoissonApp

class MenuCalculadorasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CALCULADORAS DE NUMEROS PSEUDOALEATORIOS")
        self.root.geometry("600x700")  # Ajustado para más botones
        self.root.configure(bg="white")  # Fondo blanco

        # Estilo personalizado
        style = ttk.Style()
        style.theme_use('clam')

        # Colores
        rosa = "#F8BBD0"       # Rosa suave (Material Pink 100)
        rosa_activo = "#F48FB1"  # Rosa más intenso al pasar el mouse
        blanco = "white"

        # Configurar estilos de botones
        style.configure("TButton", background=rosa, foreground="black", font=("Arial", 12, "bold"))
        style.map("TButton", background=[('active', rosa_activo)])

        # Título central
        title_label = tk.Label(
            self.root,
            text="CALCULADORAS DE NÚMEROS PSEUDOALEATORIOS",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="black"
        )
        title_label.pack(pady=20)

        # Frame para los botones
        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(expand=True, fill=tk.BOTH, padx=50, pady=10)

        # Lista de botones con sus textos y comandos
        botones = [
            ("1. Algoritmo de Cuadrados Medios", self.abrir_cuadrados_medios),
            ("2. Algoritmo de Productos Medios", self.abrir_productos_medios),
            ("3. Algoritmo de Multiplicador Constante", self.abrir_multiplicador_constante),
            ("4. Generador de Números Uniformes", self.abrir_generador_uniforme),
            ("5. Prueba Kerland - k*ERLANG", self.abrir_prueba_kerlan),
            ("6. Generador de Números Exponenciales", self.abrir_exponencial),
            ("7. Generador de Números Gamma", self.abrir_generador_gamma),
            ("8. Generador de Números Normales", self.abrir_generador_normal),
            ("9. Generador de Números Weibull", self.abrir_generador_weibull),
            ("10. Generador de Números Uniformes 2", self.abrir_generador_uniforme2),
            ("11. Generador de Números Bernoulli", self.abrir_generador_bernoulli),
            ("12. Generador de Números Binomial", self.abrir_generador_binomial),
            ("13. Generador de Números Poisson", self.abrir_generador_poisson),
        ]

        for texto, comando in botones:
            ttk.Button(
                button_frame,
                text=texto,
                command=comando,
                style="TButton"
            ).pack(pady=4, fill=tk.X, padx=20)

        # Botón Salir (con un poco más de espacio)
        ttk.Button(
            button_frame,
            text="❌ Salir",
            command=self.root.quit,
            style="TButton"
        ).pack(pady=(15, 5), fill=tk.X, padx=20)

    # Métodos para abrir ventanas (sin cambios en lógica)
    def abrir_cuadrados_medios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Cuadrados Medios")
        app = CuadradosMediosApp(ventana)

    def abrir_productos_medios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Productos Medios")
        app = ProductosMediosApp(ventana)

    def abrir_multiplicador_constante(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Algoritmo de Multiplicador Constante")
        app = MultiplicadorConstanteApp(ventana)

    def abrir_generador_uniforme(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Uniformes")
        app = GeneradorUniformeApp(ventana)

    def abrir_prueba_kerlan(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Prueba Kerlan - k*ERLANG")
        app = PruebaKerlandApp(ventana)

    def abrir_exponencial(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Exponenciales")
        app = ExponencialApp(ventana)

    def abrir_generador_gamma(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Gamma")
        app = GammaApp(ventana)

    def abrir_generador_normal(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Normales")
        app = GeneradorNormalApp(ventana)

    def abrir_generador_weibull(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Weibull")
        app = GeneradorWeibullApp(ventana)

    def abrir_generador_uniforme2(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Uniformes2")
        app = GeneradorUniforme2App(ventana)

    def abrir_generador_bernoulli(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Bernoulli")
        app = GeneradorBernoulliApp(ventana)

    def abrir_generador_binomial(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Binomial")
        app = GeneradorBinomialApp(ventana)

    def abrir_generador_poisson(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Generador de Números Poisson")
        app = GeneradorPoissonApp(ventana)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = MenuCalculadorasApp(root)
    root.mainloop()