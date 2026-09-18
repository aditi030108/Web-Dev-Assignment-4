# Web Application Development II – Assignment 4
## IRCTC Railway Reservation System

**Author:** Aditi  
**Repository:** [https://github.com/aditi030108/Web-Dev-Assignment-4.git](https://github.com/aditi030108/Web-Dev-Assignment-4.git)

---

### Overview
This project is a Django-based simulation of an IRCTC railway reservation portal developed for Web Application Development II (Assignment 4). The objective of the assignment is to demonstrate:
- Django project and application setup (`irctc_portal` project, `booking` app)
- URL routing and view controllers
- Project-level template inheritance (`templates/base.html`)
- Passing and rendering in-memory dynamic data in templates without using database models or external CSS

### Project Layout
```text
irctc_portal/
├── manage.py
├── irctc_portal/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── booking/
│   ├── views.py
│   ├── urls.py
│   └── tests.py
└── templates/
    ├── base.html
    ├── home.html
    ├── trains.html
    ├── passenger.html
    └── confirmation.html
```

### Application Routes
- **`/` (Home):** Displays a welcome message along with featured train details passed from the view context.
- **`/trains/` (Train Search):** Lists available train schedules and details from a list of dictionaries.
- **`/passenger/` (Passenger Details):** Renders the passenger profile (Name, Age, Gender, Coach, Berth).
- **`/confirmation/` (Booking Confirmation):** Displays the confirmed ticket details including passenger name and booked train.

### How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/aditi030108/Web-Dev-Assignment-4.git
   cd Web-Dev-Assignment-4
   ```

2. Set up virtual environment and install Django:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install django
   ```

3. Navigate to the Django project folder and run server:
   ```bash
   cd irctc_portal
   python3 manage.py runserver
   ```

4. View the pages in your browser:
   - Home: `http://127.0.0.1:8000/`
   - Available Trains: `http://127.0.0.1:8000/trains/`
   - Passenger Details: `http://127.0.0.1:8000/passenger/`
   - Booking Confirmation: `http://127.0.0.1:8000/confirmation/`

### Running Tests
To run the automated tests:
```bash
python3 manage.py test
```

