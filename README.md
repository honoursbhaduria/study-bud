
# 📚 Study Bud

[![Made with Django](https://img.shields.io/badge/Made%20with-Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A simple and clean web-based chat application built to help students and study partners connect, collaborate, and study together.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Future Improvements](#future-improvements)

---

## 📖 About the Project

**Study Bud** was developed as a beginner project to practice web development skills and understand the basics of creating a system.  
It allows users to register, login, and send simple messages to one another.

---

## ✨ Features

- 🔐 User Registration and Login
- 💬 One-on-One Chatting
- 🖥️ Simple, Responsive UI
- 🗂️ Organized code structure for easy learning and extension

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite (default Django database)
- **Hosting**: (Localhost for development)

---

## 🚀 Getting Started

Follow these instructions to set up **Study Bud** locally:

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the Repository**
   ```bash
   git clone https:https://github.com/honoursbhaduria/study-bud.git
   cd study-bud
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

---

## 🔮 Future Improvements

- Add group chats and channels
- Real-time messaging with WebSockets
- Profile customization (profile pictures, status)
- Notification system for new messages
- Improved mobile responsiveness

---

 🚀 Happy Chatting with Study Bud!

