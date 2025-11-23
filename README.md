# 🌐 Examen Final – Programación Web con Flask

**Repositorio remoto:** [https://github.com/jonathanmaker/examen-flask-entrega.git](https://github.com/jonathanmaker/examen-flask-entrega.git)

---

<p align="center">
  <img src="https://img.shields.io/badge/Proyecto-Flask-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Estado-Funcional-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Lenguaje-Python%203.x-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Licencia-Estudiantil-lightgrey?style=for-the-badge" />
</p>

---




---

## 📘 Descripción General

Este proyecto corresponde al **examen final de la asignatura Programación Web**, utilizando **Python + Flask** como base tecnológica.

La aplicación incluye:

* Un menú principal para navegar entre ejercicios.
* **Ejercicio 1:** Cálculo de descuentos en la compra de tarros de pintura.
* **Ejercicio 2:** Inicio de sesión con validación de usuarios.
* Templates HTML creados con Jinja2.
* Estilos CSS personalizados.
* Arquitectura limpia y ordenada.

La aplicación es totalmente funcional y está lista para ser ejecutada, evaluada y desplegada.

---

## 📁 Estructura del Proyecto

```
.
├── main.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
│
└── static/
    └── css/
        └── styles.css
```

---

## 🚀 Instalación y Ejecución

### 🔧 1. Clonar el repositorio

```bash
git clone https://github.com/jonathanmaker/examen-flask-entrega.git
cd examen-flask-entrega
```

### 🐍 2. Crear entorno virtual (opcional)

```bash
python -m venv venv
```

**Activación:**

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 📦 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### ▶️ 4. Ejecutar la aplicación

```bash
python main.py
```

La aplicación quedará disponible en:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📝 Detalle de los Ejercicios

### ✔️ Ejercicio 1 — Descuento en Tarros de Pintura

El formulario solicita:

* Nombre
* Edad
* Tarros de pintura

**Reglas de negocio:**

| Edad        | Descuento |
| ----------- | --------- |
| Menor de 18 | 0%        |
| 18 a 30     | 15%       |
| Mayor de 30 | 25%       |

Valor por tarro: **$9.000**.

Se despliega:

* Total sin descuento
* Total con descuento
* Porcentaje aplicado

---

### ✔️ Ejercicio 2 — Sistema de Login

El sistema tiene usuarios predefinidos:

| Usuario | Contraseña | Rol           |
| ------- | ---------- | ------------- |
| juan    | admin      | Administrador |
| pepe    | user       | Usuario       |

Si las credenciales no coinciden → "Usuario o contraseña incorrectos".

---

## 🎨 Estilos (CSS)

El archivo `styles.css` incluye:

* Tipografías generales
* Tarjetas de resultados
* Botones con hover
* Formularios estilizados
* Diseño centrado y limpio

---

## 📸 Capturas de Pantalla

*(Se agregan en Word u otro documento de entrega)*

Recomendaciones:

* Menú principal
* Ejercicio 1: formulario
* Ejercicio 1: resultado con 0%, 15% y 25%
* Ejercicio 2: login correcto e incorrecto

---

## 🧠 Tecnologías Utilizadas

* Python 3.x
* Flask
* HTML5
* CSS3
* Jinja2
* Git & GitHub
* Visual Studio Code

---

## 📌 To-Do / Mejoras Futuras

* [ ] Agregar base de datos con SQLite
* [ ] Crear sistema de registro de usuarios
* [ ] Validaciones adicionales con WTForms
* [ ] Implementar pruebas unitarias
* [ ] Crear versión Docker
* [ ] Añadir componentes dinámicos con JavaScript

---

## 👨‍💻 Autor

**Jonathan Peña**
GitHub: [https://github.com/jonathanmaker](https://github.com/jonathanmaker)

---

## 🏁 Estado del Proyecto

**✔️ Proyecto finalizado y aprobado para entrega.**

---

<p align="center">
  <strong>¡Gracias por visitar este proyecto! 👋</strong>
</p>
