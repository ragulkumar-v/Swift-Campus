# Swift Campus 🚀

**Swift Campus** is a centralized complaint management system designed for college and university campuses. It streamlines the reporting and resolution of operational issues like IT outages, infrastructure problems, classroom malfunctions, and more — ensuring smooth communication between students, faculty, and administrative staff.

Swift Campus enhances accountability, transparency, and efficiency across educational institutions.

---

## 🔍 Features

- 📌 **Issue Reporting**: Report campus-related issues by selecting category and location.
- 📅 **Tracking System**: Real-time status updates on complaint progress.
- 🧑‍💼 **Role-based Dashboards**: Distinct views for Students, Faculty, Admins, and Technicians.
- 📨 **Email Notifications**: Automated updates and resolution confirmations.
- 📊 **Analytics**: Visual representation of reported issues by type, priority, and status.
- 🔒 **Authentication & Authorization**: Secure login for different roles.

---

## 🏛️ Target Users

- Students  
- Faculty Members  
- Administrative Staff  
- Campus Maintenance Teams  

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Django (Python)  
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)  
- **Version Control**: Git & GitHub  


---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/swift-campus.git
cd swift-campus
```
### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install Django
python -m pip install Pillow
```
### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```
### 6. Run the development server
```bash
python manage.py runserver
```
Open your browser and go to ```bash http://127.0.0.1:8000/ ```.

### 📁 Project Structure
```bash
swift-campus/
├── complaints/           # Django app for managing complaints
├── users/                # Authentication and user roles
├── templates/            # HTML templates
├── static/               # CSS, JS, and image files
├── media/                # Uploaded images
├── manage.py
└── db.sqlite3
```
### 📌 Roadmap
 Basic complaint reporting

 Admin panel for managing issues

 Technician workflow integration

 Push notifications (future)

 Mobile app support (future)

 Role-specific analytics dashboard (future)

### License
This project is licensed under the MIT License — see the LICENSE file for details.

# cygnus-campus-complaint-app
 web portal for students to register their complaints about any matter in the campus
![](working.gif)
