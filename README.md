# Technophilia

## Tips to navigate through the directory
1. Database configuration in astraverseproject/settings.py
2. Images, CSS can be found in static folder of root directory
3. pages folder contains the templates, models, views etc.
4. views.py has the business logic with rendering templates
5. accounts has the User(Donor) Schema
6. admin panel can be found in /admin route.

## Running the project

### if running for the first time (or) made changes to models
- <i>python manage.py makemigrations</i><br />
- <i>python manage.py migrate</i><br />

### to run the project
- <i>python manage.py runserver</i><br />

### creating superuser
- <i>python manage.py createsuperuser</i>


