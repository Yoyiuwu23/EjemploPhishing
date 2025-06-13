# EjemploPhishing

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green?logo=qt)](https://riverbankcomputing.com/software/pyqt/intro)
[![Dotenv](https://img.shields.io/badge/python--dotenv-.env-important?logo=python)](https://pypi.org/project/python-dotenv/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

---

## 📧 ¿Qué es EjemploPhishing?

**EjemploPhishing** es una aplicación educativa desarrollada en Python que simula el envío de correos electrónicos personalizados usando plantillas HTML y una interfaz gráfica moderna con PyQt5.  
Su objetivo es **concientizar y enseñar sobre los riesgos del phishing** y cómo los atacantes pueden crear correos falsos convincentes.

---

## 🚨 ¿Por qué es importante aprender sobre phishing? :warning:

El **phishing** es una de las amenazas más comunes en ciberseguridad. Consiste en engañar a las personas para que revelen información confidencial (contraseñas, datos bancarios, etc.) mediante correos electrónicos o sitios web falsos que imitan a los legítimos.

> **Saber identificar y entender cómo funcionan estos ataques es fundamental para protegerse y proteger a los demás.**

- El phishing puede afectar tanto a usuarios individuales como a empresas.
- Los atacantes usan técnicas cada vez más sofisticadas, incluyendo plantillas HTML y suplantación de identidad.
- Aprender a reconocer señales de phishing ayuda a prevenir fraudes y pérdidas de datos.

---

## 🛠️ Tecnologías usadas

- [![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)  
  Lenguaje principal del proyecto.

- [![PyQt5](https://img.shields.io/badge/PyQt5-GUI-green?logo=qt)](https://riverbankcomputing.com/software/pyqt/intro)  
  Framework para la interfaz gráfica.

- [![Dotenv](https://img.shields.io/badge/python--dotenv-.env-important?logo=python)](https://pypi.org/project/python-dotenv/)  
  Manejo seguro de variables de entorno y credenciales.

- [![GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)  
  Licencia de software libre GNU General Public License v3.0.

---

## 🚀 ¿Cómo ejecutar el proyecto?

1. **Clona el repositorio:**

```

git clone https://github.com/Yoyiuwu23/EjemploPhishing.git
cd EjemploPhishing

```

2. **Crea y activa un entorno virtual:**

```

python -m venv venv
source venv/bin/activate

```

3. **Instala las dependencias:**

```

pip install -r requeriments.txt

```

4. **Configura tu archivo `.env`** (no lo subas a GitHub):

```

EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_contraseña_de_aplicacion
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

```

5. **Ejecuta la aplicación:**

```

python main.py

```

---

---


## 🔧 Problemas Comunes y Soluciones

### 1. Error al activar el entorno virtual
**Síntoma:**  
El entorno virtual parece activado (`(venv)` en el prompt), pero `pip` o `python` apuntan al sistema.

**Solución:**  
Verifica la activación correcta:
```

which pip  \# Debe mostrar: .../EjemploPhishing/venv/bin/pip

```
Si no está activo:
```

source venv/bin/activate

```

### 2. Error con PyQt5: "Could not load the Qt platform plugin 'xcb'"
**Síntoma:**  
La aplicación falla al iniciar con mensajes relacionados con el plugin gráfico.

**Solución:**  
Instala las dependencias gráficas en Ubuntu:
```

sudo apt install libxcb-xinerama0 libxcb-cursor0 libxcb1 libx11-6 libxext6 libxrandr2

```

### 3. Autenticación rechazada por Gmail (error 535)
**Síntoma:**  
"No se pudo enviar el correo: (535, b'5.7.8 Username and Password not accepted')".

**Solución:**  
Genera una **contraseña de aplicación** en tu cuenta de Google:  
[https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)  
Usa esa contraseña en el archivo `.env`, no tu contraseña normal.
``

---
## 📚 Recursos útiles

- [Más sobre phishing (Wikipedia)](https://es.wikipedia.org/wiki/Phishing)
- [python-dotenv (manejo de variables de entorno)](https://pypi.org/project/python-dotenv/)
- [PyQt5 (interfaz gráfica)](https://riverbankcomputing.com/software/pyqt/intro)
- [Shields.io (badges para README)](https://shields.io/)
- [Licencia GPLv3 (GNU)](https://www.gnu.org/licenses/gpl-3.0.html)

---

## ⚠️ Aviso ético

Este proyecto es **solo para fines educativos y de concientización**.  
No uses este software para actividades maliciosas o ilegales.

---

## 📩 Contacto

¿Dudas, sugerencias o quieres aportar?  
[![Email](https://img.shields.io/badge/email-rodrigosanzana2000@gmail.com-blue?logo=gmail)](mailto:rodrigosanzana2000@gmail.com)
