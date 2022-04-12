# Store Administration

Store purchase management system. Total management of products and categories.

## Quickstart

First of all, clone this repo.

``
git clone https://github.com/DD21S/crud-categories-products.git
``

Then, in the project directory, you install the requirements.

``
pip install -r requirements.txt
``

Now, make the migrations.

``
python3 manage.py migrate
``

And finally, run the project.

``
python3 manage.py runserver
``

Ready, now your administration system is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create one with this command:

``
python3 -m venv venv
``

## About this project

This project is developed with the Django web framework. Among other things, class-based views were used. Also, tests for forms, views, models and urls which allows a more stable and consistent development and expansion of the application. It has two CRUD to manage products and categories.

### Notes

This project is not ready to be deployed on a web server. Rather, it's made to be run on a local server. Feel free to make any necessary modifications to deploy it.  