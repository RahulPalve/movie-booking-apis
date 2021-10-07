# movie-booking-apis

## Setup Instructions
- `docker-compose up` for quickly setting up db, Or setup manually
- create a `virtualenv`, activate it
- `pip install -r requirements.py`
- `python manage.py migrate`
- python manage.py runserver`
- API Documentation can be found at `/api/docs` endpoint -> http://localhost:8000/api/docs/.
- You can use this [postman collection](bms_apis.postman_collection.json) for testing APIs.

## Notes
- DRF's Viewsets and django filters are use which provide great extensibility and helped to reduce code duplication
