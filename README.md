
# Django Poll App

## Introduction

This is a simple Poll application built with Django. It allows users to create polls, vote on them, and view the results.

## Features

- Create new polls
- Add questions and choices to polls
- Vote on polls
- View poll results

## Prerequisites

- Python 3.x
- Django 3.x or higher
- SQLite (default for Django, but you can use any other database)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/django-poll-app.git
   cd django-poll-app
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/admin` to log in as the admin and start creating polls.

## Usage

### Creating a Poll

1. Log in to the admin site.
2. Add a new poll by providing the question and the choices.
3. Save the poll.

### Voting on a Poll

1. Visit the homepage.
2. Select a poll and vote for one of the choices.

### Viewing Poll Results

1. After voting, you can see the results of the poll on the same page.

## Project Structure

```
django-poll-app/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── polls/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   └── polls/
│   │       ├── detail.html
│   │       ├── index.html
│   │       └── results.html
│   └── migrations/
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The Django Project for the awesome framework.
- The Django documentation and tutorials for guidance.

