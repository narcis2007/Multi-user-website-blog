Description:
------------------------------
A website made using Python Django Framework, HTML, CSS and Ajax  where users can log in and publish their own articles.
Each user has a profile which they can edit and can be viewed by other people, logged users can post
comments or add new articles, they can edit or delete them in their account section, when the action is completed they are informed with a suggestive message. 
The website comes with a notification system.
Everyone can register. If someone forgot their password they only have to enter their email adress and they will receive a link to a page where they can reset it.


How to install it
------------------------------
 
- Clone the code from git.
- Create an environment using [virtualenv](https://virtualenv.pypa.io/en/latest/) and activate it.
- Install the project dependencies with [pip](https://pip.pypa.io/en/latest/installing.html). Run this command: `pip install -r requirements.txt` while being in the folder with the `requirements.txt` file.
- Access mysql server using: `mysql -u root -p` and create the database: `CREATE DATABASE user_authentication;`
- Create the following `local_settings.py` file in the same folder as `settings.py`:
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'user_authentication',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': '',
    'PORT': ''
    }
}
DEBUG = True
```
- Run `python manage.py migrate` to create the tables.
- Run `python manage.py runserver` to actually run the application.
