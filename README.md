# Internship Finder

## Installation

1. Migrate the database
```bash
python manage.py migrate
```

2. Run auth_groups fixture.
```bash
python manage.py loaddata auth_groups.json
```

3. Creating an admin user
```bash
python manage.py createsuperuser
```

4. Run the application
```bash
python manage.py runserver
```