# URL Shortener Django Projectf
Welcome to the URL Shortener Django Project repository! This project provides a web-based URL shortening service implemented using Django, allowing users to easily create and share shortened URLs.
## Requirements
To run this project, you'll need the following:
- Python 3.x
- Django 3.x
- Virtual environment (optional but recommended)
## Installation
Follow these steps to set up the project on your local machine:

1. Clone this repository to your preferred directory:
2. Navigate to the project directory:
   cd url-shortener-django
3. Create a virtual environment (optional but recommended):
   python3 -m venv venv
4. Activate the virtual environment:
   On Windows:
   venv\Scripts\activate
5. Install project dependencies:
   pip install -r requirements.txt
6. Set up the database:
   python manage.py migrate
7. Create a superuser to access the admin panel:
   python manage.py createsuperuser
   follow the prompts to create a username and password ie ADMIN password: amjunior
8. Run the development server:
   python manage.py runserver

The project should now be running at http://127.0.0.1:8000/. You can access the admin panel at http://127.0.0.1:8000/admin/ to manage URLs and monitor the system.

## Usage
- To create a shortened URL, visit the home page and enter the long URL in the provided input.
- To manage URLs and access the admin panel, use the credentials provided during the initial setup.

## Templates and Models
The project comes with pre-designed templates for a user-friendly interface. The templates are located in the `templates` directory and are ready to use out of the box.

The project's models define the data structure and relationships. The URL model, defined in the `shortener/models.py` file, stores information about original and shortened URLs.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests if you encounter bugs, want to add new features, or improve existing ones.

## License

This project is licensed under the MUST License - see the [LICENSE](MUST.URLSHORT) file for details.
Author by Angura Emmanuel 2021/BCS/019/PS
Happy URL Shortening!


     