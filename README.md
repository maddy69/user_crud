# Django User CRUD App

A simple Django web application for performing CRUD operations on user data.

## Table of Contents
- Features
- Installation
- Usage
- Folder Structure
- Contributing
- License

## Features

- Create, Read, Update, and Delete (CRUD) operations on user data.
- User-friendly web interface.
- Bootstrap for basic styling.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/django-user-crud.git
   ```

2. Navigate to the project directory:

   ```bash
   cd django-user-crud
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for accessing the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Access the application at http://127.0.0.1:8000/

## Usage

1. Create a superuser account to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Provide the required information.

2. Run the development server:

   ```bash
   python manage.py runserver
   ```

   Access the application at http://127.0.0.1:8000/

3. Use the Django admin panel to manage users:

   ```bash
   http://127.0.0.1:8000/admin/
   ```

   Use the superuser credentials created earlier.

4. Perform CRUD operations on users using the web interface:

   ```bash
   http://127.0.0.1:8000/users/
   ```

## Folder Structure

- user_crud/: Project-level configuration and settings.
- users/: App containing models, views, templates, and static files.
- templates/: HTML templates for rendering pages.
- static/: Static files such as CSS stylesheets.
