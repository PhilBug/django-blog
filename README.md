# django-blog

## General info

This is a simple blog app.  
It uses Django Framework for both frontend and backend as well as bootstrap for css styling.  
Posts can be added/deleted/edited via admin panel (localhost:8000/admin by default).  
All credentials are stored in a provided `.env` file.

## Project structure

- Blog is the main project app, defining settings and main url routing

- Pages app is reponsible for displaying main static pages: index (homepage), about, and contact_form

- Posts app mostly handles 'Post' model, defines db fields, and single post view

- Each app stores its template files inside templates folder, partials and base.html are used to reduce redundant frontend code.

Server uses managed postgresql instance.
SendGrid is an email API provider.

## Dependency installation

Create new python virtualenv.  
Run:

```bash
pip install -r requirements.txt

or

# (pip3 install pipenv)
pipenv install
```

## Starting the application

Ensure secrets inside `.env` file are correct.  
Run:

```bash
./manage.py runserver

# or (if using pipenv)

pipenv shell; ./manage.py runserver
```

## Checking received emails

Emails are sent to account defined by `ADMIN_EMAIL` environment variable (has to be enabled and whitelisted sendgrid api management panel).
Credentials to that account are provided in the `.env` file.
