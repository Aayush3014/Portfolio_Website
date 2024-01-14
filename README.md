## Portfolio Generator
This is a dynamic portfolio website built with Django that allows users to easily create and manage their own portfolio.

## Features

- Add projects - Users can add project details like title, description, skills used, etc.
- Add skills - Users can add their skills.
- Project list - Projects are displayed in a list on the homepage
- Project detail view - Click on a project to see a detailed view.
- Project Edit Feature - You can also edit the information of your particular project by using ```django-forms``` which are already implemented
- Skill list - Skills added by the user are displayed on a skills page
- Contact Feature - Anyone can send you messages and you can access them in inbox tab of you website
- Dynamic rendering - Projects and skills are rendered dynamically based on data in the database
- Voting System - Chart.js based voting system is also implemented for little interaction with the users.
- Payments - Integrated Razorpay for accepting payments (optional feature)


## Installation

- Fork the repository
- Clone the repository
- Create and activate a virtual environment -->   ```python3 -m venv <virtual_environment name>```
- Install requirements -->   ```pip install -r requirements.txt```
- Run migrations -->  ```python manage.py migrate```
- Create admin user -->  ```python manage.py createsuperuser```
- Run the server -->  ```python manage.py runserver```
- The app should now be running at http://127.0.0.1:8000/

## Built With
- Python - Language used
- Django - The web framework used
- Razorpay - Payment integration (optional)
- MySQL - Database used
