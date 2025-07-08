# 🌦️ Monitor de Clima Automatizado

Este proyecto en Python permite consultar el clima actual de cualquier ciudad utilizando la API de OpenWeatherMap. Automatiza tareas como el envío de alertas por correo, el almacenamiento de reportes, la detección de condiciones climáticas críticas y la visualización de datos históricos en gráficas.

---

## 🚀 Funcionalidades principales

- ✅ Consulta de clima en tiempo real por ciudad.
- 📩 Envío automático de reportes por correo electrónico (con adjunto).
- 🔔 Detección de alertas meteorológicas personalizadas (ej. calor extremo, vientos fuertes, etc.).
- 📊 Registro y graficación histórica de temperaturas por ciudad.
- 🧹 Limpieza automática de reportes duplicados.
- 📅 Ejecución programada con el Programador de Tareas de Windows.

---

## 🧱 Estructura del proyecto

monitor_clima_proyecto/
│
├── clima_api.py # Módulo para consumir la API de clima
├── main.py # Script principal con menú de opciones
│
├── data/
│ └── historico_{ciudad}.csv # Históricos por ciudad
│
├── logs/
│ └── registro.txt # Registro de alertas
│
├── reportes/
│ └── reporte_{ciudad}_fecha.txt # Reportes generados
│
└── utils/
├── utils.py # Funciones auxiliares generales
├── utils_archivos.py # Manejo de archivos, reportes y CSV
├── alertas.py # Lógica para generar alertas
└── graficar_ciudad.py # Módulo de visualización de datos


---

## ⚙️ Requisitos

- Python 3.10+
- Librerías:
  - `requests`
  - `matplotlib`
  - `smtplib` (incluida por defecto)
  - `email` (incluida por defecto)
- Cuenta en [OpenWeatherMap](https://openweathermap.org/) y una API Key válida
- Cuenta en un proveedor SMTP (por ejemplo, [smtp2go](https://www.smtp2go.com/))

---

## 🧪 Cómo usar

1. **Configura tu API Key** en el archivo `clima_api.py`.
2. **Modifica los datos SMTP reales** en el `main.py` si deseas activar el envío de correos.
3. Ejecuta el script principal:

```bash
python main.py
