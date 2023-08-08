# Rick and Morty Django Project

This is a Django web application that scrapes character data from the Rick and Morty API and displays it on the website.

## Installation and how to use it

1. Clone the repository to your local machine:

   git clone https://github.com/JGattringer/assync_multithread_django.git
   cd rick_morty_project

2. Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the project dependencies:

pip install -r requirements.txt

4. Run database migrations:

python manage.py migrate

5. Scrape and save character data:

python manage.py shell
exec(open('scrapper.py').read())

6. Run the development server:

python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to see the character data.

7. Usage

/: Homepage that displays character data.
/admin/: Django admin panel for managing character data.

8. Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request.

9. Credits

Django
Aiohttp
Rick and Morty API