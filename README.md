📘 studentSystem
A Django-based Student Information System for managing student records, admissions, grades, and more. Designed for ease of use and extensibility.

🚀 Features
🎓 Add, view, update, and delete student details

🗓 Track admission dates

📈 Store and retrieve student grades

⚠️ Handles invalid or duplicate entries with proper validation

🧪 Tested with exception handling and form validation

🛠 Tech Stack
Python 3.x

Django 5.x

SQLite (default) or any other supported DB

HTML/CSS (for templates)

📂 Project Structure
bash
Copy code
studentSystem/
├── manage.py
├── studentSystem/          # Django project settings
│   └── settings.py
├── students/               # Main student app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/students/
├── static/                 # CSS, JS, images
└── templates/              # Global templates
