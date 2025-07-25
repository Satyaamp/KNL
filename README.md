# Knowledge Nook Library (KNL) Web Application

## Overview
Knowledge Nook Library (KNL) is a Django-based web application designed to manage library registrations, user accounts, and provide an interactive user interface for library services. The application includes user registration with validation, login/logout functionality, profile management, and an enhanced admin panel with a modern glassmorphism design.

## Features
- User registration with validation for unique contact number and Aadhaar number.
- Secure login and logout functionality.
- User profile page displaying registration details.
- Admin panel with custom glassmorphism style for improved UI/UX.
- Admin action to export selected registrations as PDF.
- Responsive navigation bar showing relevant links based on user authentication status.
- Static and media file handling for user photos and Aadhaar images.
- Custom authentication backend supporting login via phone number or Aadhaar number.

## Technologies Used
- Python 3.13
- Django 5.1.4
- SQLite (default database)
- ReportLab (for PDF export in admin)
- HTML, CSS (including custom glassmorphism CSS for admin)
- Git for version control

## Project Structure
- `one/` - Main Django project directory.
- `two/` - Django app handling core library functionalities.
- `templates/` - HTML templates for the web pages.
- `static/` - Static files including CSS, images, and custom admin styles.
- `media/` - Uploaded media files (user photos, Aadhaar images).
- `README.md` - This documentation file.

## Installation and Setup
1. Clone the repository:
   ```
   git clone https://github.com/Satyaamp/KNL.git
   cd KNL/one
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv myvenv
   myvenv\Scripts\activate  # Windows
   source myvenv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```
   python manage.py createsuperuser
   ```

6. Collect static files:
   ```
   python manage.py collectstatic
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the application at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin/`.

## Usage
- Register new users via the registration page.
- Login using contact number or Aadhaar number.
- Manage user profiles.
- Admins can manage registrations and export data as PDF.
- Admin panel features a modern glassmorphism UI for better experience.

## Customizations
- Glassmorphism style applied to Django admin panel via custom CSS (`static/admin_glassmorphism.css`).
- Registration form includes validation for unique contact and Aadhaar numbers.
- Navigation bar dynamically changes based on user authentication status.

## Deployment
- Ensure DEBUG is set to `False` in production.
- Configure allowed hosts in `settings.py`.
- Set up a production-ready database (e.g., PostgreSQL).
- Use a WSGI server like Gunicorn or uWSGI.
- Configure static and media file serving.
- Secure the application with HTTPS and proper security settings.

## Contributing
Contributions are welcome. Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact
For any queries or support, please contact the project maintainer.

---

Thank you for using Knowledge Nook Library!
