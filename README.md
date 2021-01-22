# django-blog

## Dependency installation

Create new python virtualenv.  
Run:

```bash
pip install -r requirements.txt
```

```bash
./manage.py collectstatic
```

```bash
./manage.py makemigrations && ./manage.py migrate
```

## Starting the application

Ensure secrets inside `.env` file are correct.  
Run:

```bash
./manage.py runserver
```
