# LibraryProject

This is my first Django project created for the ALX Django Learn Lab.

## Setup Instructions
1. Install Django using `pip install django`
2. Create the project: `django-admin startproject LibraryProject`
3. Run the server: `python manage.py runserver`

## Project Structure
- **manage.py**: Django’s command-line utility for managing the project.
- **settings.py**: Contains all configurations for the Django project.
- **urls.py**: Maps URLs to views.
- **asgi.py / wsgi.py**: Entry points for ASGI/WSGI-compatible web servers.


# settings.py
# Security Best Practices Implemented:
# - DEBUG=False to prevent exposing sensitive info
# - SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF
#   protect against XSS and clickjacking
# - CSRF_COOKIE_SECURE & SESSION_COOKIE_SECURE for secure cookie transmission
# - HSTS headers force HTTPS
# - CSP headers prevent loading scripts/styles from untrusted sources
