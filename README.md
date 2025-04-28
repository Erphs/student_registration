# Student Registration System

🎓 A full-stack student registration system built with Django, MySQL, and Bootstrap — combining powerful backend management with a responsive and modern frontend design.

---

## 📚 Project Description
This project allows you to:

- Register new students 📄
- Store their details in a MySQL database 🗄️
- Search, update, or delete records 🔍

The goal is to create a basic yet functional system for student registration using Django as the backend, MySQL as the database, and Bootstrap for a modern, responsive user interface.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Erphs/student_registration.git
cd student_registration
```

### 2. Install Requirements

You will need Python 3.7 or higher, along with the necessary libraries. Install them using pip:

```bash
pip install -r requirements.txt
```

Make sure MySQL is installed and running on your system.

### 3. Setup MySQL Database

Before running the project, you will need to create a database in MySQL. You can do this with the following SQL command:

```sql
CREATE DATABASE student_registration;
```

In your Django settings file (`settings.py`), update the database settings as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_registration',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 4. Run the Migrations

Run the following commands to create the necessary tables in MySQL:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Program

Finally, run the project with:

```bash
python manage.py runserver
```

You can now access the app at `http://127.0.0.1:8000/`.

---

## 🛠 How It Works (SQL Usage)

The system uses **MySQL** as its database backend.

- When you run the project, it will create the necessary tables in the `student_registration` database.
- The database will have a table named `students` with columns like `id`, `name`, `email`, etc.

Example SQL Table Creation:

```sql
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    course VARCHAR(255) NOT NULL
);
```

When you add a student, the system will execute an SQL `INSERT` like:

```sql
INSERT INTO students (name, email, course) VALUES (%s, %s, %s);
```

When you want to search, update, or delete, it uses standard SQL commands like `SELECT`, `UPDATE`, and `DELETE`.

---

## 📸 Preview

*(Optional: Add some screenshots or a demo GIF here!)*

---

## ✨ Features to Improve

- Adding GUI with Django Templates and Bootstrap 🖥️
- Export student list as CSV or PDF 📄
- Authentication system for admin access 🔒

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit improvements.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

Made with ❤️ by [Erphs](https://github.com/Erphs)
