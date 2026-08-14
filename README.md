# 🛍️ ShopSphere — Modern E-Commerce Web Application

[![Django](https://img.shields.io/badge/Django-6.0.7-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Live Demo](https://img.shields.io/badge/Live-Demo_on_Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)](https://shop-spher.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

> **ShopSphere** is a full-featured, responsive e-commerce web application built using **Django** and **Vanilla CSS**. It provides a complete shopping experience with real-time product filtering, category browsing, cart management, user authentication, and admin controls.

---

## 🌐 Live Application

🔗 **Live URL:** [https://shop-spher.onrender.com](https://shop-spher.onrender.com)

---

## ✨ Features

- 🛒 **Product Catalog & Details**: Browse products by category, view trending items, exclusive offers, and detailed specifications.
- 🔍 **Search & Category Filter**: Real-time filtering by categories (Laptops, Clothes, Phones, Sports, Perfumes, Skincare) and search queries.
- 🛍️ **Cart System**: Add to cart, dynamic badge count, quantity increment/decrement, real-time total price calculation, and item removal.
- 🔐 **User Authentication**: User Registration, Login, Logout, Profile Management, and Password Reset.
- 📱 **Fully Responsive UI**: Mobile-first layout with smooth animated hamburger navigation, clean responsive cards, and modern footer.
- 🛡️ **Django Admin Integration**: Full CRUD capabilities for products, categories, stock, and user accounts.
- ⚡ **Production Ready**: Configured with Gunicorn, WhiteNoise for static asset compression, and media serving.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 6.0.7, Python 3.12 |
| **Frontend** | HTML5, Vanilla CSS3 (Custom Design System, Inter Typography) |
| **Database** | SQLite3 / PostgreSQL compatible |
| **Server / WSGI** | Gunicorn |
| **Static & Media** | WhiteNoise, Django Static & Media Handler |
| **Deployment** | Render Web Service |

---

## 📁 Project Structure

```text
ShopSphere/
├── myproject/
│   ├── manage.py                  # Django CLI management script
│   ├── requirements.txt           # Production dependencies
│   ├── Procfile                   # Server process definition
│   ├── create_admin.py            # Automatic superuser bootstrap script
│   ├── base/                      # Core store app (products, cart, home)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/             # home, cart, product, about, help
│   ├── user_auth/                 # Authentication app (login, profile, register)
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/             # login, register, profile, forgot
│   ├── static/                    # Global CSS stylesheets and assets
│   │   └── css/style.css
│   ├── templates/                 # Base layout templates (main, nav, footer)
│   │   ├── main.html
│   │   ├── nav.html
│   │   └── footer.html
│   └── myproject/                 # Main Django project configuration
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── README.md
```

---

## 🚀 Quick Start (Local Setup)

### 1. Clone the repository
```bash
git clone https://github.com/Dibya-Ranjan-18/Shop-Spher.git
cd Shop-Spher/myproject
```

### 2. Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. Create superuser
```bash
python manage.py createsuperuser
```

### 6. Start development server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

---

## 👨‍💻 Author

**Dibya Ranjan Das**
- GitHub: [@Dibya-Ranjan-18](https://github.com/Dibya-Ranjan-18)
- Project: [ShopSphere](https://github.com/Dibya-Ranjan-18/Shop-Spher)

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).
