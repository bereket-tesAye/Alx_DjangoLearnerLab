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

"""
HTTPS and Secure Redirects Configuration

- SECURE_SSL_REDIRECT = True -> Redirects all HTTP traffic to HTTPS
- SECURE_HSTS_SECONDS = 31536000 -> Enforces HTTPS for 1 year via HSTS
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True -> Applies HSTS to all subdomains
- SECURE_HSTS_PRELOAD = True -> Allow browsers to preload site in HSTS list
- SESSION_COOKIE_SECURE = True -> Ensure session cookies only sent over HTTPS
- CSRF_COOKIE_SECURE = True -> Ensure CSRF cookies only sent over HTTPS
- X_FRAME_OPTIONS = 'DENY' -> Prevent clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF = True -> Prevent MIME sniffing
- SECURE_BROWSER_XSS_FILTER = True -> Enable XSS browser protection

Deployment:
- SSL/TLS certificates configured on web server (Nginx or Apache)
- HTTP to HTTPS redirect configured
- Proxy headers passed for secure connections
"""

