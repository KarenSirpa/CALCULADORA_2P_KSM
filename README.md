# CALCULADORA_2P_KSM
Karen Sirpa Calculadora segundo parcial
Generadores de Distribuciones Estadísticas y Herramientas de Cálculo
Este repositorio contiene una colección de scripts en Python para generar muestras aleatorias de distribuciones de probabilidad comunes, junto con herramientas auxiliares para cálculos y pruebas estadísticas.
Incluye soporte especial para la distribución Weibull, como solicitado.
Estructura del Proyecto
uncionalidades
Generación de variables aleatorias: Normal, Exponencial, Binomial, Poisson, Uniforme, Gamma, Weibull, Bernoulli.
Métodos clásicos de generación: Cuadrados Medios, Productos Medios.
Menú interactivo para navegación fácil.
Prueba de bondad de ajuste (Kolmogorov-Smirnov).
Soporte especial para Weibull (parámetros de forma y escala configurables).
otas Finales
El archivo prueba_kerland.py parece referirse a la prueba de Kolmogorov-Smirnov; considera renombrarlo para mayor claridad.
Todos los generadores usan métodos basados en transformación inversa o algoritmos clásicos (ej: método de aceptación-rechazo para Poisson/Gamma).



Simulaciones, Juegos de la Vida y Generadores Aleatorios
Este repositorio contiene una colección de scripts en Python enfocados en simulaciones estocásticas, juegos de la vida (1D y 2D) y generación de números aleatorios. Ideal para estudiantes, entusiastas de la simulación o quienes quieran explorar modelos dinámicos y sistemas complejos.
Funcionalidades
 Simulación de propagación de enfermedades (COVID-19 simple).
 Juego de la Vida 1D y 2D — implementación desde cero usando reglas celulares.
 Generadores aleatorios personalizados — incluyendo métodos como congruencial lineal, cuadrados medios, etc.
 Aplicación interactiva (distribuciones_app.py y simulaciones_app.py) para ejecutar y visualizar resultados.
 Notas Finales
Los juegos de la vida están implementados sin dependencias externas, solo con numpy y matplotlib.
La simulación de COVID es simplificada, ideal para entender modelos SIR básicos.
distribuciones_app.py puede usarse como base para construir interfaces gráficas más complejas con tkinter.
